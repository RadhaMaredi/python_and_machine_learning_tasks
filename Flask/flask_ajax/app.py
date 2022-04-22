#app.py
from flask import Flask, render_template,request, jsonify
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
def index():

    """it give the entire data from the emp table in crud database
    and returned that data to index.html file to display"""

    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cur.execute("SELECT * FROM emp ORDER BY id")
    employee = cur.fetchall()
    return render_template('index.html', employee=employee)
 
@app.route("/ajax_add",methods=["POST","GET"])
def ajax_add():

    """get the user entered details from the form and add
     those details to the database """

    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    #getting user entered details using the name attribute from the form
    if request.method == 'POST':
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(txtname)

        #if the form details are empty show the text to enter details
        if txtname == '':
            msg = 'Please Input name'  
        elif txtdepartment == '':
           msg = 'Please Input Department'  
        elif txtphone == '':
           msg = 'Please Input Phone'  
        else:        
            cur.execute("INSERT INTO emp (name,department,phone) VALUES (%s,%s,%s)",[txtname,txtdepartment,txtphone])
            mysql.connection.commit()       
            cur.close()
            msg = 'New record created successfully' 

    return jsonify(msg)
 
@app.route("/ajax_update",methods=["POST","GET"])
def ajax_update():

    """user can edit the existed details from the database"""

    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == 'POST':
        string = request.form['string']
        txtname = request.form['txtname']
        txtdepartment = request.form['txtdepartment']
        txtphone = request.form['txtphone']
        print(string)

        cur.execute("UPDATE emp SET name = %s, department = %s, phone = %s WHERE id = %s ",
                    [txtname, txtdepartment, txtphone, string])
        mysql.connection.commit()       
        cur.close()
        msg = 'Record successfully Updated'  

    return jsonify(msg)    
 
@app.route("/ajax_delete",methods=["POST","GET"])
def ajax_delete():

    """this method is for delete the particular row from the database"""

    cursor = mysql.connection.cursor()
    cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

    if request.method == 'POST':
        getid = request.form['string']
        print(getid)

        cur.execute('DELETE FROM emp WHERE id = {0}'.format(getid))
        mysql.connection.commit()       
        cur.close()
        msg = 'Record deleted successfully'  

    return jsonify(msg) 
 
 #driver code    
if __name__ == "__main__":
    app.run(debug=True)