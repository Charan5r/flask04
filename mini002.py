from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def input_page():
    return render_template("input.html")
@app.route("/hello")
def handle_request():
    userName = request.args.get('userName')
    company = request.args.get('company')
    yoj = request.args.get('year')
    exp = 2021-int(yoj)
    return render_template('result.html', x=userName, y=company, z=yoj, v=exp)

app.run(port=5003)