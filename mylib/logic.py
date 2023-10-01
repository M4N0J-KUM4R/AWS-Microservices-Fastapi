import wikipedia
from textblob import TextBlob


def wiki(name="War Goddess", length=1):
    """This is a Wikipedia fetcher"""

    my_wiki = wikipedia.summary(name, sentences=length)
    return my_wiki


def search_wiki(name):
    """Search Wikipedia for Names"""
    results = wikipedia.search(name)
    return results


def phrase(name):
    """Returns a phrase from a Wikipedia"""

    page = wiki(name)
    blob = TextBlob(page)
    return blob.noun_phrases
