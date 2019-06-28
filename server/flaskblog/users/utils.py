from flask import url_for
from flask_mail import Message
from flaskblog import mail, app
from PIL import Image
import secrets
import os

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)   # returns file type of the file | first variable in file name which is named _ because we won't use it
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn) #full path up till package directory
    # resize picture
    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)
    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    print("routes.py 110", token)
    msg = Message('Password Reset Request', 
                    sender='noreply@demo.com', 
                    recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)} 
    '''
    mail.send(msg)
    print("mail sent!")
