# This is a sample Python script.
from flask import Flask, render_template
import pandas

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
app = Flask("Website")


@app.route("/")
def home():
    return render_template("home.html")


#@app.route("/about/")
#def about():
 #   return render_template("about.html")

@app.route("/tutorial/")
def tutorial():
    return render_template("tutorial.html")

@app.route("/api/v1/<stations>/<date>")
def about(station, date):
    temperatue = 23
    df = pandas.read_csv("")
    return render_template("about.html")


app.run(debug=True)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
