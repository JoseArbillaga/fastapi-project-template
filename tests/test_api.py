from fastapi.testclient import TestClient
from proyecto_api import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "Bienvenido" in r.json().get("message", "")


def test_crud_item():
    # create
    payload = {"name": "Prueba", "description": "desc", "price": 9.99}
    r = client.post("/items", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["id"] == 1
    assert data["name"] == payload["name"]

    # list
    r = client.get("/items")
    assert r.status_code == 200
    lst = r.json()
    assert isinstance(lst, list) and len(lst) >= 1

    # get
    r = client.get("/items/1")
    assert r.status_code == 200

    # update
    update = {"name":"Prueba2","description":"n","price":10.0}
    r = client.put("/items/1", json=update)
    assert r.status_code == 200
    assert r.json()["name"] == "Prueba2"

    # delete
    r = client.delete("/items/1")
    assert r.status_code == 204

    r = client.get("/items/1")
    assert r.status_code == 404
