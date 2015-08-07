from jinja2 import StrictUndefined
#to make sure that errors cannot fail silently
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, init_app, Clothing_type, Style_code, Size, User, Share, Wish

app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def homepage():
	"""renders homepage information"""

	return render_template("homepage.html")

@app.route('/form')
def form_holder():
    """renders clothing form"""

    sizes = Size.query.all()
    style_code = Style_code.query.all()
    item_type = Clothing_type.query.all()
    return render_template('form.html', sizes=sizes, style_code=style_code,
        item_type=item_type)

@app.route('/process-form')
def process_form():
    """Adds form results to database table Share or Wish"""

    user_email = request.form['email']
    post_type = request.form['post_type']
    size = request.form['size']
    style = request.form['style']
    item_type = request.form['type']
    photo = request.form['photo']

    if post_type is "wish":
        new_wish = Wish(user_email=user_email, size=w_size, style=w_style,
            item_type=w_item_type, photo=w_pic)

        db.session.add(new_wish)

    else:
        new_share = Share(user_email=user_email, size=s_size, style=s_style,
            item_type=s_item_type, photo=w_pic)
        db.session.add(new_share)

    db.session.commit()

    flash("Your posting has been added")
    return redirect('homepage.html')




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension. Also, don't forget to 
    #change it to false before releasing it onto the internet!
    app.debug = True

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()