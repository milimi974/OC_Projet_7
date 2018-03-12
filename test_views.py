# import target test script
import mainApp.views as script
from mainApp.utils import parse_search_request
import urllib.request
from io import BytesIO
import json

from mainApp import app as my_app

import pytest


GOOGLE_API_KEY = "AIzaSyDsUmBpuxHQ3cb1KBQ-vC-Sk7nz1w5ftxg"
GOOGLE_API_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
WIKI_URL = "https://fr.wikipedia.org/w/api.php"


# Test function get location form google API
def test_get_location():

    response = script.get_location("Nice")
    assert 'formatted_address' in response


# Test function get_story from wiki API
def test_get_story():
    response = script.get_story("OpenClassRoom")
    assert type(response) is str


@pytest.fixture
def app():
    app = my_app
    app.debug = True
    return app


# Test function result return html
def test_result(client):
    mimetype = 'text/html'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    data = {
        'q': 'Nice'
    }
    response = client.post('/result/', data=json.dumps(data), headers=headers)

    assert response.content_type == mimetype


# Test function word parser
def test_parse_search_request():
    assert parse_search_request("Mon message pour le parser") == "message parser"


# Mock google API answer
def test_http_google_return(monkeypatch):

    results = [{
        "html_attributions": [],
        "results" : [],
        "status": "INVALID_REQUEST"
    }]

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert [script.get_request_results(url=GOOGLE_API_SEARCH_URL, params={
        "query": "",
        "key": GOOGLE_API_KEY,
        "language": "fr",
    })] == results


# Mock wiki API answer
def test_http_wiki_return(monkeypatch):

    results = ['Nice']

    def mockreturn(request):
        return results
    response = script.get_request_results(url=WIKI_URL, params={
        "action": "opensearch",
        "search":
            "Nice",
    })
    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert response[0] == results[0]

