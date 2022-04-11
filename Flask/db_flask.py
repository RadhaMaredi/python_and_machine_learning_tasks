from flask import Flask, render_template,request
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

#conigure databaese
db = yaml.load(open("./db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)   #instance of mysql obj

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        #fetch form data
        userDetails = request.form
        name = userDetails["nm"]
        email = userDetails["mail"]

        cur = mysql.connection.cursor() #post request to make an entry into db
        cur.execute("INSERT INTO users(name, email) Values (%s, %s)", (name, email))
        mysql.connection.commit()  #it saves the changes in db
        cur.close() #close cursor
        return "Success"
    return render_template("form.html")

if __name__ == "__main__":
    app.run(debug=True)
