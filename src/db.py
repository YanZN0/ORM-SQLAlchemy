# Aqui é onde fazemos conexão com o nosso banco de dados.

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker     # ORM para fazermos as transformações do código em Python para um código estruturado SQL.

SQLALCHEMY_DATABASE_URL = "sqlite:///./database_pokemon.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)     # Fazendo conexão com o banco
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)     # A varíavel SessionLocal agora é responsavel para Sessões e Conexões, com ela nos conectamos e falamos com o nosso banco.
Base = declarative_base()       # Base tem como objetivo principal fazer o ORM das tabelas criadas por código Python (classes).
