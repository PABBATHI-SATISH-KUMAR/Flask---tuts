from flask import Flask
app = Flask(__name__)
@app.route('/')
def welcome():
    return "Hi I am Satish"

@app.route('/members')
def members():
    return "I am a DS student member"

if __name__ == "__main__":
    app.run(debug=True)
    