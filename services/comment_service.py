import json

def load_comments():
    with open("data/sample_comments.json", "r") as file:
        return json.load(file)
