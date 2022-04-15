from flask import Flask,render_template,request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def score_of_sentiment(line):

    """ it takes user text as an input and returns
    the sentimental analysis and polarity score"""

    #object for SentimentIntensityAnalyzer
    obj = SentimentIntensityAnalyzer()
    
    # Polarity, It can be positive, neagtive or neutral.
    dictionary = obj.polarity_scores(line)
    #declare a empty string to store the emotion
    sentiment_analysis = "" 
    
    #decide the analysis
    if dictionary['compound'] >= 0.05:
        sentiment_analysis = "Positive"

    elif dictionary['compound'] <= - 0.05:
        sentiment_analysis = "Negative"

    else:
        sentiment_analysis = "Neutral"

    return sentiment_analysis + " " +str(dictionary['compound'])



app = Flask(__name__)

@app.route('/')
def home():

    """this goes to the html page and excute the html code """

    return render_template('api.html')


@app.route('/text',methods=['GET','POST'])
def text():

    """ this function brings the text from user and 
    that text passed as an argument to the score_of sentiment function 
    by calling the function """

    text = request.form['text']
    result = score_of_sentiment(text)
    return result

app.run(debug=True)