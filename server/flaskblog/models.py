import datetime
from mongoengine import *
from bson.objectid import ObjectId
from flaskblog import login_manager, app
from flask_login import UserMixin
from bson.json_util import loads, dumps
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from mongoengine import StringField, EmailField, DateTimeField, ListField, ObjectIdField, URLField

@login_manager.user_loader
def load_user(user_id):
    for query in User.objects(id=user_id): 
        return query


class User(Document, UserMixin):
    
    username = StringField(max_length=60, required=True, unique=True)
    email = EmailField(required=True,unique=True)
    password = StringField(max_length=70)
    image_file = StringField(default="default.jpg")
    preferences = ListField(default=None)

    def get_reset_token(self, expires_sec=1800):
        #s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return dumps({'user_id': self.id})#.decode('utf-8')

    @staticmethod       # tell python we don't need self as token
    def verify_reset_token(token):
        #s = Serializer(app.config['SECRET_KEY'])
        try:
            # print("models.py 30", token)
            user_id = loads(token)['user_id']
            # print(user_id)
        except:
            return None
        for query in User.objects(id=user_id):
            print("models.py 35", query)
            return query

    def __str__(self):
        return f"User('{self.username}','{self.email}','{self.password}')"

class Hackathon(Document):
    name = StringField(required=True, max_length=60)
    start_date = DateTimeField(required=True)
    end_date = DateTimeField(required=True)
    state = StringField(required=True)
    city = StringField(required=True)
    address = StringField(required=True)
    url = URLField()
    about = StringField()
    logo = StringField()
    school = StringField()
    hackers = ListField()
'''
    # todo: get hackathon season based on start_date: f2017
    def get_season(self):
        if start_date.month <= 6: season = "s"
        else: season = "f"
        return season, start_date.year

    # returns the url_id for this hackathon, used as hackathon_id in url
    # hackathon_name+hackathon_season
    def get_url_id(self):
        season, year = get_season(self)
        return self.name+season+year
'''
class Conversation(Document):
    participants = ListField(StringField())
    last_active_date = DateTimeField(default=datetime.datetime.now())

    # fetches all messages associated with this conversation
    # returns a sorted list of messages ordered by message time
    def fetch_messages(self):
        return None

# TODO: modify conversationId and sender field to objectId fields instead of string
class Message(Document):
    content = StringField(required=True)
    created_date = DateTimeField(default=datetime.datetime.now())
    conversationId = StringField(required=True)
    sender = StringField(required=True)
    

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    date_posted = DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

#ross = Post(title='noo@example.com', content='what the heck', author='noo').save()
