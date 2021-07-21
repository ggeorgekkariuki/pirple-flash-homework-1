from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
	return ('Hello World')

@app.route('/about', methods=['GET'])
def about():
	return render_template("about.html")

if __name__ == '__main__':
	app.run(debug=True)