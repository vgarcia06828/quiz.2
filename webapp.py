from flask import Flask, redirect, url_for, session, request, jsonify, render_template, flash
from markupsafe import Markup
#from flask_apscheduler import APScheduler
#from apscheduler.schedulers.background import BackgroundScheduler
from flask_oauthlib.client import OAuth
from bson.objectid import ObjectId

import pprint
import os
import time
import pymongo
import sys
 
app = Flask(__name__)

app.debug = False #Change this to False for production
#os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1' #Remove once done debugging

app.secret_key = os.environ['SECRET_KEY'] #used to sign session cookies
oauth = OAuth(app)
oauth.init_app(app) #initialize the app to be able to make requests for user information

#Set up GitHub as OAuth provider
github = oauth.remote_app(
    'github',
    consumer_key=os.environ['GITHUB_CLIENT_ID'], #your web app's "username" for github's OAuth
    consumer_secret=os.environ['GITHUB_CLIENT_SECRET'],#your web app's "password" for github's OAuth
    request_token_params={'scope': 'user:email'}, #request read-only access to the user's email.  For a list of possible scopes, see developer.github.com/apps/building-oauth-apps/scopes-for-oauth-apps
    base_url='https://api.github.com/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',  
    authorize_url='https://github.com/login/oauth/authorize' #URL for github's OAuth login
)

#Connect to database
url = os.environ["MONGO_CONNECTION_STRING"]
client = pymongo.MongoClient(url)
db = client[os.environ["MONGO_DBNAME"]]
collection = db['users'] #TODO: put the name of the collection here

    
@app.route("/home")
def render_home():
    #ans = request.args['an1']
    return render_template('home.html')
    
@app.route("/")
def render_main():
    return render_template('layout.html')
    
@app.route("/pg1")
def render_pg1():
    return render_template('page1.html')
    
@app.route("/pg2")
def render_pg2():
    return render_template('page2.html')

@app.route("/pg3")
def render_pg3():
    return render_template('page3.html')


if __name__ == '__main__':
    app.run(debug=False) # change to False when running in production
