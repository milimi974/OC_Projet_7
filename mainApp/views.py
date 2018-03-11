#! /usr/bin/env python3
# coding: utf-8

# import dependencies
from flask import Flask, render_template, request, jsonify
from mainApp.utils import *
import requests
import random

# instantiate flask app
app = Flask(__name__)
app.config.from_object('config')

# Constant
GOOGLE_API_KEY = "AIzaSyDsUmBpuxHQ3cb1KBQ-vC-Sk7nz1w5ftxg"
GOOGLE_API_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
GOOGLE_API_DETAILS_URL = "https://maps.googleapis.com/maps/api/place/details/json"
WIKI_URL = "https://fr.wikipedia.org/w/api.php"


@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')


@app.route('/result/', methods=['GET', 'POST'])
def result():
    """ display result of ajax request """
    # parse text before google request
    q = parse_search_request(request.form['q'])
    # get google API information
    google_response = get_location(question=q)

    if google_response:
        # get location story from wiki
        story = get_story(google_response['name'])
        if story == '':
            # if no story get error message
            story = find_grandpy_error_message()
        else:
            story = find_grandpy_story_message(story)

        return render_template('result.html',
                               title=find_grandpy_location_message(google_response['name']),
                               marker=google_response['name'],
                               location=google_response['formatted_address'],
                               id="map{}".format(request.form['id']),
                               localisation=google_response['geometry']['location'],
                               story=story)
    # if no location found return error
    return render_template('error.html',
                           message=find_grandpy_error_message())


def get_location(question):
    """ return location from GOOGLE API """
    # Request to API
    response = get_request_results(url=GOOGLE_API_SEARCH_URL, params={
        "query": question,
        "key": GOOGLE_API_KEY,
        "language": "fr",
    })

    # return answer
    if response["results"]:
        return response["results"][0]

    return False


def get_story(text):
    """ return story of title from WIKI API """
    story = ''
    # Request to API
    response = get_request_results(url=WIKI_URL, params={
        "action": "opensearch",
        "search": text,
    })

    # Random answer
    if response[2]:
        if len(response[2]) == 1:
            story = response[2][0]
        else:
            idx = random.randint(0, len(response[2]))
            story = response[2][idx]
    return story


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