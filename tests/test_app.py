from app.main import app

client = app.test_client()


def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.get_json() == {"status": "ok"}


def test_add_todo():
    resp = client.post("/todos", json={"title": "learn ci"})
    assert resp.status_code == 201
    assert resp.get_json()["title"] == "learn ci"


def test_add_todo_without_title():
    resp = client.post("/todos", json={})
    assert resp.status_code == 200
