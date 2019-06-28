from flaskblog import app, socketio
from flask_wtf.csrf import CSRFProtect




if __name__ == '__main__':
	csrf = CSRFProtect(app)
	socketio.run(app, debug=True)
    #app.run(debug=True)


