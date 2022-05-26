# test_database.py
SQLALCHEMY_DATABASE_URL = "postgresql://test-fastapi:password@db/test-fastapi-test"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

def test_post_items():

    # We grab another session to check
    # if the items are created
    db = override_get_db()
    client = TestClient(app)

    client.post("/items/", json={"title": "Item 1"})

    client.post("/items/", json={"title": "Item 2"})

    items = crud.get_items(db)
    assert len(items) == 2