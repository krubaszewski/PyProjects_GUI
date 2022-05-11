import PySimpleGUI as sg

layout = [  [sg.Text('My Window')],
            [sg.Input(key='-IN-', enable_events=True)],
            [sg.Button('Go'), sg.Button('Exit')]  ]

window = sg.Window('Window Title', layout)

while True:             # Event Loop
    event, values = window.read()
    if event in (None, 'Exit'):
        break
    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('0123456789.'):
        window['-IN-'].update(values['-IN-'][:-1])
window.close()