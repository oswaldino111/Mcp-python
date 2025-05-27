################## Biblotecas
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import Column, Integer, String

#############################
class Base(DeclarativeBase):
    pass

################## Classe do ORM de carros
class Carro(Base):
    __tablename__ = "carros"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String)
    ano = Column(Integer)
    modelo = Column(String)
    cor = Column(String)
    quilometragem = Column(Integer)
    quantidade_portas = Column(Integer)
    chassi = Column(String)
    propulsao = Column(String)
    lugares = Column(Integer)
    cambio = Column(String)

    def to_dict(self):
        """
            ### Transforma o modelo em json para processamento
        """
        return {
            "id": self.id,
            "marca": self.marca,
            "ano": self.ano,
            "modelo": self.modelo,
            "cor": self.cor,
            "quilometragem": self.quilometragem,
            "quantidade_portas": self.quantidade_portas,
            "chassi": self.chassi,
            "propulsao": self.propulsao,
            "lugares": self.lugares,
            "cambio": self.cambio,
        }
