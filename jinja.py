# {{ }} expression to output data
# {% %} statement to control logic
# {% for %} loop to iterate over data
# {% if %} condition to check data
# {% block %} define blocks for inheritance
# {#...#} comment to ignore content
# Flask application with Jinja2 templating
# Jinja2 is a templating engine for Python, commonly used with Flask.
# This code demonstrates a simple Flask application that uses Jinja2 templates
# to render HTML pages and handle form submissions.


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

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        return f"Form submitted! Name: {name}"
    return render_template('form.html')

@app.route("/success/<int:score>")
def success(score):
    #return f"Your score is {score}."
    res = ''
    if score >= 50:
        res = "Congratulations! You passed the exam."
    else:
        res = "Sorry, you did not pass the exam."
    
    return render_template('success.html', score=score, result=res)

@app.route("/successres/<int:score>")
def successres(score):
    #return f"Your score is {score}."
    res = ''
    if score >= 50:
        res = "Congratulations! You passed the exam."
    else:
        res = "Sorry, you did not pass the exam."
    
    exp = {'score': score} #'result': res
    return render_template('result.html', score=score, result=exp)

if __name__ == '__main__':
    app.run(debug=True)