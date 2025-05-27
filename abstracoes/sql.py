################## Biblotecas
from abc import ABC, abstractmethod
from typing import Any
import pandas as pd
#############################

class SQL(ABC):
    """
        ### Abstração dos metodos obrigatorios em todos os bancos Sql
    """

    @abstractmethod
    def retornar_engine(self) -> Any:
        pass

    @abstractmethod
    def retornar_conexao(self) -> Any:
        pass

    @abstractmethod
    def criar_conexao(self) -> Any:
        pass

    @abstractmethod
    def fechar_conexao(self) -> None:
        pass

    @abstractmethod
    def executar_query(self, query: str, retorno=False) -> Any:
        pass