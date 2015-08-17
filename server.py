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
    share = Post.query.filter(Post.post_types == "Share").all()
    wish = Post.query.filter(Post.post_types == "Wish").all()
    return render_template("homepage.html", share=share, wish=wish)

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

@app.route('/login', methods=['GET'])
def login_form():
    """Shows login form"""
   
    return render_template('login.html')

@app.route('/login', methods=["POST"])
def process_login():


    email = request.form["email"]
    user_name = request.form['username']
    password = request.form['password']

    user = User.query.filter(db.or_(User.email == email, 
        User.user_name == user_name)).first()

    if not user:
        flash("Incorrect email or username!")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")

    session["user_id"] = user.user_id
    flash("Logged in")
    return redirect("/")


@app.route('/register')
def register_form():
    """processes registration."""

    return render_template("register.html")

@app.route('/register', methods=['POST'])
def button():
    """Registers new users"""

    email = request.form['email']
    user_name = request.form['username']
    password = request.form['password']

    new_user = User(email=email, user_name=user_name, password=password)

    db.session.add(new_user)
    db.session.commit()

    flash('Welcome %s' % username)
    return redirect('/')

@app.route('/logout')
def logout():
    """logout user."""

    del session['user_id']
    flash('logged out')
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