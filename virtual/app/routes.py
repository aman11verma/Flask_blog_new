from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
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