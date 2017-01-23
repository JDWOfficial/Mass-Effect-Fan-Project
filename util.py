from json import load as load_json


def get_str():
    with open('strings.json') as f:
        try:
            return load_json(f)
        except ValueError:
            print('Failed to load strings!')
