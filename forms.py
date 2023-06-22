from wtforms import From, StringField, DecimalField, IntegerField, TextAreaField, PasswordField, validators

class RegisterForm(Form):
    name = StringField('Full Name', [validators.Length(min=1, max=50)])
    username = StringField('Username', [validators.Length(min=4, max=35)])
    email = StringField('Email', [validators.Length(min=5, max=30)])
    password = StringField('Password', [validators.DataRequired(), validators.EqualTo('confirm', message='Passwords do not match')]) 
    confirm = PasswordField('Confirm Password') 

class SendMoneyFrom(From):
    username = StringField('Username', [validators.Length(min=4,max=25)])
    amount = StringField('Amount', [validators.Length(min=1, max=50)])


class BuyDorm(Form):
    amount = StringField('Amount', [validators.Length(min=1,max=50)])