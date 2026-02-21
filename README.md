# 🚀 Consumo de API com Validação de Dados (Pydantic)

Este repositório contém um estudo prático de **Engenharia de Dados** e **Backend em Python**, focado no consumo de APIs REST e na garantia da qualidade dos dados através de contratos de dados (Schemas).

## 🧠 Conceitos Aplicados

Neste projeto, explorei pilares fundamentais para o desenvolvimento de pipelines de dados modernos:

1.  **Consumo de APIs REST**: Utilização da biblioteca `requests` para realizar requisições HTTP e manipular respostas em formato JSON.
2.  **Validação com Pydantic**: Implementação de um **Schema** utilizando `BaseModel`. Isso garante que, se a API mudar a estrutura do dado, o erro seja capturado imediatamente na entrada, evitando "lixo" no restante do processamento.
3.  **Data Transformation**: Lógica para extração e formatação de dados aninhados (mapeamento da lista de tipos do Pokémon para uma string única).
4.  **Tipagem Estática (Type Hinting)**: Uso de dicas de tipo para melhorar a legibilidade e facilitar a manutenção do código.
5.  **Configuração de Atributos**: Uso do `from_attributes = True` no Pydantic, preparando o modelo para integração futura com ORMs (como SQLAlchemy).

## 🛠️ Tecnologias e Ferramentas

* **Python 3.12+**
* **Pydantic**: Para modelagem e validação rigorosa de dados.
* **Requests**: Para comunicação com a PokeAPI.
* **Poetry**: Para gerenciamento de dependências e ambientes virtuais.

## 📋 Estrutura do Contrato de Dados

O uso do Pydantic permite definir exatamente o que esperamos da API:

```python
from pydantic import BaseModel

class PokemonSchema(BaseModel):
    name: str
    type: str

    class Config:
        from_attributes = True
```

