import PySimpleGUI as sg
import random
import json

def readJSON():
    jsonFile = open('test.json')
    students = json.load(jsonFile)
    return students

def getRandomStudent(students):
    randomStudent = random.randint(0,(len(students)-1))
    return randomStudent

# 1. Create the Layout
layout = [  [sg.Image('images/placeholder.png',size=[340,340],key='image')],
            [sg.Text('_______________', auto_size_text = True, font=["Comic Sans",22],justification="center", pad=(80,0), key='name')],
            [sg.Text('')],
            [sg.Button('Pick Student',pad=(120,0),size=[12,3])],
            [sg.Text('')],
            [sg.Button('Count as Present',pad=(117,0))]
            ]

# 2. Create the Window
window = sg.Window('Student Selector',text_justification='center',resizable=True).Layout(layout)


# 3. event loop
currentStudent = None
students = readJSON()
while True:
    button, values = window.Read()

    if button is None:
        break

    elif button == 'Pick Student':
        students = readJSON()
        currentStudent = getRandomStudent(students)
        window.FindElement('image').Update(students[currentStudent]["image"])
        window.FindElement('name').Update(students[currentStudent]["name"])

    elif button == 'Count as Present':
        print('goodbye')