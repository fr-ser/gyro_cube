import pytest


@pytest.mark.asyncio
async def test_pagination(client, db_session, gyro_side_factory):
    stuff = gyro_side_factory.create_batch(100)
    db_session.add_all(stuff)
    db_session.commit()

    response = await client.get("/gyro/sides?size=5&page=3")
    assert response.status_code == 200

    given = response.json()

    assert type(given["items"]) is list
    assert given["size"] == 5
    assert given["size"] == len(given["items"])
    assert given["page"] == 3
    assert given["total"] == 100
