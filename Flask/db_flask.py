from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#conigure databaese
db = yaml.load(open("/home/neosoft/Desktop/task/Flask/db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]  #getting host
app.config["MYSQL_USER"] = db["mysql_user"]   
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)   #instance of mysql obj

@app.route("/", methods=["GET", "POST"])
def index():

    """getting data from the user and inserting into database"""

    if request.method == "POST":
        #getting details form the user using request method
        user_details = request.form
        name = user_details["nm"] 
        email = user_details["mail"]

        #post request to make an entry into db
        cur = mysql.connection.cursor()
        #inserting details into database
        cur.execute("INSERT INTO users(name, email) Values (%s, %s)", (name, email))
        mysql.connection.commit()  #it saves the changes in db
        cur.close() #close cursor
        return "<h1>Successfully inserted</h1>"

    else:
        return render_template("form.html")
    
@app.route("/result")
def result():
     
    """ reading the data from the db and return 
    to the users.html file to display the details """

    #GET request to make an entry into db
    cur = mysql.connect.cursor()
    #getting rows from the db
    value_store = cur.execute("SELECT * FROM users")

    #if data base has data it will return to users.html file
    if value_store > 0:
        details = cur.fetchall()
        return render_template("users.html", details = details)
        
    else:
        return "No records found"


if __name__ == "__main__":
    app.run(debug=True)
