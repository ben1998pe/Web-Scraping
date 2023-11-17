import requests
import pandas as pd

# URL de la API de Pokémon para el Pokémon "Ditto"
url = 'https://pokeapi.co/api/v2/pokemon/ditto'

# Realiza una solicitud GET a la API
response = requests.get(url)

# Verifica si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Convierte la respuesta JSON a un diccionario de Python
    pokemon_data = response.json()

    # Crea un DataFrame de pandas con la información del Pokémon
    data = {
        'Nombre del Pokémon': [pokemon_data['name']],
        'Altura': [pokemon_data['height']],
        'Peso': [pokemon_data['weight']]
    }

    abilities = []
    for ability in pokemon_data['abilities']:
        abilities.append({
            'Nombre': ability['ability']['name'],
            'Escondida': ability['is_hidden'],
            'Ranura': ability['slot']
        })

    data['Habilidades'] = [abilities]

    types = []
    for tipo in pokemon_data['types']:
        types.append({
            'Nombre': tipo['type']['name'],
            'Ranura': tipo['slot']
        })

    data['Tipos'] = [types]

    moves = []
    for move in pokemon_data['moves']:
        move_details = []
        for group_detail in move['version_group_details']:
            move_details.append({
                'Nombre': move['move']['name'],
                'Nivel aprendido': group_detail['level_learned_at'],
                'Método de aprendizaje': group_detail['move_learn_method']['name'],
                'Grupo de versión': group_detail['version_group']['name']
            })
        moves.extend(move_details)

    data['Movimientos'] = [moves]

    # Crea un DataFrame de pandas con los datos
    df = pd.DataFrame(data)

    # Guarda el DataFrame en un archivo Excel
    df.to_excel('pokemon_ditto_info.xlsx', index=False)

    print('Información del Pokémon guardada en "pokemon_ditto_info.xlsx"')

else:
    print('Error al realizar la solicitud:', response.status_code)
