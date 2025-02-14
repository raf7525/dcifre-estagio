from sqlalchemy.orm import Session
from models import Empresa
from schemas import EmpresaCreate

def get_empresa_by_cnpj(db: Session, cnpj: str):
    return db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

def create_empresa(db: Session, empresa: EmpresaCreate):
    db_empresa = Empresa(
        nome=empresa.nome,
        cnpj=empresa.cnpj,
        endereco=empresa.endereco,
        email=empresa.email,
        telefone=empresa.telefone,
    )
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa
