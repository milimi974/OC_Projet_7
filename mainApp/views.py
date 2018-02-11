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


def result():
    """ display result of ajax request """
    return "Result"


def get_location(question):
    """ return location from GOOGLE API """

    return "Answer Google Api for " + question


def get_story(text):
    """ return story of title from WIKI API """

    return "Answer Wiki Api for " + text

# if not import launch main
if __name__ == '__main__':
    app.run()
