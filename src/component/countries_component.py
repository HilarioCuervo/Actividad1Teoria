import PySimpleGUI as sg
import time
from src.windows import countries_window
from src.handlers import countries_handler


def start():
    ''' Funcion encargada de iniciar la ventana de datos de paises ''' 

    window = loop()
    window.close()


def loop():
    ''' Funcion encargada de captar los eventos de la ventana de paises '''

    # Guarda en data los datos a mostrar en pantalla
    data = countries_handler.get_data()
    window = countries_window.build(data)

    while True:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        time.sleep(0.2)

    return window