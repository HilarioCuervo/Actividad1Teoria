import PySimpleGUI as sg


def build(data):
    ''' Funcion que construye la interfaz 
        grafica de los datos de los paises '''

    layout = [
        [sg.Text('Los 7 Paises con mayor indice de mortalidad infantil de America Latina/Central: ', size = (50,3), font = ('Arial', 18), justification = 'center')]
    ]

    # Despliega en pantalla cada uno de los datos de data
    for country in data:
        
        layout += [
            [sg.Text(f'{data.index(country) + 1}-  {country[0]}  ----> {country[1]}', size = (50,2), font = ('Arial', 15))]
        ]

    board = sg.Window('Paises').Layout(layout)

    return board