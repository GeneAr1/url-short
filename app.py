from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)


#############################
##   ROUTES
#############################

## Home route

@app.route('/')
def home():
    return render_template('home.html')

## About route

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        # add a  method to save url's and file rev 1.11
        urls = {}
        urls[request.form['code']] = {'url': request.form['url']}  #save in dict

        with open('urls.json', 'w') as url_file:        #open and save to JSON file
            json.dump(urls, url_file) 

        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))    #redirect to home using url_for if a arrived by GET 