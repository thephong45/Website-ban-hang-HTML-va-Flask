from flask import Flask, request, render_template, session
from AdminView import Admin123View
app = Flask(__name__)

Admin123View.register(app, route_base='/admin')
#Duong dan 
@app.route('/')
def hello():
	# string ="""
	# <form action='/new2' method='POST'>
	# 	<input type='text' name= 'soa'>
	# 	<input type='text' name='sob'>
	# 	<input type='submit'>

	# </form>
	# """
	# return string

	# str = "https://www.facebook.com"
	# myname ='phan hoang trung'
	# array = ['ca', 'tom', 'thit']

	return render_template('shop/home.html')



@app.route('/new', methods=['GET'])
def ham():
	gta = request.args.get('soa')
	gtb = request.args.get('sob')
	giatri =  int(gta) + int(gtb)
	return str(giatri)


@app.route('/new2', methods=['POST'])
def ham2():
	gta = request.form['soa']
	gtb = request.form['sob']
	giatri =  int(gta) + int(gtb)
	return str(giatri)

@app.route('/login', methods=['GET', 'POST'])
def hamlogin():
	if request.method == "GET":
		if 'username' in session:
			message = 'xin chao ban: ' + session['username']
			return message
		else:
			return """
			<form action='/login' method='post'>
				Username:
				<input type='text' name='uname'><br>
				Password: 
				<input type='password' name='pass'><br>
				<input type='submit'>


			</form>
			"""
	elif request.method == "POST":
		session['username'] = request.form['uname']
		return """
		<h1>Ban da dang nhap thanh cong</h1>	

		"""
	else:
		return "<h1>Co loi gi do</h1>"




if __name__ == '__main__':
	app.secret_key = "hoangtrungkma"
	app.run(host='192.168.137.5', port='5000')


	
