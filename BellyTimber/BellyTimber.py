from flask import Flask, render_template
app= Flask(__name__)


@app.route("/")
@app.route("/home")
def home():
	return render_template('home.html')



@app.route("/place_order")
def place_order():
	return render_template('order.html')


if __name__ == '__main__':
	app.run(debug=True)