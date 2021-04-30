import PySimpleGUI as sg


def build(data):
    ''' Funcion que construye la interfaz grafica 
        de los datos de las peliculas de disney '''

    window = [
        [sg.Text('Las 10 Peliculas de Disney con mejor taquilla en la Historia: ', size = (50,3), font = ('Arial', 18), justification = 'center')]
    ]

    # Despliega en pantalla cada uno de los datos de data
    for movie in data:

        window += [
            [sg.Text(f'{data.index(movie) + 1}-  {movie[0]}  ----> {movie[1]}', size = (50,2), font = ('Arial', 15))]
        ]

    board = sg.Window('Disney').Layout(window)

    return board