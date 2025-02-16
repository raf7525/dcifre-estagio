# crud.py
from sqlalchemy.orm import Session
from models import Empresa, ObrigacaoAcessoria
from schemas import EmpresaCreate, ObrigacaoAcessoriaCreate

# Funções para Empresa
def get_empresa_by_cnpj(db: Session, cnpj: str):
    return db.query(Empresa).filter(Empresa.cnpj == cnpj).first()

def create_empresa(db: Session, empresa: EmpresaCreate):
    db_empresa = Empresa(**empresa.dict())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_empresas(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Empresa).offset(skip).limit(limit).all()

def get_empresa(db: Session, empresa_id: int):
    return db.query(Empresa).filter(Empresa.id == empresa_id).first()

def update_empresa(db: Session, empresa_id: int, empresa: EmpresaCreate):
    db_empresa = get_empresa(db, empresa_id)
    if db_empresa:
        for key, value in empresa.dict().items():
            setattr(db_empresa, key, value)
        db.commit()
        db.refresh(db_empresa)
    return db_empresa

def delete_empresa(db: Session, empresa_id: int):
    db_empresa = get_empresa(db, empresa_id)
    if db_empresa:
        db.delete(db_empresa)
        db.commit()
        return True
    return False

# Funções para ObrigacaoAcessoria
def create_obrigacao(db: Session, obrigacao: ObrigacaoAcessoriaCreate):
    db_obrigacao = ObrigacaoAcessoria(**obrigacao.dict())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def get_obrigacoes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(ObrigacaoAcessoria).offset(skip).limit(limit).all()

def get_obrigacao(db: Session, obrigacao_id: int):
    return db.query(ObrigacaoAcessoria).filter(ObrigacaoAcessoria.id == obrigacao_id).first()

def update_obrigacao(db: Session, obrigacao_id: int, obrigacao: ObrigacaoAcessoriaCreate):
    db_obrigacao = get_obrigacao(db, obrigacao_id)
    if db_obrigacao:
        for key, value in obrigacao.dict().items():
            setattr(db_obrigacao, key, value)
        db.commit()
        db.refresh(db_obrigacao)
    return db_obrigacao

def delete_obrigacao(db: Session, obrigacao_id: int):
    db_obrigacao = get_obrigacao(db, obrigacao_id)
    if db_obrigacao:
        db.delete(db_obrigacao)
        db.commit()
        return True
    return False
