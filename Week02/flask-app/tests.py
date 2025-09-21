from app import app


def test_team_number():
    client = app.test_client()
    response = client.get('/')

    assert response.status_code == 200
    assert response.data == b'This is Team 1\'s Flask app!'