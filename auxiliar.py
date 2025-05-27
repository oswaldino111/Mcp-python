################## Biblotecas
from server import server
from open_ai import OpenAI
import json
import traceback
#############################


class Auxiliar:
    """
        ### Buscando carros utilizando OpenAi como intermediario
    """

    def __init__(self):
        self.mcp = server
        self.ia = OpenAI()
        self.query = dict()

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################
    def __verifica_minimo_respostas(self):
        """
            ### Função para verificar se o usuario informou pelo menos 3 caracteristicas
        """
        if len(self.query) < 3:
            return None
        else:
            return self.query
            

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def __prompt_para_busca_info(self) -> dict:
        """
            ### A open ai para solicitar parâmetros ausentes.
        """
        respostas = self.__verifica_minimo_respostas()
        if respostas:
            return respostas

        # Monta um prompt para solicitar o parâmetro
        prompt_user = f"""Você está ajudando um usuário a realizar uma busca de veículos. Ele ainda nâo forneceu no minimo 3 informações
        Pergunte ao usuário de forma amigável e clara e simpatica qual é os valores de (marca, ano, modelo, cor, quantidade_portas, propulsao, 
        lugares, cambio). Forneça uma resposta curta porém fluida, e peça apenas os valores cuja as chave ainda não estejam em {self.query.keys()}.
        Retorne apenas a pergunta a ser fornecida ao usuário, sem texto adicional."""

        valor = self.ia.enviaPrompt(comando=prompt_user)

        resposta_usuario = input(valor)

        try:
            self.processar_mensagem(resposta=resposta_usuario)

            #Exemplificar funções recursivas
            return self.__prompt_para_busca_info()

        except:
            print(f"Erro ao processar a resposta: {traceback.format_exc()}")
            ValueError("Não consegui encontrar a caracteristica")

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 25/05/2025
    ################################################ 
    def processar_mensagem(self, resposta: str) -> None:
        """
            ### Processa a primeira mensagem do usuário de acordo com o negocio
            Args:
                resposta é o conteúdo que o usuario enviou
            Retorno:
                None
        """

        prompt_user = f"""Você está ajudando um usuário a realizar uma busca de veículos. Ele enviou uma mensagem com 
        informações sobre qual veiculo ele quer, ele pode dizer sobre (marca, ano, modelo, cor, quantidade_portas, propulsao, lugares, cambio), 
        considerando isso o usuario disse: '{resposta}'.Com base nisso me retorne quais informações voce encontrou em json 
        chave: valor, sem texto adicional."""

        valor = self.ia.enviaPrompt(comando=prompt_user)

        dados = json.loads(valor.replace("```json", "").replace("```", ""))

        for key in dados.keys():
            self.query.update({key: dados[key]})

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 26/05/2025
    ################################################
    def __gera_mensagem_inicial(self, resposta: str):
        """
            ### gera a primeira mensagem de interação com o usuario
            Args:
                resposta é o retorno da solicitação anterior
            Resposta:
                é o que o usuario digitou
        """
        adicional = ''
        if resposta == "não achou":
            adicional = 'O usuario já realizou uma consulta e não encontrou o veiculo que queria.'

        elif resposta == "achou":
            adicional = 'O usuario já realizou uma consulta encontrou o veiculo que queria e quer pesquisar outro.'

        # Monta um prompt para solicitar o parâmetro
        prompt_user = f"""Você está ajudando um usuário a realizar uma busca de veículos. {adicional} Faça uma introdução amigavel para ele!"""

        valor = self.ia.enviaPrompt(comando=prompt_user)

        resposta = input(valor)

        return resposta

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def busca_veiculo(self, resposta: str) -> dict:
        """
            ### Função para realizar a busca de veículos com base nos parâmetros.
        """

        resposta = self.__gera_mensagem_inicial(resposta=resposta)  

        self.processar_mensagem(resposta=resposta)

        self.__prompt_para_busca_info()

        # Retornar a query para a busca
        print(self.query)

        return self.query