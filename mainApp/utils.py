# import dependencies
from mainApp.stop_words import get_stop_words


def parse_search_request(text):
    """ Parse string to remove common word then return result
        argument:
        text -- string
    """
    stopwords = get_stop_words()
    words = text.lower().split(' ')
    for word in list(words):
        if word in stopwords:
            words.remove(word)

    return ' '.join(words)
