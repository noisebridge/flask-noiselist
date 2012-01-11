# -*- coding: utf-8 -*-
from flask import Flask, request
<<<<<<< HEAD
from flask import render_template
=======
>>>>>>> 469946adad19506bca2be4345498bafb71111de0


class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True


# create the application
app = Flask(__name__)
app.config.from_object(_DefaultSettings)
del _DefaultSettings


def init_db():
    """Create the database tables."""
    pass


@app.route('/')
def index():
<<<<<<< HEAD
    return render_template('hello.html')
    
=======
    if request.args:
        BREAK (with_NameError)
    return 'Hello %s!' % app.config['USERNAME'].title()
>>>>>>> 469946adad19506bca2be4345498bafb71111de0
