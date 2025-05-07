from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/passed/<int:score>')
def passed(score):
    return f"Congratulations! You have passed with a score of {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"Sorry! You have failed with a score of {score}"

@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 50:
        result = "fail"
    else:
        result = "passed"
    # Pass the parameter 'score' to match the route definitions
    return redirect(url_for(result, score=marks))

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == 'POST':
        marks = int(request.form['marks'])
        return redirect(url_for('results', marks=marks))
    return render_template('submit.html')

if __name__ == "__main__":
    app.run(debug=True)
