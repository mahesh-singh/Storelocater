from app import db

class Location(db.Model):
	__tablename__ = 'locations'

	id = db.Column(db.Integer, db.Sequence('location_id_seq'), primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	code = db.Column(db.String(50))
	name = db.Column(db.String(100), nullable=False)
	desc = db.Column(db.String(1000))
	address_one = db.Column(db.String(1000), nullable=False)
	address_two = db.Column(db.String(1000))
	city = db.Column(db.String(100))
	state = db.Column(db.String(100))
	country = db.Column(db.String(100))
	phone_one = db.Column(db.String(100))
	phone_two = db.Column(db.String(100))
	email = db.Column(db.String(200))
	url = db.Column(db.String(1000))
	lon = db.Column(db.Float)
	lat = db.Column(db.Float)
	openings = db.relationship('Opening', backref='openings', lazy='dynamic')
	deleted = db.Column(db.Boolean, default = False)
	published = db.Column(db.Boolean, default = False)
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

	def __init__(self, name, desc, address, phone_one, phone_two, email, url, lon, lat):
		self.name = name
		self.desc = desc
		self.address = address
		self.phone_one = phone_one
		self.phone_two = phone_two
		self.email = email
		self.url = url
		self.lon = lon
		self.lat = lat
			
class Opening(db.Model):
	__tablename__ = 'openings'	
	id = db.Column(db.Integer, db.Sequence('opening_id_seq'), primary_key=True)
	location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
	day = db.Column(db.Integer)
	open_time_one = db.Column(db.Integer)
	close_time_one = db.Column(db.Integer)
	open_time_two = db.Column(db.Integer)
	close_time_two = db.Column(db.Integer)
	closed = db.Column(db.Boolean)
	created_on = db.Column(db.DateTime, default = db.func.now())
	updated_on = db.Column(db.DateTime, default = db.func.now(), onupdate = db.func.now())

	def __init__(self, location_id, day, 
		open_time_one, close_time_one, 
		open_time_two, close_time_two, closed):

		self.location_id = location_id
		self.day = day
		self.open_time_one = open_time_one
		self.close_time_one = close_time_one
		self.open_time_two = open_time_two
		self.close_time_two = close_time_two
		self.closed = closed