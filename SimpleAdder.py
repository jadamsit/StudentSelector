import PySimpleGUI as sg

#1. Create the Layout
layout = [  [sg.Text('Add Two Numbers')],
            [sg.InputText(size=(8,1),key='in1'),sg.Text(" + "),sg.InputText(size=(8,1),key="in2"),sg.Text(" = "),sg.Text('',size=(8,1),key='answer')],
            [sg.Text('')],
            [sg.ReadButton('Add')]
            ]

#2. Create the Window
window = sg.Window('Student Selector').Layout(layout)

#3. event loop
while True:
    button, values = window.Read()

    if button is None:
        break

    num1 = int(values['in1'])
    num2 = int(values['in2'])

    answer = num1 + num2

    window.FindElement('answer').Update(answer)
