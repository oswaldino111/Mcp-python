################## Biblotecas
import unittest
from unittest.mock import MagicMock
from class_sqlite import SQLITE
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



if __name__ == '__main__':
    unittest.main()