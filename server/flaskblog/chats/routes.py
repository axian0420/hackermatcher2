import datetime
from flask import Blueprint
from flask import render_template, url_for, request, jsonify, flash, redirect
from flaskblog import app, db, socketio
from flask_login import current_user
from flaskblog.models import User, Conversation, Message
from bson.json_util import dumps
from flask_socketio import send, emit, Namespace, join_room, leave_room

# DEBUG packages
from colorama import Fore

chats = Blueprint('chats', __name__)

@socketio.on('join_private')
def on_join(data):
	room = data['room']
	join_room(room)
	send(current_user.username + ' has entered the room.', room=room)
#	todo: handle no permission

@socketio.on('private_message')#, namespace='/hackrpi')
def private_message(data):
	room = data['room']
	msg = data['message']
	emit('private_message', {'message':msg, 'sender':current_user.username, 'picture': current_user.image_file}, room=room)

@socketio.on('typing')
def on_typing(data):
	room = data['room']
	socket.emit('typing', {user: current_user.username}, room=room)

@socketio.on('leave')
def on_leave(data):
	room = data['room']
	leave_room(room)
	send(current_user.username + ' has left the room.', room=room)

# when B clicks the conversation -> check db to see if B is part of participants for this conversation -> load all messages -> B joins the room
@chats.route("/chat/<string:convo_id>", methods=['GET', 'POST'])
def chat(convo_id):
	if request.method == 'POST':		# message sent, save new message to db
		message = request.get_json()['message']
		msg = Message(sender=str(current_user.id), content=message, conversationId=str(convo_id)).save()
		Conversation.objects(id=convo_id).update_one(last_active_date=datetime.datetime.now())
		return dumps({'success':True}), 200, {'ContentType':'application/json'} 
	elif request.method == 'GET':
		if not current_user.is_authenticated:
			return redirect(url_for('main.home'))
		for query in Conversation.objects(id=convo_id): 
			convo = query
			if str(current_user.id) in convo.participants:
				# load history messages
				history = []
				for query in Message.objects(conversationId=str(convo.id)):
					history.append(query)
				history.sort(key=lambda x: x.created_date, reverse=True)
				profile_pics = {}
				for msg in history:
					if msg.sender not in profile_pics:
						for query in User.objects(id=msg.sender): 
							profile_pics[msg.sender]=query.image_file
				print(profile_pics)
				return render_template('chat.html', history=history, profile_pics=profile_pics)
			else:
				# todo: handle error : you do not have permission to enter this chat
				flash("You do not have permission to enter this chat", "fail")
				return redirect(url_for('main.home'))
		# todo: handle error: conversation not found
		flash("Chat not found", "fail")
		return redirect(url_for('main.home'))

# from ajax post request in profile.html
@chats.route("/new_private_chat/<string:user_id>", methods=['POST'])
def new_private_chat(user_id):
	if request.method == 'POST':		# message sent
		# save new message to database. Create new conversation if conversation does not exist
		message = request.form['message']
		current_participants = [str(current_user.id), user_id]
		convo = None
		for query in Conversation.objects(participants=current_participants): convo = query
		if not convo or convo == None:   #conversation does not exist
			convo = Conversation(participants=current_participants, last_active_date=datetime.datetime.now()).save()
		msg = Message(sender=str(current_user.id), content=message, conversationId=str(convo.id)).save()
		return dumps({'success':True}), 200, {'ContentType':'application/json'}

@chats.route('/new_group_chat', methods=['POST'])
def new_group_chat():
	if request.method == 'POST':
		jsonData = request.get_json()
		participants = jsonData['participants']
		message = jsonData['message']
		# create a group convo
		convo = None
		for query in Conversation.objects(participants=participants): convo = query
		if not convo or convo == None:   #conversation does not exist
			convo = Conversation(participants=participants, last_active_date=datetime.datetime.now()).save()
		msg = Message(sender=str(current_user.id), content=message, conversationId=str(convo.id)).save()
		return dumps({'url':True}), 200, {'ContentType':'application/json'}

# returns all chats the current user is involved, ordered by last_active_date
@chats.route('/all_chats', methods=['GET'])
def all_chats():
	if not current_user.is_authenticated:
		return redirect(url_for('main.home'))
	conversations = []
	for query in Conversation.objects(participants=str(current_user.id)):	
		conversations.append(query)
	conversations.sort(key=lambda x: x.last_active_date, reverse=True)
	return dumps({'data':conversations}), 200, {'ContentType':'application/json'} 


