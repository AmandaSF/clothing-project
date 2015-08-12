from jinja2 import StrictUndefined
#to make sure that errors cannot fail silently
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, init_app, Clothing_type, Style_code, User, Post, Size

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	"""renders homepage information"""

	return render_template("homepage.html")

@app.route('/form', methods=['GET'])
def form_holder():
    """renders clothing form"""

    sizes = Size.query.all()
    style_code = Style_code.query.all()
    item_type = Clothing_type.query.all()
    return render_template('form.html', sizes=sizes, style_code=style_code,
        item_type=item_type)

@app.route('/process-form', methods=['POST'])
def process_form():
    """Adds form results to database table Share or Wish"""

    user_email = request.form['email']
    post_type = request.form['post_type']
    size = request.form['size']
    style = request.form['style']
    item_type = request.form['type']
    photo = request.form['photo_url']
    
    new_post = Post(size=size, style=style, item_type=item_type,
        user_email=user_email, post_types=post_type, pic=photo)

    db.session.add(new_post)
    db.session.commit()

    flash("Your posting has been added!")
    return redirect('/')

@app.route('/test', methods=['GET'])
def test():
    """test things"""
   
    return render_template('test.html')

@app.route('/process-test', methods=["POST"])
def process_test():


    email = request.form["email"]

    new_user = User(email=email)

    db.session.add(new_user)
    db.session.commit()

    flash('%s' % email)
    return redirect('/')

@app.route('/button')
def button():

    size = Size.query.first()
    thing = size.sizes

    flash("does this even work? %s" % thing)
    return redirect('/')


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension. Also, don't forget to 
    #change it to false before releasing it onto the internet!
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()