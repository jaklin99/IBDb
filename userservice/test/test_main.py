from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_read_users():
    response = client.get("/users", headers={"X-Token": "coneofsilence"})
    assert response.status_code == 200
    assert response.json() == {
        "id": "foo",
        "username": "Foo",
        "email": "hero@gmail.com",
    }


def test_create_user():
    response = client.post(
        "/users/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "username": "Foo",
              "email": "hero@gmail.com"}
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "username": "Foo",
        "email": "hero@gmail.com"
    }


def test_create_existing_user():
    response = client.post(
        "/users/",
        headers={"X-Token": "coneofsilence"},
        json={
            "id": "foo",
            "username": "Foo",
            "email": "hero@gmail.com"
        },
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "User already exists"}
