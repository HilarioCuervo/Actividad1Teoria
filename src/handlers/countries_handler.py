import csv
import json


def make_reader():
    ''' Funcion que abre el archivo de paises
        y lo hace recorrible con el reader '''

    file = open('/Users/hilario/Desktop/2do Año/Python/Actividad1Teoria/src/files/countries_of_the_world.csv', 'r', encoding = 'utf-8')
    countries = csv.reader(file, delimiter = ',')

    # Avanza un campo en el archivo para saltear la cabecera
    next(countries)

    return countries


def create_json(worst_infant_mortality):
    ''' Funcion que crea un archivo json con los datos a mostrar'''

    file = open('/Users/hilario/Desktop/2do Año/Python/Actividad1Teoria/src/files/worst_infant_mortality.json', 'w')

    data = {}

    for country in worst_infant_mortality:
        data[worst_infant_mortality.index(country) + 1] = country

    # Creo el json con el dict creado a partir de la lista recibida como parametro
    json.dump(data, file, indent = 4)


def get_data():
    ''' Funcion encargada de filtrar los datos a mostrar de los paises '''

    countries = make_reader()

    # Lista auxiliar para unificar campos y facilitar el filtrado
    aux_countries = [(country[0], country[1].replace(' ', ''), country[7].replace(',', '.')) for country in countries]

    # Creo lista de tuplas con los datos a usar y la ordeno por el criterio del campo 1 (mort. infantil)
    south_america_countries = [(country[0], float(country[2])) for country in aux_countries if (country[1] == 'LATINAMER.&CARIB')]
    south_america_countries = sorted(south_america_countries, key = lambda country: country[1], reverse = True)

    # Me quedo con los primeros 7
    worst_infant_mortality = [south_america_countries[index] for index in range(0,7)]
    
    create_json(worst_infant_mortality)

    return worst_infant_mortality