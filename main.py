from flask import Flask,render_template


app=Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/verifier")
def verifier():
    return render_template("verifier.html")


@app.route("/token")
def token():
    return render_template("token.html")


@app.route("/cashcounter")
def cashcounter():
    return render_template("cashcounter.html")


app.run(debug=True)

