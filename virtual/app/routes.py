from flask import render_template
from app import app
from	app.forms	import	LoginForm

@app.route('/')
@app.route('/index')
@app.route('/login')
def index():
	user = {'username':'Aman'}
	posts =[
	{	
		'author'	:	{'username'	:	'Verma'},
		'body'		:	{'Quarantine is boring'}
	},

	{
		'author'	:	{'username'	:	'Saitama'},
		'body'		:	{'Lets make it fun'}
	}
	]
	return	render_template('index.html',title='Home',user=user,posts=posts)


def login():
	form=LoginForm()
	return	render_template('login.html',	title='Sign	In',form=form)
