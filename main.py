################## Biblotecas
from mcp.client.streamable_http import streamablehttp_client
from mcp import ClientSession
from auxiliar import Auxiliar
import asyncio
import json

#############################
    ### O uso da bibloteca e metodos voce encontr em:
    # https://pypi.org/project/mcp/

#############################

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 25/05/2025
################################################
async def main(argumentos: dict) -> None:
    """
        ### Função main para busca no mcp
        Args:
            argumentos é o json de entrada com os filtros desejados
        Retorno:
            None

    """
    async with streamablehttp_client("http://localhost:8000/mcp") as (
        read_stream,
        write_stream,
        _,
    ):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()

            # Chamada da ferramenta com dicionário de argumentos
            tool_result = await session.call_tool("buscar_carros", arguments={"filtros": argumentos})

            return tool_result

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 25/05/2025
################################################
def main_dados(resposta: str) -> dict:
    """
        ### Função main de busca no auxiliar
        Args:
            None
        Retorno:
            Json com os filtros para serem enviados ao mcp
    """
    
    # Instanciar a ferramenta
    tool = Auxiliar()

    result = tool.busca_veiculo(resposta=resposta)
    print("Resultado da busca:", result)

    return result

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 27/05/2025
################################################
def mostrar_informacoes(carro):
    """
        ### Função para 
    """
    print(f"Marca: {carro['marca']} ")
    print(f"Ano: {carro['ano']} ")
    print(f"Modelo: {carro['modelo']} ")
    print(f"Cor: {carro['cor']} ")
    print(f"Quilometragem: {carro['quilometragem']} ")
    print("\n\n")


# Iniciando
if __name__ == "__main__":

    ultima_resposta = None

    while True:
        argumentos = main_dados(resposta=ultima_resposta)

        retorno = asyncio.run(main(argumentos))
        dados = json.loads(retorno.content[0].text)

        if dados["total_carros"] < 1:
            print("Infelizmente não tenho esse carro!")
            ultima_resposta = "não achou"
        
        else:
            for carro in dados["carros"]:

                mostrar_informacoes(carro)

            ultima_resposta = "achou"
