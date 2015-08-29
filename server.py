from jinja2 import StrictUndefined
#to make sure that errors cannot fail silently
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from model import connect_to_db, db, init_app, login_required
from model import Clothing_type, Style_code, User, Post, Size

app = Flask(__name__)
app.secret_key = "ABC"
app.jinja_env.undefined = StrictUndefined




@app.route('/')
def homepage():
    """renders homepage information"""
	
    share = db.session.query(Post, User).join(User).filter(db.and_(
    	Post.post_types == "Share", Post.active == True)).all()
    wish = db.session.query(Post, User).join(User).filter(db.and_(
    	Post.post_types == "Wish", Post.active == True)).all()

    return render_template("homepage.html", share=share, wish=wish)


@app.route('/new-posting', methods=['GET'])
@login_required
def form_holder():
    """renders clothing form"""

    sizes = Size.query.all()
    style_code = Style_code.query.all()
    item_type = Clothing_type.query.all()

    return render_template('new_posting.html', sizes=sizes, style_code=style_code,
        item_type=item_type)

@app.route('/new-posting', methods=['POST'])
@login_required
def process_form():
    """Adds form results to database table Share or Wish"""

    current_user = session.get("user_id")
    print "look at this"
    user = User.query.filter(User.user_id == current_user).first()
    print "right here"
    user_email = user.email
    print user_email
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


    name = request.form["name"]
    password = request.form['password']

    user = User.query.filter(db.or_(User.email == name, 
        User.user_name == name)).first()

    if not user:
        flash("Incorrect email or username!")
        return redirect("/login")

    if user.password != password:
        flash("Incorrect password")
        return redirect("/login")


    session["user_id"] = user.user_id
    return redirect("/")

@app.route('/user-page')
@login_required
def user_page():
    """displays relevent user information"""

    current_user = session.get("user_id")
    user = User.query.filter(User.user_id == current_user).first()

    share = Post.query.filter(db.and_(Post.user_email == user.email,
    	Post.active == True, Post.post_types == "Share")).all()
    wish = Post.query.filter(db.and_(Post.user_email == user.email,
    	Post.active == True, Post.post_types == "Wish")).all()


    return render_template('user_page.html', user=user, 
    	share=share, wish=wish)



@app.route('/register-form', methods=['GET'])
def register_form():
    """processes registration."""

    return render_template("register.html")

@app.route('/register', methods=['POST'])
def process_registration():
    """Registers new users"""

    email = request.form['email']
    user_name = request.form['username']
    password = request.form['password']

    new_user = User(email=email, user_name=user_name, password=password)

    db.session.add(new_user)
    db.session.commit()

    user = User.query.filter(User.email == email).first()
    session["user_id"] = user.user_name

    flash('Welcome %s' % user_name)
    return redirect('/')

@app.route('/logout')
def logout():
    """logout user."""

    del session['user_id']
    return redirect('/')
   

@app.route('/update-user')
def update_user_form():
    """Updates User Information"""

    return render_template('user_update.html')


@app.route('/update-user', methods=['POST'])
def process_update_user():
    """Updates User Information to database."""

    user_id = session.get('user_id')
    user = User.query.filter(User.user_id == user_id).first()

    username = request.form['username']
    email = request.form['email']
    password = request.form['password']


    if len(username) > 0:
        user.user_name = username
        db.session.commit()
        flash("Your Username is now %s" % username)
    if len(email) > 0:
        user.email = email
        db.session.commit()
        flash("Your Email is now %s" % email)
    if len(password) > 0:
        user.password = password
        db.session.commit()
        flash("Your password has been updated.")

    return redirect('/')

@app.route('/post-update')
def select_post_update():
	"""renders post selection form"""

	current_user = session.get("user_id")
	user = User.query.filter(User.user_id == current_user).first()
	post = Post.query.filter(db.and_(Post.user_email == user.email,
		Post.active == True)).all()
	

	return render_template('select_post.html', post=post)

@app.route('/post-update/<int:post_id>')
def update_post(post_id):
	"""allows postings to be updated"""

	post = Post.query.filter(Post.post_id == post_id).first()

	return render_template('post_update.html', post=post)

@app.route('/post-update/update/<int:post_id>', methods=['POST'])
def proccess_update_post(post_id):
	"""proccess the update of a user's post"""

	post = Post.query.filter(Post.post_id == post_id).first()
	photo = request.form['photo_url']

	if len(photo) > 0:
		post.pic = photo
		db.session.commit()
		flash("Your photo has been updated.")
	
	return redirect('/user-page')

@app.route('/delete-posting')
def delete_posting():
	"""renders the template for deativating postings"""

	current_user = session.get("user_id")
	user = User.query.filter(User.user_id == current_user).first()
	post = Post.query.filter(db.and_(Post.user_email == user.email,
		Post.active == True)).all()

	return render_template('delete_posting.html', post=post)

@app.route('/delete-posting', methods=['POST'])
def proccess_delete_posting():
	"""Assigns an inactive value to postings."""

	selected_posts = request.form.getlist('posting')

	for item in selected_posts:
	  	post = Post.query.filter(Post.post_id == item).first()
		post.active = False
		db.session.commit()

	flash("The selected posts have been deleted.")
	return redirect('/user-page')

@app.route('/faq')
def faq():
	"""renders faq page"""

	return render_template('faq.html')

@app.route('/test')
def test():
    """test function"""
    
   
    return render_template('test_function.html')




if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension. Also, don't forget to 
    #change it to false before releasing it onto the internet!
    app.debug = False

    connect_to_db(app)

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run()