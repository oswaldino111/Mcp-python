################## Biblotecas
from faker import Faker
import random
import pandas as pd
from class_sqlite import SQLITE
#############################
fake = Faker()
#############################


json_dados = {
    "marca" : ["porche", "bmw", "audi", "fiat", "chevrolet", "hyundai", "bid", "toyota", "volkswagen", "honda"],
    "modelo" : ["sedan", "hatch", "suv", "picape", "esportivo", "minivan", "crossover"],
    "propulsao" : ["combustão", "eletrico", "hibrido"],
    "cambio": ["automatico 6 marchas", "automatico 8 marchas", "manual 5 marchas", "manual 6 marchas"],
    "cores": ["azul", "branco", "preto", "amarelo", "cinza", "vermelho"]
}

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 24/05/2025
################################################
def cria_carro() -> dict:
    """
        ### Monta o json de carro usando presets e faker
    """
    return {
        "marca" : random.choice(json_dados["marca"]),
        "ano" : fake.random_int(min=2000, max=2025),
        "modelo" : random.choice(json_dados["modelo"]),
        "cor" : random.choice(json_dados["cores"]),
        "quilometragem" : fake.random_int(min=0, max=100000),
        "quantidade_portas" : fake.random_int(min=2, max=6),
        "chassi" : str(fake.license_plate()).lower(),
        "propulsao" : random.choice(json_dados["propulsao"]),
        "lugares" : fake.random_int(min=2, max=7),
        "cambio": random.choice(json_dados["cambio"]),
    }

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 24/05/2025
################################################
def salva_carros(df_carros: pd.DataFrame) -> None:
    """
        ### Utilizando a conexao do sqlite insere o dataframe
        Args:
            df_carros é o dataframe final de carros
        Retorno:
            None
    """
    database = SQLITE()
    database.criar_conexao()
    conn = database.retornar_conexao()
    df_carros["id"] = df_carros.index
    df_carros.to_sql('carros', index=False, con=conn, if_exists='replace')
    database.fechar_conexao()

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 24/05/2025
################################################
def cria_dataframe(lista_json: dict) -> pd.DataFrame:
    """
        ### Cria o dataframe pandas
        Args:
            lista_json é uma lista de json criado com dados de carros
        Retorno:
            Dataframe de carros em pandas
    """
    return pd.DataFrame(lista_json)

################################################
# Modificado por: Oswaldo Veloso
# Atualizado em 24/05/2025
################################################
def main():
    """
        ### Inicia o fluxo de criação de dados
    """
    list_cars = list()
    for _ in range(900):
        list_cars.append(cria_carro())
    
    dados = cria_dataframe(list_cars)
    salva_carros(dados)


if __name__ == "__main__":
    main()