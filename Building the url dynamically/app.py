from flask import Flask,redirect,url_for
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Hi I am Satish"

@app.route('/passed/<int:score>')
def passed(score):
    return f"Congratulations! You have passed with a score of {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"Congratulations! You have failed with a score of {score}"

@app.route('/results/<int:marks>')
def results(marks):
    result =""
    if marks < 50:
        result = "fail"
    else:
        result = "passed"
    return redirect(url_for(result, score=marks))

#there is some error in the code please correct it for me please?
    

if __name__ == "__main__":
    app.run(debug=True)
    