#flask is a microwave framework writen in python. it is light weight
from flask import Flask, redirect, url_for

app = Flask(__name__) #instance of the class(obj)

@app.route("/")  #decoratore, declaring path of the result
def home():
    return "<h1>Welcome Flask</h1>"

@app.route("/defination")
def defination():
    return "Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries."

@app.route("/<name>") #dynamic routing
def name(name):
    return f"Hello {name}"

# when we click on one address it will goes to another address

@app.route("/admin")
def admin():
    return redirect("/")


@app.route("/admin")
def admin():
    return redirect(url_for("defination")) # it goes to particular domain






if __name__ == "__main__":
    app.run(debug = True) # run the code, if doesn't give debug = true the it doent update the changes. if we want to update changes we need to run the code again and again
