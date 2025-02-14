from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine
from models import Empresa  


from database import Base
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

@app.get("/")
def read_root():
    return {"message": "API está rodando!"}