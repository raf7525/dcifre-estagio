# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    
    assert response.status_code == 404

def test_create_empresa():
    payload = {
        "nome": "Empresa Teste",
        "cnpj": "98765432000188",
        "endereco": "Rua Teste, 456",
        "email": "teste@empresa.com",
        "telefone": "(21) 9876-5432"
    }
    response = client.post("/empresas/", json=payload)
    
    assert response.status_code == 200
    data = response.json()
    assert data["cnpj"] == payload["cnpj"]
