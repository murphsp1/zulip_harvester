import json

'''
A few functions to help with data import and export. This module
will hopefully grow and improve with time.
'''

def save_json(filename, data):
    with open(filename, 'wb') as outfile:
        json.dump(data, outfile)


def load_json(filename):
    with open(filename) as infile:
        data = json.load(infile)
    return data
