import requests
from loguru import logger
from schema import PokemonSchame
from models import Pokemon
from db import SessionLocal, engine, Base
from decorator_log import log_decorator

Base.metadata.create_all(bind=engine)

@log_decorator
def pegar_pokemon(id: int) -> PokemonSchame:

    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}")        # select na API com requests.
    data = response.json()      # Converte nosso resultado de json para um dicionário Python.
    data_types = data['types']      # Entrando e filtrando em nosso dicionário para pegarmos  tudo aquilo com o nome de 'types'.
    types_list = []     # Criando uma lista vazia.
    for type_info in data_types:        # Criando um loop FOR para adicionar os valores de data_types na varíavel de type_info
        types_list.append(type_info['type']['name'])        # Adicionando os valores na lista vazia, e específicando as chaves/valor que queremos adicionar.
    types = ', '.join(types_list)       # Aqui ele transforma nossas chaves/valor em string e separa eles por uma ","(vírgula).
    add = PokemonSchame(name=data['name'], type=types)   # Adicionando direto a nossa class. (futuro banco de dados).
    return add


@log_decorator
def add_pokemon_data(pokemon_schema: PokemonSchame) -> Pokemon:

    with SessionLocal() as db:      # Abrindo uma sessão e conectando com o nosso banco de dados.
        db_pokemon = Pokemon(name=pokemon_schema.name, type=pokemon_schema.type)    # Recebe de pokemon_schema valores de name e type, e adiciona na nossa classe da tabela do banco de dados (Pokemon).
        db.add(db_pokemon)      # Com a conexão com o banco de dados, adicionado esse valor a tabela.
        db.commit()         # Commit para finalizar e salvar as aplicações no banco e dados.


## fazer uma query basica com o sqlalchemy.

## 301