import requests

def write_to_file(filename, text):
    open(filename, 'w').write(text)
    return True
