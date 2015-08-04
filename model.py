"""Table models and helper function for Project database"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):

	__tablename__ = "users"

	user_id = db.Column(db.Integer, autoincrement=True, nullable=False)
	email = db.Column(db.String(50), nullable=False)

	def __repr__(self):
		"""Represent info about user"""

		return "<User user_id=%d email=%s>" % (self.user_id, self.email)


class Share(db.Model):

	__tablename__ = "sharing"

	share_id = db.Column(db.Integer, autoincrement=True, nullable=False)
	s_size = db.Column(db.Integer, nullable=False)
	s_style = db.Column(db.String(6), nullable=False)
	s_item_type = db.Column(db.String(20), nullable=False)
	s_active = db.Column(db.Boolean, unique=False, default=True)
	user_email = db.Column(db.String(50), ForeignKey('users.email'
		), nullable=False)

	def __repr__(self):
		"""Represent info from Share table"""

		return "<Share share_id=%d s_item_type=%s user_email=%s>" % (
			self.share_id, self.s_item_type, self.user_email)

class Wish(db.Model):

	__tablename__ = "wishing"

	wish_id = db.Column(db.Integer, autoincrement=True, nullable=False)
	w_size = db.Column(db.Integer, nullable=False)
	w_style = db.Column(db.String(6), nullable=False)
	w_item_type = db.Column(db.String(20), nullable=False)
	w_active = db.Column(db.Boolean, unique=False, default=True)
	user_email = db.Column(db.String(50), ForeignKey('users.email'
		), nullable=False)

	def __repr__(self):
		"""Represent info from Wish table"""

		return "<Wish wish_id=%d w_item_type=%s user_email=%s>" % (
			self.wish_id, self.w_item_type, self.user_email)

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
