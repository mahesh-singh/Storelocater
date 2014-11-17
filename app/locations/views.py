from flask import Blueprint, request, render_template, redirect, url_for
from flask.ext.login import login_user, login_required

from app import db
from app.locations.models import Location
from app.locations.forms import LocationForm

mod = Blueprint('location', __name__, url_prefix='/location')

@mod.route('/')
@login_required
def home():
	return render_template('locations/index.html')


@mod.route('/add')
@login_required
def add():
	locationForm = LocationForm(request.form)
	return render_template('locations/add.html', form = locationForm)