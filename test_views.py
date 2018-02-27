# import target test script
import mainApp.views as script
from mainApp.utils import parse_search_request
import urllib.request
from io import BytesIO
import json

GOOGLE_API_KEY = "AIzaSyDsUmBpuxHQ3cb1KBQ-vC-Sk7nz1w5ftxg"
GOOGLE_API_SEARCH_URL = "https://maps.googleapis.com/maps/api/place/textsearch/json"
WIKI_URL = "https://fr.wikipedia.org/w/api.php"


# Test function get location form google API
def test_get_location():
    assert script.get_location("Nice") == "Answer Google Api for OpenClassRoom"


# Test function get_story from wiki API
def test_get_story():
    assert script.get_story("OpenClassRoom") == "Answer Wiki Api for OpenClassRoom"


# Test function result return html
def test_result():
    assert script.result() == "Result"


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

    results = [{
        0: "",
        1: [],
        2: [],
        3: [],
    }]

    def mockreturn(request):
        return BytesIO(json.dumps(results).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)
    assert [script.get_request_results(url=WIKI_URL, params={
        "action": "opensearch",
        "search": "",
    })] == results