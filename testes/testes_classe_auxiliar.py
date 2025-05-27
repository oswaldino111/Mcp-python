################## Biblotecas
import unittest
from unittest.mock import patch, MagicMock
from auxiliar import Auxiliar
#############################

#############################

class TestAuxiliar(unittest.TestCase):

    
    def setUp(self):
        """
            ### Cria o inicio de cada teste individualmente
        """
        self.auxiliar = Auxiliar()
        self.auxiliar.mcp = MagicMock()
        self.auxiliar.ia = MagicMock()
        self.auxiliar.query = {}


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def teste_verifica_minimo_respostas_faltante(self):
        """
            ### Teste da __verifica_minimo_respostas que devera ser no caso 3 e nesse teste continuar.
        """
        self.auxiliar.query = {"marca": "Toyota", "ano": 2020}
        result = self.auxiliar._Auxiliar__verifica_minimo_respostas()
        self.assertIsNone(result, "Não deveria ser none")


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def teste_verifica_minimo_respostas_sucesso(self):
        """
            ### Teste da __verifica_minimo_respostas que devera ser no caso 3 e nesse teste parar.
        """
        self.auxiliar.query = {"marca": "Toyota", "ano": 2020, "modelo": "Corolla"}
        result = self.auxiliar._Auxiliar__verifica_minimo_respostas()
        self.assertEqual(result, self.auxiliar.query, {"marca": "Toyota", "ano": 2020, "modelo": "Corolla"})


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    @patch('builtins.input')
    def teste_prompt_para_busca_info_sufficiente(self, mock_input):
        """
            ### Teste __prompt_para_busca_info .
        """
        self.auxiliar.query = {"marca": "Toyota", "ano": 2020, "modelo": "Corolla"}
        result = self.auxiliar._Auxiliar__prompt_para_busca_info()
        self.assertEqual(result, self.auxiliar.query, "Deverá retornar ")
        mock_input.assert_not_called()
        self.auxiliar.ia.enviaPrompt.assert_not_called()


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    @patch('builtins.input')
    def teste_prompt_para_busca_info_pouco_elemento(self, mock_input):
        """
            ### Teste __prompt_para_busca_info quando não tem 3 informações.
        """
        self.auxiliar.query = {"marca": "toyota"}
        mock_input.return_value = "Do ano 2020 quero um Corolla"
        self.auxiliar.ia.enviaPrompt.return_value = "Por favor, informe mais informações como ano e o modelo do veículo."
        
        # Mock processar_mensagem to update query
        def mock_processar_mensagem(resposta):
            self.auxiliar.query.update({"ano": 2020, "modelo": "corolla"})
        
        with patch.object(self.auxiliar, 'processar_mensagem', mock_processar_mensagem):
            result = self.auxiliar._Auxiliar__prompt_para_busca_info()
        
        self.assertEqual(result, {"marca": "toyota", "ano": 2020, "modelo": "corolla"},
                        "Should return updated query after processing")
        
        self.auxiliar.ia.enviaPrompt.assert_called_once()
        mock_input.assert_called_once()


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    @patch('auxiliar.json.loads')
    def teste_processar_mensagem_sucesso(self, mock_json_loads):
        """
            ###
        """
        resposta = "Quero um fiat que pode ser do ano 2020"
        self.auxiliar.ia.enviaPrompt.return_value = '{"marca": "fiat", "ano": 2020}'
        mock_json_loads.return_value = {"marca": "fiat", "ano": 2020}
        
        self.auxiliar.processar_mensagem(resposta=resposta)
        
        self.assertEqual(self.auxiliar.query, {"marca": "fiat", "ano": 2020}, "Não é um json válido")
        
        self.auxiliar.ia.enviaPrompt.assert_called_once()
        mock_json_loads.assert_called_once_with('{"marca": "fiat", "ano": 2020}')


if __name__ == '__main__':
    unittest.main()