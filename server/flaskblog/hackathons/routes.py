from flask import Blueprint
from flask import render_template, url_for, flash, redirect, request, session
from flaskblog import app
from flaskblog.models import User, Hackathon
from flask_login import current_user

hackathons = Blueprint('hackathons', __name__)

def hackathon_invalid(hackathon):
	if not current_user.is_authenticated or current_user.preferences == None:
		return render_template('hackathon.html', hackathon=hackathon, authenticated=False)
	if len(hackathon.hackers) == 0:
		return render_template('hackathon.html', hackathon=hackathon, authenticated=True, tophackers=None)
	if len(hackathon.hackers) <= 10:
		return render_template('hackathon.html', hackathon=hackathon, authenticated=True, tophackers=hackathon.hackers)
	return

@hackathons.route('/hackathons/<string:hackathon_id>', methods=["GET"])
def hackathon(hackathon_id):
	for query in Hackathon.objects(id=hackathon_id): hackathon = query
	hackathon_invalid(hackathon)
	# make prediction
