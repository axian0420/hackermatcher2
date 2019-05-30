from mongoengine import *
from mongoengine import StringField, EmailField, DateTimeField
import datetime
from flaskblog import login_manager, app
from flask_login import UserMixin
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from bson.json_util import loads, dumps

@login_manager.user_loader
def load_user(user_id):
    for query in User.objects(id=user_id): 
        return query


class User(Document, UserMixin):
    username = StringField(max_length=60, required=True, unique=True)
    email = EmailField(required=True,unique=True)
    password = StringField(max_length=70)
    image_file = StringField(default="default.jpg")
    posts = ReferenceField('Post')

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

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    date_posted = DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return f"Post('{self.title}', '{self.date_posted}')"

#ross = Post(title='noo@example.com', content='what the heck', author='noo').save()
