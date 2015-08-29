"""Table models and helper function for Project database"""

from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import session, flash, redirect

db = SQLAlchemy()


class User(db.Model):
	"""Stores user information"""

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	email = db.Column(db.String(50), nullable=False, unique=True)
	user_name = db.Column(db.String(20), nullable=False, unique=True)
	password = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		"""Represent info about user"""

		return "<User user_id=%d email=%s>" % (self.user_id, self.email)


class Post_type(db.Model):
	"""Determines if a post if a wanted item, or an item to share"""

	__tablename__ = "post_types"

	post_type_id = db.Column(db.String(6), primary_key=True)

	def __repr__(self):
		"""Represent info about Post_type"""

		return "<Post_type post_type_id=%s>" % (self.post_type_id)

class Size(db.Model):
	"""Stores sizing iformation for post"""

	__tablename__ = "sizing"

	sizes = db.Column(db.Integer, primary_key=True)

	def __repr__(self):
		"""Represent info about Size"""

		return "<Size sizes=%d>" % (self.sizes)

class Style_code(db.Model):
	"""Stores what style a posting is, e.g. Formal/Business Casual/etc"""

	__tablename__ = "styling"

	code_id = db.Column(db.String(6), primary_key=True)
	code_desc = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		"""Represent info about styling"""

		return "<Style_code code_id=%s code_desc=%s>" % (self.code_id, 
			self.code_desc)

class Clothing_type(db.Model):
	"""Stores item type of clothing, e.g. pants/skirt/shirt/dress"""

	__tablename__ = "clothing_types"

	type_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	type_desc = db.Column(db.String(20), nullable=False)

	def __repr__(self):
		"""Represent info about clothing_types"""

		return "<Clothing_type type_desc=%s>" % (self.type_desc)

class Post(db.Model):
	"""Where all of the information of an individual post is kept"""

	__tablename__ = "posting"

	post_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
	size = db.Column(db.Integer, db.ForeignKey("sizing.sizes"))
	style = db.Column(db.String(6), db.ForeignKey('styling.code_id'), 
		nullable=False)
	item_type = db.Column(db.String(20), db.ForeignKey(
		'clothing_types.type_desc'), nullable=False)
	active = db.Column(db.Boolean, unique=False, default=True)
	user_email = db.Column(db.String(50), db.ForeignKey('users.email'
		), nullable=False)
	post_types = db.Column(db.String(5), db.ForeignKey(
		'post_types.post_type_id'), nullable=False)
	pic = db.Column(db.String(200), nullable=True)

	

	post_sizes = db.relationship("Size", 
		backref=db.backref("posting", order_by=size))
	
	styles = db.relationship("Style_code", 
		backref=db.backref("posting", order_by=style))
	
	item_types = db.relationship("Clothing_type", 
		backref=db.backref("posting", order_by=item_type))
	
	email = db.relationship("User", 
		backref=db.backref("posting", order_by=user_email))
	
	types = db.relationship("Post_type", 
		backref=db.backref("posting", order_by=post_types))

	def __repr__(self):
		"""Represent info from posting table"""

		return "<Post post_id=%d item_type=%s user_email=%s>" % (
			self.post_id, self.item_type, self.user_email)



#Helper functions 

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get('user_id') is not None:
            return f(*args, **kwargs)
        else:
            flash('You must be logged in to see this page.')
            return redirect('/login')
    return decorated_function      

def init_app():

    from flask import Flask
    app = Flask(__name__)

    connect_to_db(app)

def connect_to_db(app):
    """Connect the database to our Flask app."""

    # Configure to use our SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projects.db'
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
