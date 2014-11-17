from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, EqualTo, Email
import pycountry

class LocationForm(Form):
	name = TextField('Name', [Required()])
	address_one = TextField('Address line 1', [Required()])
	address_two = TextField('Address line 2', [Required()])
	city = TextField('City', [Required()])
	state = TextField('City', [Required()])
	country = SelectField(u'Programming Language', 
		choices=[(country.alpha2, country.name) for country in pycountry.countries]) 
	email = TextField('Email', [Email()])
	url = TextField('URL')
	phone_one = TextField('Primary Phone')
	phone_two = TextField('Alertnate Phone')
	desc = TextAreaField('Description')