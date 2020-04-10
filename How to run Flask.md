How to Install flask on Bash terminal *ie VSCode

# Use the python virtual environment to run the server.   Acts a lot like npm for node systems 
# when installing packages and logging

1> to install pipenv  

# make the directory
$ mkdir   

# install pipenv in directory
$ pip install pipenv   

# create python environment for flask
$pip env install        

$ export FLASK_APP=appname.py
       
$ export FLASK_ENV=development      


# to run environment or to install packages in shell must be in the shell :

#starts shell in production or deve depending on how FLASK_ENV is set.
$ pipenv shell      

# run flask

$ flask run

# installs packages into environment act like nmp install 
# ex pipenv install pkgname where pkgname may equal flask etc
$ pipenv install  *pkg name       




