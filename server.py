from bottle import route, run
from bottle import template
from bottle import get, post, request # or route
from bottle import static_file
from bottle import response
from bottle import error

#defining check_login function:
def check_login(user, passwd):
	username = 'rfBone'
	password = 'bone32'
	log = True if (user == username) else False
	pw = True if (passwd == password) else False
	if log == True :
		if pw == True :
			return 'a'
		else:
			return 'b'
	else :
		return 'c'	

@route('/hi')
def hello():
	return "Hello There!"

@route('/<name>/greet')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)

@route('/')
def server_static():
	return static_file('index.html', root='./')

@route('/<location>')
def server_static(location):
	return static_file(location + '.html', root='./')

@route('/<path:path>')
def server_static(path):
	return static_file(path, root='./')

def server_static(path):
	return static_file(path, root='./')

def server_static(path):
	return static_file(path, root='./')

@get('/login') # or @route('/login')
def login_cookie():
	if request.get_cookie("visited"):
		return static_file('log.html', root='./')
	else:
		return static_file('login.html', root='./')

@post('/login') # or @route('/login', method='POST')
def server_static():
	usr = request.forms.get('username')
	pwd = request.forms.get('password')
	ans = check_login(usr, pwd)
	if ans == 'a':
		response.set_cookie("visited", "yes")
		return static_file('log.html', root='./')
	elif ans == 'b':
		return static_file('badpw.html', root='./')
	else: 
		return static_file('badlog.html', root='./')

@error(404)
def error404(error):
	return 'Nothing here, sorry'

@route('/hw_cookie')
def hello_again():
	if request.get_cookie("visited"):
		return "Welcome back! Nice to see you again"
	else:
		response.set_cookie("visited", "yes")
		return "Hello there! Nice to meet you"

run(host='0.0.0.0', port=80, debug=True)


