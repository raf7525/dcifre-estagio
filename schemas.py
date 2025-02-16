# schemas.py
from pydantic import BaseModel, EmailStr

# Schemas para Empresa
class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class Config:
        from_attributes = True  # Para converter objetos ORM

# Schemas para ObrigacaoAcessoria
class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str  # "mensal", "trimestral", "anual"

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    empresa_id: int

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int
    empresa_id: int

    class Config:
        from_attributes = True
