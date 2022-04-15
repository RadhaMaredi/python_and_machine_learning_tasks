#flask is a microwave framework writen in python. it is light weight
from flask import Flask, redirect, url_for

#instance of the class(obj)
app = Flask(__name__) 

#decoratore, declaring path of the result
@app.route("/")
def home():
    return "<h1>Welcome Flask</h1>"

@app.route("/defination")
def defination():
    text = """Flask is a micro web framework written in Python. 
            It is classified as a microframework because
            it does not require particular tools or libraries."""
    return text

@app.route("/<name>") #dynamic routing
def name(name):
    return f"Hello {name}"

# when we click on one address it will goes to another address
@app.route("/admin")
def admin():
    return redirect("/")

@app.route("/admin")
def admin():
    # it goes to particular domain
    return redirect(url_for("defination")) 

#driver code
if __name__ == "__main__":
    # run the code, if doesn't give debug = true the it doent update the changes.
    # if we want to update changes we need to run the code again and again
    app.run(debug = True)
