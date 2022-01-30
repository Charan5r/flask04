from flask import Flask, render_template, request
from sqlite3 import connect

app = Flask(__name__)

@app.route("/")
def handle_input():
    return render_template("sresult.html")

@app.route("/search4")
def do_search():
    phrase = request.args.get("phrase")
    letters = request.args.get("letters")
    result = set(phrase).intersection(set(letters))
    save_search_to_db(phrase, letters, result)
    return render_template("sresult.html", x=phrase, y=letters, z=result)

@app.route("/viewlog")
def get_all_searches():
    con = connect("results_db.sql")
    sql = """SELECT * FROM records"""
    cursor = con.cursor()
    cursor.excute(sql)
    all_searches = cursor.fetchall()
    return render_template("viewallresult.html", x=all_searches)

def save_search_to_db(phrase, letters, result):
    con = connect("create_db.py")
    sql = """insert into records values('%s', '%s', '%s')""" %(phrase, letters, result)
    cursor = con.cursor()
    cursor.execute(sql)
    con.commit()


app.run(port=5002)