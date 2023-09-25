from pydantic import BaseModel
from typing import List

from model import Anuncio


class AnuncioViewSchema(BaseModel):
    """ Define como deve ser a estrutura do Anúncio retornado após uma requisição
    """
    id: int
    nome_veiculo: str
    valor_diaria: float


class ListaAnunciosSchema(BaseModel):
    """ Define como uma listagem de Anúncios será retornada.
    """
    alugueis:List[AnuncioViewSchema]


# Defs


def show_anuncios(anuncios: List[Anuncio]):
    """ Retorna uma representação de uma lista de Anúncios seguindo o schema definido em
        ListaAnunciosSchema.
    """
    result = []
    for anuncio in anuncios:
        result.append({
            'id': anuncio.id,
            'nome_veiculo': anuncio.nome_veiculo,
            'valor_diaria': anuncio.valor_diaria
        })

    return {'anuncios': result}
