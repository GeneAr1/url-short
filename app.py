from flask import Flask, render_template, request, redirect, url_for, flash, abort
import json
import os.path
from werkzeug.utils import secure_filename         #secure file name utility

app = Flask(__name__)
app.secret_key = 'test1212121212'  # secret key to secure messaging from system to user v1.12


#############################################
# ROUTES
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

        # check if url path exixts import and use os.path
        if os.path.exists('urls.json'):
            with open('urls.json') as urls_file:
                urls = json.load(urls_file)
                # check if short code in urls file to stop overwriting
                if request.form['code'] in urls.keys():
                    flash(
                        'That short name has already been taken,  please select another name')
                    # if key is there redirect back to home page
                    return redirect(url_for('home'))

        #change code to check logic to decide if url or file ver 1.3

        if 'url' in request.form.keys():
            urls[request.form['code']] = {
                'url': request.form['url']}  # save in dict
        #file is trying to be saved
        else:
            f = request.files['file']
            full_name = request.form['code'] + secure_filename(f.filename)  #secure the file name
            #f.save('C:/Users/GeneA/PythonProjects/url-short/' + full_name)   #add savee location(root)
            f.save('C:/Users/GeneA/PythonProjects/url-short/static/user_files/' + full_name) #to use static folder
            urls[request.form['code']] = {'file': full_name}                #add to JSON

        with open('urls.json', 'w') as url_file:  # open and save to JSON file
            json.dump(urls, url_file)
        
        return render_template('your_url.html', code=request.form['code'])
    else:
        return redirect(url_for('home'))    #redirect to home using url_for if a arrived by GET 

# Variable Route to return websites and files

@app.route('/<string:code>')
def redirect_to_site(code):    
    if os.path.exists('urls.json'):
        with open('urls.json') as urls_file:
            urls = json.load(urls_file)
            if code in urls.keys():
                if 'url' in urls[code].keys():
                    return redirect(urls[code]['url'])
                else:
                    #its a file serve it from the static folder
                    return redirect(url_for('static', filename='user_files/' + urls[code]['file']))

    return abort(404)

# Page not found route

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



