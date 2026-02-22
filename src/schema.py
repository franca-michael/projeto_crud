from pydantic import BaseModel

class PokemonSchema(BaseModel): # contrato de dados, shcema de dados que quero garantir no meu banco
    name: str
    type: str

    class Config:
        from_attributes = True
