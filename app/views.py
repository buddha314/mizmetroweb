__author__ = 'buddha'
from . import app
import models
from flask import render_template, flash, redirect, url_for
from flask.ext.security import login_required, current_user



@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"
