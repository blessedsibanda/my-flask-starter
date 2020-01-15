from datetime import datetime

from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SECRET_KEY'] = '\x03g\x8a\xcc_\t\xefw\xe1\x0e\x92\xa9\xd7\xea1\x8b'

class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    ip_addr = request.remote_addr
    name = None 
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data 
        form.name.data = ''
    return render_template('index.html', ip_addr=ip_addr, current_time=datetime.utcnow(), form=form, name=name)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500