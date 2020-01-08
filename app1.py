import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return("This is not the correct word please try again")

word = input("Enter word:  ")

print(translate(word)) 
