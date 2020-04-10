from flask import Flask, render_template

app = Flask(__name__)


#############################
##   ROUTES
#############################

## Home route

@app.route('/')
def home():
    return render_template('home.html')

## About route

@app.route('/about')
def about():
    return 'Yo from the about route of the url shortener '

