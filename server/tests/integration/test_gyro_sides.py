import pytest

from models import models


@pytest.mark.asyncio
async def test_get_sides(client, db_session, gyro_side_factory):
    side_1 = gyro_side_factory.create(side=1, timestamp=11, name="one")
    side_2 = gyro_side_factory.create(side=2, timestamp=22, name="two")

    db_session.add_all([side_1, side_2])
    db_session.commit()

    response = await client.get("/gyro/sides", params={"page_size": 5})
    assert response.status_code == 200

    api_sides = response.json()

    assert len(api_sides["items"]) == 2

    # newest first
    assert api_sides["items"][0]["timestamp"] == 22
    assert api_sides["items"][0]["name"] == "two"
    assert api_sides["items"][0]["side"] == 2

    assert api_sides["items"][1]["timestamp"] == 11
    assert api_sides["items"][1]["name"] == "one"
    assert api_sides["items"][1]["side"] == 1


@pytest.mark.asyncio
async def test_create_side(client, db_session):
    response = await client.post(
        "/gyro/sides", json={"side": 1, "timestamp": 11, "name": "one"}
    )
    assert response.status_code == 201

    api_side = response.json()

    assert api_side["timestamp"] == 11
    assert api_side["name"] == "one"
    assert api_side["side"] == 1

    db_side = db_session.query(models.GyroSide).get(11)
    assert db_side.name == "one"
    assert db_side.side == 1
