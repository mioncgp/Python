"A simple python interactive dictionary"
import json
from difflib import get_close_matches


with open('data.json') as f:
    data = json.load(f)

#user_input = input("Enter a word: ")

def main():
    """promtpts for an input and asks again"""
    while True:
        user_input = input("Enter a word (q) for quit: ")
        if user_input.lower() == "q":
            break
        iterated_output(find_defenition(user_input))


def find_defenition(word):
    """Take in a word as an argument and finds its defenition"""

    if word.lower() in data.keys():
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper():
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        reprompt = input("Did you mean %s instead?. (Yes/No): " %   get_close_matches(word, data.keys())[0])
        if reprompt.lower() == 'yes':
            return data[get_close_matches(word, data.keys())[0]]
        elif reprompt.lower() == 'no':
            return "No such word in this dictionary."
        else:
            return "Did not understand the entry."
    else:
        return "Sorry, the word does not exist in this dictionary."


def iterated_output(func):
    """take in a function, iterates, prints the output"""
    if type(func) == list:
        for num, item in enumerate(func):
            print(f"{num + 1}: {item}.")
    else:
        print(func)

main()

