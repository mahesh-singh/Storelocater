from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, PasswordField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, EqualTo, Email
import pycountry

class LocationAddForm(Form):
	name = TextField('Name', [Required()])
	address_one = TextField('Street address', [Required()])
	address_two = TextField('Address line 2')
	city = TextField('City', [Required()])
	state = TextField('State', [Required()])
	country = SelectField(u'Country', 
		choices=[(country.alpha2, country.name) for country in pycountry.countries]) 
	zip_code = TextField('Zip code')