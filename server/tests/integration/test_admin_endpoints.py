import pytest


@pytest.mark.asyncio
async def test_can_get_open_api_spec(client):
    response = await client.get("/docs")
    assert response.status_code == 200


@pytest.mark.asyncio
async def test_health(client):
    response = await client.get("/admin/health")
    assert response.status_code == 204
