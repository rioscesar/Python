''' tutorial from https://stormpath.com/blog/build-a-flask-app-in-30-minutes/
by RANDALL DEGGES ''' 

from datetime import datetime

# flask imports
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    url_for,
                   )

# imports that allow for easy user applications
from flask_stormpath import (
    StormpathError,
    StormpathManager,
    User,
    login_required,
    login_user,
    logout_user,
    user,
    )

# set the app configurations
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SECRET_KEY'] = 'some_really_long_random_string_here'
app.config['STORMPATH_API_KEY_FILE'] =  'apiKey-7AX4LPV2IE7FNUHGVWG9ECZGS.properties'
app.config['STORMPATH_APPLICATION'] = 'flaskr'

stormpath_manager = StormpathManager(app)

# default method that shows the posts
@app.route('/')
def show_posts():
    # create an empty list of posts 
    posts = []
    # run through the accounts and check the posts from users
    for account in stormpath_manager.application.accounts:
        if account.custom_data.get('posts'):
            posts.extend(account.custom_data['posts'])
    # sort the posts by date inserted
    posts = sorted(posts, key=lambda k: k['date'], reverse=True)
    
    return render_template('show_posts.html', posts=posts)

# method that allows the addition of posts 
# only logged in users can post
@app.route('/add', methods=['POST'])
@login_required
def add_post():
    # give the user a custom post dictionary 
    if not user.custom_data.get('posts'):
        user.custom_data['posts'] = []
    
    # insert the data into the posts with date title and text
    user.custom_data['posts'].append({
        'date': datetime.utcnow().isoformat(),
        'title': request.form['title'],
        'text': request.form['text'],
        })
    user.save()
    
    # tell the user that their post was successful
    flash('New Post successfully added.')
    
    # redirection that goes to the post showing
    return redirect(url_for('show_posts'))

# method that attempts to login a user 
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    # attempt to login using email and password
    if request.method == 'POST':
        try:
            _user = User.from_login(
                request.form['email'],
                request.form['password'],
                )
            # everything works and you get to log in 
            login_user(_user, remember=True)
            flash('You were logged in.')
            
            return redirect(url_for('show_posts'))
        except StormpathError, err:
            error = err.message
    
    # else you are not a user and need to log in 
    return render_template('login.html', error=error)

# method that logs out the user 
@app.route('/logout')
def logout():
    logout_user()
    # logs you out
    flash('You were logged out.')
    # redirection to the posts but you can't post
    return redirect(url_for('show_posts'))




if __name__ == '__main__':
    app.run()