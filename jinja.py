from flask import Flask, render_template, request, redirect, url_for

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

@app.route("/success/<int:score>")
def success(score):
    res = ''
    if score >= 50:
        res = "Congratulations! You passed the exam."
    else:
        res = "Sorry, you did not pass the exam."
    
    return render_template('success.html', score=score, result=res)

@app.route("/successres/<int:score>")
def successres(score):
    exp = {'score': score} 
    return render_template('result.html', score=score, result=exp)

# Renamed the conflicting function 'submit' to 'submit_scores'
@app.route('/submit_scores', methods=['GET', 'POST'])  # Renamed route function
def submit_scores():
    total_score = 0
    if request.method == 'POST':
        science = int(request.form['science'])
        math = int(request.form['math'])    
        stat = int(request.form['stat'])
        total_score = (science + math + stat)/3
    else:
        return render_template('getresult.html')
    return redirect(url_for('successres', score=total_score))

if __name__ == '__main__':
    app.run(debug=True)
