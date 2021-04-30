import PySimpleGUI as sg
import time
from src.windows import disney_window
from src.handlers import disney_handler


def start():
    ''' Funcion encargada de iniciar la ventana de datos de disney ''' 

    window = loop()
    window.close()


def loop():
    ''' Funcion encargada de captar los eventos de la ventana de disney '''

    # Guarda en data los datos a mostrar en pantalla
    data = disney_handler.get_data()
    window = disney_window.build(data)

    while True:

        event, values = window.read()

        if event == sg.WINDOW_CLOSED:
            break

        time.sleep(0.2)

    return window