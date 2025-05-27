################## Biblotecas
from class_sqlite import SQLITE
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.models import Carro
#############################

################## Classe de manipulação dos carros
class CarroCrm:
    """
        ### Classe responsável por tratar os carros no sistema
        Obs:
            Cruds a serem incluídos aqui
    """

    locadora = "Locadora do Oswaldo"
    intermediadora = "C2S"

    def __init__(self) -> None:
        self.db = SQLITE()

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def get_filtros_validos(self, escolha: str):
        """
            ### Valida se o filtro solicitado existe
            Args:
                escolha é o filtro solicitado
            Retorno:
                A coluna de carros correspondente a o filtro
        """
        try:
            valid_filters = {
                'marca': Carro.marca,
                'ano': Carro.ano,
                'modelo': Carro.modelo,
                'cor': Carro.cor,
                'quilometragem': Carro.quilometragem,
                'quantidade_portas': Carro.quantidade_portas,
                'chassi': Carro.chassi,
                'propulsao': Carro.propulsao,
                'lugares': Carro.lugares,
                'cambio': Carro.cambio
            }

            return valid_filters[escolha]
        except:
            return None

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def buscar_carro(self, filtros: dict) -> list:
        """
            ### Busca o carro considerando todos os filtros enviados existentes em get_filtros_validos
            Args:
                filtros é o dicionário de filtros
            Retorno:
                Lista com os resultados encontrados
        """
        engine = self.db.retornar_engine()
        with Session(engine) as session:
            stmt = select(Carro)

            condicoes = list()

            for key, value in filtros.items():
                filtro = self.get_filtros_validos(key)
                if filtro is not None:
                    condicoes.append(filtro == value)
        
        stmt = stmt.where(*condicoes)
        result = session.execute(stmt).scalars().all()
        carros_dict = [carro.to_dict() for carro in result]
        return carros_dict
        