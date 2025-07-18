from flask import Flask 

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/index')
def index():
    return "This is the index page."

@app.route('/about')
def about():
    return "This is the about page."

if __name__ == '__main__':
    app.run(debug=True)