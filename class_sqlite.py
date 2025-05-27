################## Biblotecas
import sqlite3
from typing import Any
from sqlite3 import Error
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from abstracoes.sql import SQL
#############################

class SQLITE(SQL):

    database = "sistema_carros.db"

    def __init__(self):
        self.conn = None
        self.cursor = None
        self.engine = None

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def retornar_engine(self):
        """
            "Getter" da engine
        """
        engine = create_engine(f'sqlite:///{self.database}')
        return engine
    
    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def retornar_conexao(self):
        """
            "Getter" da conexão
        """
        return self.conn

    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def criar_conexao(self) -> None:
        """
            ### Cria a conexão com o banco de dados funcriona como um "Setter"
            Args:
                None
            Retorno:
                Conexão SQLite
        """
        self.conn = None
        try:
            conn = sqlite3.connect(self.database)
            print("Conexão com SQLite estabelecida com sucesso")

        except Error as e:
            print(f"Criando conexão: {e}")
            return None
        
        self.conn = conn
        self.cursor = conn.cursor()
    
    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def fechar_conexao(self):
        """
            ### Fecha a conexão e o cursor do sqlite
            Args:
                None
            Retorno:
                None
        """
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()
    
    ################################################
    # Modificado por: Oswaldo Veloso
    # Atualizado em 24/05/2025
    ################################################
    def executar_query(self, sql: str, retorno=False) -> Any:
        """
            ### Executa um string no banco de dados
            Args:
                sql é a string a ser executada
            Retorno:
                Caso retorno verdadeiro o resultado da query
                Caso retorno falso None
        """
        self.criar_conexao()
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            print("Tabela 'users' criada com sucesso")
        except Error as e:
            self.conn.rollback()
            print(f"Erro ao criar tabela: {e}")

        self.fechar_conexao()