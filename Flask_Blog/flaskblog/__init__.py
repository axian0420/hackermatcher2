
from flask import Flask
app = Flask(__name__)

from mongoengine import *
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

#TODO: fill out secrets here
connect(db='testflask', 
    username='jenny_xu',
    password='qwerty123',
    host='')

db = get_db()
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'		# tells manager where login route is located after @login_required is invoked
login_manager.login_message_category = 'info'	# sets categegory for login message
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = ""
app.config['MAIL_PASSWORD'] = ""
mail = Mail(app)

#import routes
from flaskblog.users.routes import users
from flaskblog.main.routes import main
app.register_blueprint(users)
app.register_blueprint(main)