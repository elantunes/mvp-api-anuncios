from pydantic import BaseModel
from typing import List

from model import Anuncio


class AnunciosPostSchema(BaseModel): 
    """ Define como um novo Anúncio a ser inserido deve ser representado.
    """
    anuncios: str    


class AnuncioViewSchema(BaseModel):
    """ Define como deve ser a estrutura do Anúncio retornado após uma requisição
    """
    id: int
    id_veiculo: int
    nome_veiculo: str
    valor_diaria: float


class ListaAnunciosSchema(BaseModel):
    """ Define como uma listagem de Anúncios será retornada.
    """
    anuncios:List[AnuncioViewSchema]


# Defs


def show_anuncios(anuncios: List[Anuncio]):
    """ Retorna uma representação de uma lista de Anúncios seguindo o schema definido em
        ListaAnunciosSchema.
    """
    result = []
    for anuncio in anuncios:
        result.append({
            'id': anuncio.id,
            'id_veiculo': anuncio.id_veiculo,
            'modelo': anuncio.modelo,
            'valor_diaria': anuncio.valor_diaria
        })

    return {'anuncios': result}
