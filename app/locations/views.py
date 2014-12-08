from flask import Blueprint, request, render_template, redirect, url_for, g
from flask.ext.login import login_user, login_required

from app import db
from app.locations.models import Location, Opening
from app.locations.forms import LocationAddForm

mod = Blueprint('locations', __name__, url_prefix='/location')

@mod.route('/')
@login_required
def home():
	#get current userid
	user_id = g.user.id
	locations = Location.query.filter_by(id = user_id)
	return render_template('locations/index.html', locations = locations)


@mod.route('/add')
@login_required
def add():
	locationAddForm = LocationAddForm(request.form)
	
	return render_template('locations/add.html', form = locationAddForm)