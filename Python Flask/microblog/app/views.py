from app import app
from flask import flash, redirect
from flask.templating import render_template
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'}  # fake user
    posts = [  # fake array of posts
        { 
            'author': {'nickname': 'John'}, 
            'body': 'Beautiful day in Portland!' 
        },
        { 
            'author': {'nickname': 'Susan'}, 
            'body': 'The Avengers movie was so cool!' 
        }
    ]
    # render the page and have it show the variables 
    return render_template("index.html",
                           title='Home',
                           user=user,
                           posts=posts)

# method that handles the login 
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s'%
              (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html', 
                           title='Sign In', 
                           form=form,
                           # scans the list to check if you have used an openid provider
                           providers=app.config['OPENID_PROVIDERS'])