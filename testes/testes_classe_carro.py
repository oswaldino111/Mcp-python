################## Biblotecas
import unittest
from unittest.mock import MagicMock, patch
from class_sqlite import SQLITE
from sqlalchemy.orm import Session
from sqlalchemy import select
from models.models import Carro
from class_carro import CarroCrm
#############################

#############################
class TestCarroCrm(unittest.TestCase):


    def setUp(self):
        """
            ### Cria o inicio de cada teste individualmente
        """
        self.carro_crm = CarroCrm()
        self.carro_crm.db = MagicMock(spec=SQLITE)
        self.session_mock = MagicMock(spec=Session)
        self.engine_mock = MagicMock()
        self.carro_crm.db.retornar_engine.return_value = self.engine_mock
        self.session_mock.__enter__.return_value = self.session_mock
        self.engine_mock.__enter__.return_value = self.engine_mock


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 26/05/2025
    ################################################
    def teste_get_filtros_validos_filtro_valido(self):
        """
            ### Testa se retorna o campo correto para um filtro válido
        """
        result = self.carro_crm.get_filtros_validos('marca')
        self.assertEqual(result, Carro.marca)

        result = self.carro_crm.get_filtros_validos('ano')
        self.assertEqual(result, Carro.ano)


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 26/05/2025
    ################################################
    def teste_get_filtros_validos_filtro_invalido(self):
        """
            ### Testa se retorna None para um filtro inválido
        """
        result = self.carro_crm.get_filtros_validos('invalido')
        self.assertIsNone(result)


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 26/05/2025
    ################################################
    def teste_buscar_carro_filtros_validos(self):
        """
            ### Mock do resultado da consulta
        """
        carro_mock = MagicMock()
        carro_mock.to_dict.return_value = {'id': 1, 'marca': 'toyota', 'modelo': 'hatch', 'ano': 2020}
        self.session_mock.execute.return_value.scalars.return_value.all.return_value = [carro_mock]

        filtros = {'marca': 'toyota', 'modelo': 'hatch'}

        result = self.carro_crm.buscar_carro(filtros)

        print(result)

        self.session_mock.execute.assert_called_once()



if __name__ == '__main__':
    unittest.main()