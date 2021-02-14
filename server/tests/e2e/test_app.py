import httpx

BASE_URL = "http://localhost:8000"


def test_startup():
    assert httpx.get(f"{BASE_URL}/docs").status_code == 200


def test_authentication_failure():
    r = httpx.get(f"{BASE_URL}/admin/health", auth=("bad_user", "bad_password"))
    assert r.status_code == 401


def test_authentication_success(auth):
    r = httpx.get(f"{BASE_URL}/admin/health", auth=auth)
    assert r.status_code == 204
