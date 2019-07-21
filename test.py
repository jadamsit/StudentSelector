import json
import random

#with open('test.json') as json_file:
#    list = json.load(json_file)

jsonFile = open('test.json')
students = json.load(jsonFile)

print((students[2]))