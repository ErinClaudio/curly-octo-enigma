import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input(
            "The word entered closely matches this word: %s, please enter Y if this the word you meant to enter, "
            "Or N if no if not  " %
            get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":  # now a response can be in both lower and upper case
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "Please double check your word entering another word"
        else:
            return "Please try entering a new word."
    else:
        return "This is not the correct word please try again"


word = input("Enter word:  ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
