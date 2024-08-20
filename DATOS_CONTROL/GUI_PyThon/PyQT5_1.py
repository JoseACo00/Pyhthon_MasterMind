import PySimpleGUI as sg

#
# layout = [[sg.Text("Hola"), sg.Input("")],
#     [sg.Text("Hola Perro")],
#     [sg.Button("OK")]
# ]

button_size= (7,3)

layout = [[sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],
          [sg.Button("", size=button_size), sg.Button("", size=button_size), sg.Button("", size=button_size)],

          [sg.Button("Cerrar")]]

window = sg.Window("Demo", layout, margins=(100, 100)).read()