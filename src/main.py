import time
import random
from controller import pegar_pokemon, add_pokemon_data
from models import Pokemon
from db import Base

def main():
    while True:
        id = random.randint(1, 350)      # ID de pokemon aleatório entre 1 e 350.
        pokemon_schema =  pegar_pokemon(id)     # Extraindo Pokemon da API pelo ID gerado aleatóriamente.
        if pokemon_schema:
            print(f'Adicionando {pokemon_schema.name} ao banco de dados')   # If com o objetivo de: se caso tudo ocorrer bem, irá nos mostrar essa mensagem.
            add_pokemon_data(pokemon_schema)    # Função que recebe esse Pokemon e adiciona ao banco de dados.  
        else:
            print(f"Não foi possível obter dados para o Pokemon com ID {id}")       # Se ocorrer algum erro no caminho.
        time.sleep(5)      # Time para cada 10 segundos, gerar um novo ID e fazer tudo denovo.

if __name__ == "__main__":
    main()




## Criar um if ou o que for melhor para garantir que os mesmos Pokémon não entrem no banco de dados