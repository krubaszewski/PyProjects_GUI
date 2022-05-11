from xml.sax.xmlreader import InputSource
import PySimpleGUI as sg

sg.theme('Dark')   # Add a touch of color
# All the stuff inside your window.

default_text_input = "Enter value"
outcome = 0

layout = [  [sg.Text('Enter value to convert:'), sg.Input(do_not_clear=True, key='-IN-', enable_events=True), sg.Combo(['m to km', 'g to kg'], default_value = "m to km", readonly = True, key='-COMBO-'), sg.Button('Convert')],
            [sg.Text( text_color = 'Orange', key = "-OUT-"), sg.Push(), sg.Push(), sg.Push(), sg.Push(), sg.Button('Exit')]]

# Create the Window
window = sg.Window('Converter', layout)

# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    print(event)
    print(values)
    
    if event == sg.WIN_CLOSED or event=="Exit" : # if user closes window 
        break

    if event == '-IN-' and values['-IN-'] and values['-IN-'][-1] not in ('0123456789.'):
        window["-IN-"].Update(values['-IN-'][:-1], visible = True)
        window.Element("-OUT-").Update("You can input values: 0123456789 and . ", visible = True)

    elif values["-IN-"] == '' and event=="Convert":
        window.Element("-OUT-").Update("You didn't type any number! Enter the value!", visible = True)

    elif event=="Convert":
        input_values = values['-IN-']
        match values['-COMBO-']:
            case 'm to km': 
                output = round(float(input_values) / 1000, 4)
                output_string = f'{input_values} meters = {output} kilometers'

            case 'g to kg': 
                output = round(float(input_values) / 1000, 4)
                output_string = f'{input_values} grams = {output} kilograms'

        window.Element("-OUT-").Update(output_string)
    

window.close()