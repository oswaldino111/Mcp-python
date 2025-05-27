################## Biblotecas
import requests
import os
from dotenv import load_dotenv
#############################
load_dotenv()
#############################

class OpenAI:

    """
        ### Criando a lógica de busca usando a OpenAi como fornecedora
    """

    url = 'https://api.openai.com/v1/chat/completions'

    def __init__(self) -> None:
        self.header = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.environ.get('OPENAI_API_KEY')}"
        }

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def enviaPrompt(self, comando: str):
        """
            ### Envia a solicitação ao chatgpt
            Args:
                comando é a string que desejo solicitar o complemento
            Retorno:
                Resposta retirada do json
        """
        dados = {
         "model": "gpt-4o",
         "messages": [{"role": "user", "content": comando}],
         "temperature": 0.7,
         "max_tokens": 16000
        }
        retorno = requests.post(self.url, headers=self.header, json=dados)
        return self.__retorna_json(retorno)

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def __retorna_json(self, retorno):
        """
            ### Apenas prepara o json de resposta para o usuario
            Args:
                retorno é a resposta recebida pelo chatgpt
            Retorno:
                Apenas a primeira resposta do chat
        """
        return str(retorno.json()["choices"][0]["message"]["content"])
