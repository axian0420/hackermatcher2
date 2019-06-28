$(document).ready(function() {
	const convo_id_url = window.location.href.substring(window.location.href.lastIndexOf('/') + 1);
	var socket = io.connect('http://127.0.0.1:5000');

	//join room
	socket.emit('join_private', {room:convo_id_url})



	socket.on('connect', function() {
		socket.send('User has connected!');
		// todo: handle user online 
	});
	// todo: disconnect doesn't detect
	socket.on('disconnect', function(){
		socket.send('AHHHUser has disconnect!');
		// todo: handle user disconnect 
	});

	socket.on('private_message', function (msg) {
		$("#messages").append('<li><img height="30px" width="30px" src=/static/profile_pics/'+msg['picture']+' />'+msg['sender']+':'+msg['message']+'</li>');
	  });

	//typing
	$('#myMessage').bind("keypress", ()=>{
		socket.emit('typing', {room:convo_id_url});
	});

	//send private message
	$('#sendbutton').on('click', function(event) {
        var message_to_send = $('#myMessage').val();
        socket.emit('private_message', {'room' : convo_id_url, 'message' : message_to_send});
        // saves message to database
        var requestUrl = Flask.url_for('chats.chat', {"convo_id":convo_id_url});
        var data = {"message":$('#myMessage').val()};
		$.ajax({
            type : 'POST',
            contentType: 'application/json',
		    url: requestUrl,
		    dataType : 'json',
            data : JSON.stringify(data)
        })
        .done(function(data) {
            console.log(data);
        }).fail((error)=>{
            console.log(error);
        });
        event.preventDefault();
        $('#myMessage').val('');
	});

	$('#addbutton').on('click', (event)=>{
		var requestUrl = Flask.url_for('chats.new_group_chat');
		var message = $('#groupMessage').val();
		var group = ['5ceffdf2988c45e7e8298a00','5cec23ecf427cb7781d5db67', '5cecac667bdba34aa4571748']
		var data = {"participants":group, "message": message};
		$.ajax({
		    type: 'POST',
		    contentType: 'application/json',
		    url: requestUrl,
		    dataType : 'json',
		    data : JSON.stringify(data)
		})
		.done(function(data) {
            console.log(data);
        }).fail((error)=>{
            console.log(error);
        });
		event.preventDefault();
	})
});