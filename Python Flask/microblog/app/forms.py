from flask_wtf import Form
from wtforms import StringField, BooleanField 
from wtforms.validators import DataRequired


class LoginForm(Form):
    # checks to make sure you inputed something in the text field 
    openid = StringField('openid', validators=[DataRequired()])
    # creates a remember me option to leave a cookie 
    remember_me = BooleanField('remember_me', default=False)

        
        