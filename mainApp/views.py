#! /usr/bin/env python3
# coding: utf-8

# import dependencies
from flask import Flask, render_template


# instantiate flask app
app = Flask(__name__)
app.config.from_object('config')

@app.route('/')
@app.route('/index/')
def index():
    """ view index """
    return render_template('index.html')


# if not import launch main
if __name__ == '__main__':
    app.run()