import csv
import json


def make_reader():
    ''' Funcion que abre el archivo de peliculas de
        disney y lo hace recorrible con el reader ''' 

    file = open('/Users/hilario/Desktop/2do Año/Python/Actividad1Teoria/src/files/disney_movies.csv', 'r', encoding = 'utf-8')
    disney_movies = csv.reader(file, delimiter = ',')

    # Avanza un campo en el archivo para saltear la cabecera
    next(disney_movies)

    return disney_movies


def create_json(best_gross):
    ''' Funcion que crea un archivo json con los datos a mostrar'''

    file = open('/Users/hilario/Desktop/2do Año/Python/Actividad1Teoria/src/files/best_gross.json', 'w')

    data = {}

    for movie in best_gross:
        data[best_gross.index(movie) + 1] = movie

    # Creo el json con el dict creado a partir de la lista recibida como parametro
    json.dump(data, file, indent = 4)
    


def get_data():
    ''' Funcion encargada de filtrar los datos a mostrar de las peliculas '''
    
    disney_movies = make_reader()

    # Creo lista de tuplas con los datos a usar y la ordeno por el criterio del campo 1 (taquilla)
    total_gross = [(movie[0], int(movie[4])) for movie in disney_movies]
    total_gross = sorted(total_gross, key = lambda movie: movie[1], reverse = True)
    
    # Me quedo con los primeros 10
    best_gross = [total_gross[index] for index in range(0,10)]

    create_json(best_gross)

    return best_gross
