import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):

    result = "n"
    word = word.lower()
    if word in data:
        return data[word]
    elif word.capitalize() in data:
        return data[word.capitalize()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        matches=get_close_matches(word, data.keys())
        if matches:
            for match in matches:
                result=str(input("Did you mean "+ match + "?(Y/N)"))
                if result.lower() == "y":
                    return data[match]
            if result.lower() == "n":
                return "Word not found"
            else:
                return "Sorry. Incorrect entry."
        else:
          return "Please check the word"


word=str(input("Enter the word to search in dictionary: "))
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
