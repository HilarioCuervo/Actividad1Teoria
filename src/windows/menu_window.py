import PySimpleGUI as sg


def build():
    ''' Funcion que construye los elementos de la ventana del menu'''

    layout = [
        [sg.Text('¿Que datos analizamos?', size = (35,1), font = ('Arial', 24), justification = 'center')],
        [sg.Button('Peliculas de Disney', key = '-Disney-', size = (50,2), font = ('Arial', 15), border_width = 2)],
        [sg.Button('Paises del todo el Mundo', key = '-Countries-', size = (50,2), font = ('Arial', 15), border_width = 2)],
        [sg.Button('Salir', key = '-Exit-', size = (50,1), font = ('Arial', 15), button_color = 'red', border_width = 2)]
    ]

    board = sg.Window('Menu', disable_close = True, element_justification = 'c').Layout(layout)

    return board