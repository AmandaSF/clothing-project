"""Table models and helper function for Project database"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	email = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		"""Represent info about user"""

		return "<User user_id=%d email=%s>" % (self.user_id, self.email)


class Share(db.Model):

	__tablename__ = "sharing"

	share_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	s_size = db.Column(db.Integer, db.ForeignKey('Size.sizes'), 
		nullable=False)
	s_style = db.Column(db.String(6), db.ForeignKey('Style_code.code_id'), 
		nullable=False)
	s_item_type = db.Column(db.String(20), db.ForeignKey(
		'Clothing_type.type_id'), nullable=False)
	s_active = db.Column(db.Boolean, unique=False, default=True)
	user_email = db.Column(db.String(50), db.ForeignKey('users.email'
		), nullable=False)

	sizes = db.relationship("Size", backref="sharing")
	style = db.relationship("Style_code", backref="sharing")
	item_type = db.relationship("Clothing_type", backref="sharing")
	email = db.relationship("User", backref="sharing")

	def __repr__(self):
		"""Represent info from Share table"""

		return "<Share share_id=%d s_item_type=%s user_email=%s>" % (
			self.share_id, self.s_item_type, self.user_email)

class Wish(db.Model):

	__tablename__ = "wishing"

	wish_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	w_size = db.Column(db.Integer, db.ForeignKey('Size.sizes'), nullable=False)
	w_style = db.Column(db.String(6), db.ForeignKey('Style_code.code_id'), 
		nullable=False)
	w_item_type = db.Column(db.String(20), db.ForeignKey(
		'Clothing_type.type_id'), nullable=False)
	w_active = db.Column(db.Boolean, unique=False, default=True)
	user_email = db.Column(db.String(50), db.ForeignKey('users.email'
		), nullable=False)

	sizes = db.relationship("Size", backref="wishing")
	style = db.relationship("Style_code", backref="wishing")
	item_type = db.relationship("Clothing_type", backref="wishing")
	email = db.relationship("User", backref="wishing")

	def __repr__(self):
		"""Represent info from Wish table"""

		return "<Wish wish_id=%d w_item_type=%s user_email=%s>" % (
			self.wish_id, self.w_item_type, self.user_email)


class Size(db.Model):

	__tablename__ = "sizing"

	sizes = db.Column(db.Integer, primary_key=True)

class Style_code(db.Model):

	__tablename__ = "styling"

	code_id = db.Column(db.String(6), primary_key=True)
	code_desc = db.Column(db.String(20), nullable=False)

class Clothing_type(db.Model):

	__tablename__ = "Clothing_types"

	type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	type_desc = db.Column(db.String(20), nullable=False)



#Helper functions 

def init_app():

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
    app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)


if __name__ == "__main__":
    # As a convenience, if we run this module interactively, it will leave
    # you in a state of being able to work with the database directly.

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)
    print "Connected to DB."
