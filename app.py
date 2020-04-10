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

@app.route('/your-url', methods=['GET', 'POST'])
def your_url():
    if request.method == 'POST':
        return render_template('your_url.html', code=request.form['code'])
    else:
        return 'This is not valid'