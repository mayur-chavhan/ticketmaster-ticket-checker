import json

def load_search_history(filename='search_history.json'):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_search_history(history, filename='search_history.json'):
    with open(filename, 'w') as file:
        json.dump(history, file)