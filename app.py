from flask import Flask, render_template, request

app = Flask(__name__)


#############################
##   ROUTES
#############################

## Home route

@app.route('/')
def home():
    return render_template('home.html')

## About route

@app.route('/your-url')
def your_url():
    return render_template('your_url.html', code=request.args['code'])