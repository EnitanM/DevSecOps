from app import app

def test_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_developer_name():
    client = app.test_client()
    response = client.get('/')
    assert b'Enitan Meduteni' in response.data