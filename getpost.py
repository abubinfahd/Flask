from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Flask App!"

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        return f"Form submitted! Name: {name}"
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)