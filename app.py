from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os.path

app = Flask(__name__)
app.secret_key = 'test'       #secret key to secure messaging from system to user v1.12


#############################################
##   ROUTES
##############################################

## Home route

@app.route('/')
def home():
    return render_template('home.html')

## your_url route

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':  

        # add a  method to save url's and file rev 1.11
        urls = {}

        #check if url path exixts import and use os.path
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
                #check if short code in urls file to stop overwriting
                if request.form['code'] in urls.keys():
                    flash('That short name has already been taken,  please select another name')
                    return redirect(url_for('home'))      #if key is there redirect back to home page

        urls[request.form['code']] = {'url': request.form['url']}  #save in dict

        with open('urls.json', 'w') as url_file:        #open and save to JSON file
            json.dump(urls, url_file) 

        return render_template('your_url.html', code=request.form['code'], url=request.form['url'])
    else:
        return redirect(url_for('home'))    #redirect to home using url_for if a arrived by GET 