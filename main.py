from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine
from models import Base


Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/empresas/", response_model=schemas.Empresa)
def create_empresa_endpoint(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa_by_cnpj(db, cnpj=empresa.cnpj)
    if db_empresa:
        raise HTTPException(status_code=400, detail="CNPJ já cadastrado")
    return crud.create_empresa(db=db, empresa=empresa)

@app.get("/empresas/", response_model=list[schemas.Empresa])
def read_empresas(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_empresas(db, skip=skip, limit=limit)

@app.get("/empresas/{empresa_id}", response_model=schemas.Empresa)
def read_empresa(empresa_id: int, db: Session = Depends(get_db)):
    db_empresa = crud.get_empresa(db, empresa_id)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.put("/empresas/{empresa_id}", response_model=schemas.Empresa)
def update_empresa_endpoint(empresa_id: int, empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    db_empresa = crud.update_empresa(db, empresa_id, empresa)
    if db_empresa is None:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return db_empresa

@app.delete("/empresas/{empresa_id}")
def delete_empresa_endpoint(empresa_id: int, db: Session = Depends(get_db)):
    if not crud.delete_empresa(db, empresa_id):
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return {"detail": "Empresa deletada com sucesso"}


@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoria)
def create_obrigacao_endpoint(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    
    empresa = crud.get_empresa(db, obrigacao.empresa_id)
    if not empresa:
        raise HTTPException(status_code=404, detail="Empresa não encontrada")
    return crud.create_obrigacao(db=db, obrigacao=obrigacao)

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoria])
def read_obrigacoes(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_obrigacoes(db, skip=skip, limit=limit)

@app.get("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def read_obrigacao(obrigacao_id: int, db: Session = Depends(get_db)):
    db_obrigacao = crud.get_obrigacao(db, obrigacao_id)
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return db_obrigacao

@app.put("/obrigacoes/{obrigacao_id}", response_model=schemas.ObrigacaoAcessoria)
def update_obrigacao_endpoint(obrigacao_id: int, obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    db_obrigacao = crud.update_obrigacao(db, obrigacao_id, obrigacao)
    if not db_obrigacao:
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return db_obrigacao

@app.delete("/obrigacoes/{obrigacao_id}")
def delete_obrigacao_endpoint(obrigacao_id: int, db: Session = Depends(get_db)):
    if not crud.delete_obrigacao(db, obrigacao_id):
        raise HTTPException(status_code=404, detail="Obrigação acessória não encontrada")
    return {"detail": "Obrigação acessória deletada com sucesso"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
