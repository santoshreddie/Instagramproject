from statistics import mode
from flask import Flask, render_template, request #importing the necessary libraries 
import pickle

import numpy as np 
app = Flask(__name__)


@app.route('/', methods = ["GET", "POST"])# this code block is to show the user html page to enter the details to be predicted and the clicking the submit button
def hello():
    print("Request for index page received")
    return render_template('index.html')

@app.route('/predict', methods = ['POST']) #This code block is when the user clicked the submit button details from html page will be received using "request.form" and predictio
                                           #will be done based on the array
def prediction():
    if request.method == 'POST':
        ongcc = request.form['ongcc']
        instaverified = request.form['verified']
        isblacklisted = request.form['listed']
        platform = request.form['platform']
        followers = request.form['follower']
        following = request.form['following']
        avgengagements = request.form['engagements']
        avglikes = request.form['likes']
        avgcomments = request.form['comments']
        noofposts = request.form['posts']
        avgreach = request.form['reach']


        data = [[ongcc, instaverified, isblacklisted, platform, followers, following, float(avgengagements), float(avglikes), float(avgcomments), float(noofposts), float(avgreach)]]
        model = pickle.load(open('instamodel.pkl', 'rb'))

        prediction = np.array(model.predict(data)[0])

    return render_template('result.html', n = prediction)# result will be posted on the prediction page

        



if __name__ == '__main__': #main execution code
    app.run()