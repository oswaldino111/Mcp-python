################## Biblotecas
from mcp.server.fastmcp import FastMCP
from class_carro import CarroCrm

############################## Cria o servidor MCP
server = FastMCP(
    "Servidor de Carros SQLite"
)

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 24/05/2025
################################################
@server.tool()
def buscar_carros(filtros: dict)-> dict:
    """
        ### Busca carros com base nos filtros recebidos 
    Args:
        filtros é o Json de filtros
    Retorno:
        Uma lista com todos os carros encontrados
    """
    carro = CarroCrm()

    carros = carro.buscar_carro(filtros=filtros)

    return {
        "total_carros": len(carros),
        "carros": carros
    }

############################## Inicia o servidor MCP
if __name__ == "__main__":
    print("Iniciado ...")
    server.run(transport="streamable-http")