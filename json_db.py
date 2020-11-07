import json
#from config import path


PATH = 'json_base.json'

def read_file():
    try:
        with open(PATH) as file:
            return json.load(file)
    except Exception as ex:
        return str(ex)

def write_file(write_object):
    try:
        with open(PATH, 'w') as file:
            json.dump(write_object, file)
            return 0
    except Exception as ex:
        return str(ex)