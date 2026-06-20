def test_get_books(client):
    response = client.get("/books")
    assert response.status_code == 200