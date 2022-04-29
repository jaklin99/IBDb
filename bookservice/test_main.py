from starlette.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_get_books():
    response = client.get("/books")
    assert response.status_code == 200


def test_get_book_by_id():
    response = client.get("/books/{id}")
    assert response.status_code == 200


def test_create_item():
    response = client.post(
        "/items/",
        headers={"X-Token": "coneofsilence"},
        json={"id": "foobar", "title": "Foo Bar", "description": "The Foo Barters"},
    )
    assert response.status_code == 200
    assert response.json() == {
        "id": "foobar",
        "title": "Foo Bar",
        "description": "The Foo Barters",
    }

    assert response.status_code == 400
    assert response.json() == {"detail": "Item already exists"}
