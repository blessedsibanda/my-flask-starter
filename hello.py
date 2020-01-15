from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@app.route('/')
def index():
    ip_addr = request.remote_addr
    return render_template('index.html', ip_addr=ip_addr)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)