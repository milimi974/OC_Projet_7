#! /usr/bin/env python3
# coding: utf-8

# import dependencies
from flask import Flask, render_template, request
import requests


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

def get_request_results(url, params):
    """ return results of the request
        arguments:
        url -- string
        params -- dict
    """
    # send request and store result
    req = requests.get(url, params=params)
    print(req.url)
    # convert result on json
    return req.json()


# if not import launch main
if __name__ == '__main__':
    app.run()
