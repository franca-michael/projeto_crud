import requests
from pydantic import BaseModel


class PokemonSchema(BaseModel): # contrato de dados, shcema de dados que quero garantir no meu banco
    name: str
    type: str

    class Config:
        from_attributes = True


def capturar_pokemon(id_pokemon: int)-> PokemonSchema:

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id_pokemon}")
    data = response.json()
    data_types = data['types']
    types_list = []

    for type_info in data_types:
        types_list.append(type_info['type']['name'])

    types = ', '.join(types_list)
    return PokemonSchema(name = data['name'], type=types)
    
    
if  __name__ == '__main__':
    print(capturar_pokemon(1))
    print(capturar_pokemon(3))
    print(capturar_pokemon(15))
    print(capturar_pokemon(25))
    print(capturar_pokemon(52))
        
    



