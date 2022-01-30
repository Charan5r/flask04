from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    name = input('enter name:')
    return "hello charan  "+ name

app.run(port=5001)

