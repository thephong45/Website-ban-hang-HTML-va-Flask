from flask_classful import FlaskView, route

class Admin123View(FlaskView):
	def index(self):
		return '<h1>Day la view admin</h1>'
	@route('/quanlytaikhoang')
	def quanly(self):
		return "<h1>Day la view quan ly tai khoang !!!</h1>"