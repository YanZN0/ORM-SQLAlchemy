import time
import random
from loguru import logger
from controller import pegar_pokemon, add_pokemon_data
from models import Pokemon
from db import SessionLocal
from decorator_log import log_decorator


def main():
    while True:
        id = random.randint(1, 350)   # ID de pokemon aleatório entre 1 e 350.
        pokemon_schema =  pegar_pokemon(id)     # Extraindo Pokemon da API pelo ID gerado aleatóriamente.
        if pokemon_schema:
            logger.info(f'Adicionando {pokemon_schema.name} ao banco de dados')   # If com o objetivo de: se caso tudo ocorrer bem, irá nos mostrar essa mensagem.
            with SessionLocal() as session:     # Abrindo uma sessão para fazer queries dentro do banco (Abrindo e fechando automaticamente com o with).
                verification_name = session.query(Pokemon).filter_by(name=pokemon_schema.name).first()  # Fazendo verificação se o Pokémon ja existe no banco de dados.
                if verification_name:       # Se o nome existir, nôs informa um erro e tenta com outro ID Pokémon.
                    logger.exception(f'O Pokémon {pokemon_schema.name} Já está no banco de dados, tente com outro Pokémon...')
                    continue   # Objetivo de todos esses IF é para verificar se o nome do pokémon está na tabela, e se caso estiver não adiciona-lo.
                else:
                    add_pokemon_data(pokemon_schema)    # Função que recebe esse Pokemon e adiciona ao banco de dados.           
        else:
            logger.exception(f"Não foi possível obter dados para o Pokemon com ID {id}")       # Se ocorrer algum erro no caminho.
        time.sleep(5)      # Time para cada 5 segundos, gerar um novo ID e fazer tudo denovo.

if __name__ == "__main__":
    main()




## Criar um if ou o que for melhor para garantir que os mesmos Pokémon não entrem no banco de dados