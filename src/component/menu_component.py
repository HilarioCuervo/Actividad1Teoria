import PySimpleGUI as sg
import time
from src.windows import menu_window
from src.component import disney_component, countries_component


def start():
    ''' Funcion encargada de iniciar la ventana del menu ''' 

    window = loop()
    window.close()


def loop():
    ''' Funcion encargada de captar los eventos de la ventana del menu '''

    window = menu_window.build()

    while True:

        event, values = window.read()

        if event == '-Exit-':
            break

        if event == '-Disney-':
            window.hide()
            disney_component.start()
            window.un_hide()

        if event == '-Countries-':
            window.hide()
            countries_component.start()
            window.un_hide()

        time.sleep(0.2)

    return window
