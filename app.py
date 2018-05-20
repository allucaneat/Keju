from flask import Flask,request
from peneliti import surel as email
app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/peneliti/surel/<fr>')
def home(fr):
	return email.path(fr)

@app.route('/peneliti/surel/<am>')
def home(am):
	return email.path(am)

@app.route('/peneliti/surel/<wa>')
def home(wa):
    return email.path(wa)

@app.route('/peneliti/surel/<gs>')
def home(gs):
    return email.path(gs)

@app.route('/peneliti/surel/<at>')
def home(at):
    return email.path(at)

@app.route('/peneliti/surel/<qq>')
def home(qq):
    return email.path(qq)

@app.route('/peneliti/surel/<ww>')
def home(ww):
    return email.path(ww)
