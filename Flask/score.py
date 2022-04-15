### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''

from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():

    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):

    """ take the avg score and return to the result if he pass or fail """
    
    res=""
    #decide the result
    if score>=50:
        res="PASS"

    else:
        res='FAIL'

    exp={'score':score,'res':res}
    #sending result to result.html
    return render_template('result.html',result=exp) 

#Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():

    """getting details from the user and return the
    avg score to success method"""

    total_score=0

    if request.method=='POST':
        #getting values from the user by using name value from index.html
        python=int(request.form['py']) 
        english=int(request.form['eng'])
    
        total_score=(python+english)/2

    #redirect to success method
    return redirect(url_for('success',score=total_score)) 

#driver code
if __name__=='__main__':
    app.run(debug=True)