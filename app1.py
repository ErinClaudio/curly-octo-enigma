import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Please have a look at these alternative options %s, please Enter Y is yes , Or N if no " %get_close_matches(w, data.keys())[0])
        if yn == "Y" or yn == "y":
            return data[get_close_matches(w,data.keys())[0]]
        elif yn == "N" or yn == "n":
            return "Please double check your word entering another word"
        else:
            return"Please try entering a new word."
    else:
        return"This is not the correct word please try again"

word = input("Enter word:  ")

print(translate(word)) 
