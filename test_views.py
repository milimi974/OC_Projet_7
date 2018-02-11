# import target test script
import mainApp.views as script


# Test method get location form google API
def test_get_location():
    assert script.get_location("OpenClassRoom") == "Answer Google Api for OpenClassRoom"


# Test method get_story from wiki API
def test_get_story():
    assert script.get_story("OpenClassRoom") == "Answer Wiki Api for OpenClassRoom"
