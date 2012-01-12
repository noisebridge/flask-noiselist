# -*- coding: utf-8 -*-
from flask import Flask, request
from flask import render_template
from model import TodoItem
from model import db


class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True


# create the application
app = Flask(__name__)
app.config.from_object(_DefaultSettings)
del _DefaultSettings


def init_db():
    """ Initialize the database """
    db.create_all()

@app.route('/')
def index():
    todo_list = TodoItem.query.all()
    return render_template('hello.html', todos=todo_list)
    
