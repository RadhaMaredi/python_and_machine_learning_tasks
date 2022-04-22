from flask import Flask,render_template,request,redirect
import mysql.connector

app = Flask(__name__)

#connecting to the mysql database
conn = mysql.connector.connect(host='localhost',username="root", database="crud")
cursor = conn.cursor()

@app.route('/')
def login():

    """this function navigates to the login page"""

    return render_template("login.html")

@app.route('/register/')
def register():

    """this function navigates to the register page"""

    return render_template("register.html")

@app.route("/home")
def home():

    """this function navigates to the home page"""

    return render_template("home.html")

@app.route('/login_validation', methods=['POST'])
def login_validation():

    """it gets login details from the user and compare with the database data.
    if details are matched it goes to further else it returns the error text"""

    email = request.form.get('email')
    password= request.form.get('password')

    cursor.execute("""SELECT * FROM logins WHERE email LIKE '{}' AND password LIKE '{}' """
                    .format(email, password))
    users = cursor.fetchall()
    
    #compare with the database data
    if len(users)>0:
        return redirect('/home')
    else: 
        return "<h1>Please Register<h1>"
    
@app.route('/add_user', methods=["POST"])
def add_user():

    """it takes required details from the user and store details
    into the database table."""

    name= request.form.get('u_name')
    email = request.form.get('u_email')
    password = request.form.get('u_password')

    cursor.execute("""INSERT INTO logins (name, email,password) VALUES
                (%s, %s, %s)""",(name,email,password))        
    conn.commit()

    return "<h1>Registered successfully<h1>"

#driver code
if __name__=="__main__":
    app.run(debug=True)