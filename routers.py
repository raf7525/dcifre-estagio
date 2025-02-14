from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud as crud_empresa
from routers import Empresa, EmpresaCreate
from database import SessionLocal
from your_router import router 

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/empresas/", response_model=Empresa)
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud_empresa.get_empresa_by_cnpj(db, cnpj=empresa.cnpj)
    if db_empresa:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    return crud_empresa.create_empresa(db=db, empresa=empresa)

