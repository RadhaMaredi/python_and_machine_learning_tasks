import json
from flask import Flask, render_template, request, redirect, url_for, flash,jsonify
import mysql.connector
from flask_mysqldb import MySQL,MySQLdb 

app = Flask(__name__)

#creating a secret key
app.secret_key = "caircocoders-ednalan"

#connecting to the database       
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_DB'] = 'crud'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/')
def login():

    """this function navigates to the login page"""

    return render_template("login.html")

@app.route('/register/')
def register():

    """this function navigates to the register page"""

    return render_template("register.html")


@app.route('/login_validation', methods=['POST'])
def login_validation():

    """it gets login details from the user and compare with the database data.
    if details are matched it goes to further else it returns the error text"""

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    email = request.form.get('name')
    #dept= request.form.get('dept')
    password = request.form.get('ph')
    
    cursor.execute("""SELECT * FROM students WHERE email LIKE %s AND password LIKE %s"""
                    ,(email, password))
    
    users = cursor.fetchall()
    #print(users)
    #compare with the database data
    if len(users)>0:
        
        return redirect("/index")

    else: 
        message = "please register before login"
        return render_template("login.html", msg = message)
    

@app.route('/add_user', methods=["POST"])
def add_user():

    """it takes required details from the user and store details
    into the database table."""

    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    name= request.form.get('u_name')
    lname = request.form.get('u_username')
    email = request.form.get('u_email')
    password = request.form.get('u_password')

    cursor.execute("""SELECT * FROM students WHERE Email LIKE %s""", [email])
    record = cursor.fetchall()
    if len(record)>=1:
        msg = "This email is already in use. Register with another Email"
        return render_template("register.html", msg=msg)
    else:
        cursor.execute("""INSERT INTO students (fname, lname, email,password) VALUES
                (%s, %s,%s,%s)""",(name,lname,email,password))        
        mysql.connection.commit()
        cursor.execute("""SELECT * FROM students """)
        users = cursor.fetchall()

        return redirect("/index")


@app.route('/jsono') #this link will show the json format of databse table
def rowdic():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   
    s = "SELECT * FROM students"
    cur.execute(s)
    res = cur.fetchall()
    list_rows = json.dumps([dict(r) for r in res])
    #json.dumps used to convert python object to json fromat
 
    return list_rows


#To Read created table
@app.route('/index')
def Index():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)  #cursor is used to read the rows in the table 
    #A cursor that keeps a list of column name is DictCursor

    s = "SELECT * FROM students"
    cur.execute(s) # Execute the SQL
    list_users = cur.fetchall()#fetches a
    print(list_users)
    return render_template('index.html', list_users = list_users)

   

#add an extra row to the table
@app.route('/add_student', methods=['POST'])
def add_student():
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        
        cur.execute("""SELECT * FROM students WHERE email LIKE %s""",[email])
        rec = cur.fetchall()
        if len(rec) >= 1:
            msg = "This email is already in use. Register with another Email" 
            return render_template("index.html", msg=msg)
        else:
            cur.execute("INSERT INTO students (fname, lname, email, password) VALUES (%s,%s,%s,%s)", (fname, lname, email,password))
            mysql.connection.commit()
            cur.close()
            msg = 'Student Added successfully'
            return render_template("index.html", msg=msg)
    return redirect(url_for('Index'))


#to edit the conetents of table
@app.route('/edit/<id>', methods = ['POST', 'GET'])
def get_employee(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor) 
    # DictCursor is a Cursor class that returns rows as dictionaries and stores the result set in the client
   
    cur.execute('SELECT * FROM students WHERE id = %s', [id])
    data = cur.fetchall()#all rows of table are fetched and returned as list of tuples 
    cur.close()
    
    return render_template('edit.html', student = data[0])

#update an row in the table
@app.route('/update/<id>', methods=['POST'])
def update_student(id):

    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
         
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    
        cur.execute("""SELECT * FROM students WHERE email LIKE %s""",[email])
        rec = cur.fetchall()

        if len(rec) >= 1:
            msg = "This email is already in use. update with another Email" 
            return render_template("index.html", msg=msg)
            
        else:
            cur.execute("""
            UPDATE students
            SET fname = %s,
                lname = %s,
                email = %s,
                password = %s
            WHERE id = %s
             """, (fname, lname, email,password, id))
            #flash('Student Updated Successfully')
            mysql.connection.commit()
            msg = 'Student Added successfully'
            return render_template("index.html", msg=msg)

    return redirect(url_for('Index'))        
            
#To delete the row from table
@app.route('/delete/<string:id>', methods = ['POST','GET'])
def delete_student(id):
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
   
    cur.execute('DELETE FROM students WHERE id = {0}'.format(id))
    mysql.connection.commit()
    flash('Student Removed Successfully')
    return redirect(url_for('Index')) 

app.secret_key = 'the random string' 
if __name__ == "__main__":
    app.run(debug=True,port=5600)
   
