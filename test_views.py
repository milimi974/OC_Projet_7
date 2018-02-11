# import target test script
import mainApp.views as script
from mainApp.utils import parse_search_request

# Test function get location form google API
def test_get_location():
    assert script.get_location("OpenClassRoom") == "Answer Google Api for OpenClassRoom"


# Test function get_story from wiki API
def test_get_story():
    assert script.get_story("OpenClassRoom") == "Answer Wiki Api for OpenClassRoom"


# Test function result return html
def test_result():
    assert script.result() == "Result"


# Test function word parser
def test_parse_search_request():
    assert parse_search_request("Mon message pour le parser") == "message parser"
