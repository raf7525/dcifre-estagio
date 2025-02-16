# models.py
from sqlalchemy import Column, Integer, String, ForeignKey
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

class ObrigacaoAcessoria(Base):
    __tablename__ = "obrigacoes_acessorias"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    periodicidade = Column(String(20), nullable=False)  # valores esperados: "mensal", "trimestral", "anual"
    empresa_id = Column(Integer, ForeignKey("empresas.id"), nullable=False)

    def __repr__(self):
        return f"<ObrigacaoAcessoria(nome='{self.nome}', periodicidade='{self.periodicidade}', empresa_id={self.empresa_id})>"
