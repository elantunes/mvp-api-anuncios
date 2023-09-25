from sqlalchemy import Column, DateTime, Float, Integer, String, Table
from sqlalchemy.sql import func

from model import Base


class Anuncio(Base):
    __table__ = Table('anuncio', Base.metadata,
        Column('id', Integer, primary_key=True),
        Column('nome_veiculo', String, nullable=False),
        Column('valor_diaria', Float, nullable=False),
        Column('data_inclusao', DateTime, server_default=func.now()),
        sqlite_autoincrement=True)

    def __init__(
            self, id: int,
            nome_veiculo: str,
            valor_diaria: float):
        """
        Instancia um Anúncio

        Arguments:
            id: ID do Anúncio
            nome: Nome do Veículo
            valor_diaria: Valor da Diária
        """
        self.id = id
        self.nome_veiculo = nome_veiculo
        self.valor_diaria = valor_diaria
