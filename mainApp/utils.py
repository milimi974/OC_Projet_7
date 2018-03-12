
# import dependencies

import random

import os


def find_grandpy_location_message(text):
    """ return random message
        argument:
        text -- string
    """
    messages = ['Bonjour mon grand tu cherche {} voici sont adresse:',
                'Ohh sache que {} se situe à :',
                'Ma mémoire me fait défault !! mais si je me souviens bien {} se trouve à:',
                'Ha ça me rappel de bon souvenirs de jeunesse {} quand on se promenait à:',
                'je connais pas {}, je dirais au hasard:',
                ]

    idx = random.randint(0, len(messages) - 1)
    # return formated text
    return messages[idx].format(text)


def find_grandpy_story_message(text):
    """ return random message
        argument:
        text -- string
    """
    messages = ['Connais-tu l\'histoire de {}',
                'Hum .. je me rappel que, {}',
                'T\'ai je déjà raconté que, {}',
                'Savais-tu que, {}',
                ]

    idx = random.randint(0, len(messages)  - 1)
    # return formated text
    return messages[idx].format(text)


def find_grandpy_error_message():
    """ return random error message """
    messages = ['J\'ai du mal à comprendre (T_T) ! tu peu préciser ? ',
                'Humm ... connais pas!',
                'Ah je pense que il y a des mots trop compliqués pour moi!!',
                'Si seulement ma mémoire me faisait pas defaut !!! ',
                ]

    index = random.randint(0, len(messages) - 1)
    # return formated text
    return messages[index]


def parse_search_request(text):
    """ Parse string to remove common word then return result
        argument:
        text -- string
    """
    script_dir = os.path.dirname(__file__)
    file = os.path.join(script_dir, 'stop_words.txt')
    # Convert text file on list of words
    text_stop_word = open(file, 'r')
    stopwords = [line.rstrip('\n') for line in text_stop_word.readlines()]

    # Convert search text on list of words
    words = text.lower().split(' ')

    for word in list(words):
        if word in stopwords:
            words.remove(word)

    return ' '.join(words)
