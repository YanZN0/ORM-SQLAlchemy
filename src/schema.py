# View: Validação de dados. (Onde validamos os dados que entrarão no nosso banco para ter mais confiabilidade e validação.)

from pydantic import BaseModel

class PokemonSchame(BaseModel):
    name: str       # o Pydantic que vai garantir que os dados entraram  nessa coluna sejam str.
    type: str       # o Pydantic que vai garantir que os dados entraram  nessa coluna sejam str.

    class Config:
        orm_mode = True