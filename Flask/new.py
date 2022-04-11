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
    res=""
    if score>=50:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,'res':res}
    return render_template('result.html',result=exp) #sending result to result.html


### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    total_score=0
    if request.method=='POST':
        python=int(request.form['py']) #getting values from the user by using name value from index.html
        english=int(request.form['eng'])
        
        total_score=(python+english)/2

    return redirect(url_for('success',score=total_score)) #redirect to success method

    



if __name__=='__main__':
    app.run(debug=True)