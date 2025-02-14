from sqlalchemy import Column, Integer, String
from database import Base

class Empresa(Base):
    __tablename__ = "empresas"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(20), unique=True, nullable=False)
    endereco = Column(String(200), nullable=False)
    email = Column(String(100), nullable=False)
    telefone = Column(String(20), nullable=False)

    def __repr__(self):
        return f"<Empresa(nome='{self.nome}', cnpj='{self.cnpj}')>"
