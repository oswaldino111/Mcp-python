################## Biblotecas
import unittest
from unittest.mock import patch, Mock
import os
from dotenv import load_dotenv
from openai import OpenAI  # Substitua por onde sua classe OpenAI está definida
#############################

#############################

class TestOpenAI(unittest.TestCase):

    def setUp(self):
        """
            ### Cria o inicio de cada teste individualmente
        """
        load_dotenv()
        self.openai = OpenAI()
        self.valid_prompt = "Teste de prompt"
        self.mock_response = {
            "choices": [
                {"message": {"content": "Resposta do ChatGPT"}}
            ]
        }

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    @patch('requests.post')
    def teste_enviaPrompt_success(self, mock_post):
        """
            ### Testa o método enviaPrompt com uma resposta válida
        """
        mock_post.return_value = Mock(status_code=200)
        mock_post.return_value.json.return_value = self.mock_response

        result = self.openai.enviaPrompt(self.valid_prompt)

        # Verifica se a requisição foi feita corretamente
        mock_post.assert_called_once_with(
            'https://api.openai.com/v1/chat/completions',
            headers=self.openai.header,
            json={
                "model": "gpt-4o",
                "messages": [{"role": "user", "content": self.valid_prompt}],
                "temperature": 0.7,
                "max_tokens": 16000
            }
        )
        self.assertEqual(result, "Resposta do ChatGPT")

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    @patch('requests.post')
    def teste_enviaPrompt_api_error(self, mock_post):
        """
            ### Testa o método enviaPrompt quando a API retorna um erro
        """
        mock_post.return_value = Mock(status_code=401)
        mock_post.return_value.json.return_value = {"error": "Unauthorized"}

        with self.assertRaises(Exception):
            self.openai.enviaPrompt(self.valid_prompt)


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def teste_retorna_json_correto(self):
        """
            ### Testa o método __retorna_json com uma resposta válida
        """
        mock_retorno = Mock()
        mock_retorno.json.return_value = self.mock_response

        result = self.openai._OpenAI__retorna_json(mock_retorno)
        self.assertEqual(result, "Resposta do ChatGPT")


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def teste_retorna_json_errado(self):
        """
            ### Testa o método __retorna_json com uma resposta inválida
        """
        mock_retorno = Mock()
        mock_retorno.json.return_value = {"choices": []}

        with self.assertRaises(IndexError):
            self.openai._OpenAI__retorna_json(mock_retorno)


    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def teste_header(self):
        """
            ### Testa se o header é inicializado corretamente com a chave da API
        """
        expected_header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
        }
        self.assertEqual(self.openai.header, expected_header)


if __name__ == '__main__':
    unittest.main()