import time

import pytest

from models import models


@pytest.mark.asyncio
async def test_get_logs(client, db_session, gyro_side_factory, gyro_log_factory):
    side = gyro_side_factory.create(side=1, timestamp=11, name="one")

    log_1 = gyro_log_factory(timestamp=123, side_timestamp=11, side=1)
    log_2 = gyro_log_factory(timestamp=456, side_timestamp=11, side=1)
    db_session.add_all([side, log_1, log_2])
    db_session.commit()

    response = await client.get("/gyro/logs", params={"page_size": 5})
    assert response.status_code == 200

    given = response.json()

    assert len(given["items"]) == 2
    # newest first
    assert given["items"][0]["timestamp"] == 456
    assert given["items"][1]["timestamp"] == 123

    for log in given["items"]:
        assert log["side"] == 1
        assert log["sides"]["timestamp"] == 11
        assert log["sides"]["name"] == "one"


@pytest.mark.asyncio
async def test_save_a_log_and_assign_side(client, db_session, gyro_side_factory):
    side_1 = gyro_side_factory.create(side=1, timestamp=11, name="one")
    side_2 = gyro_side_factory.create(side=2, timestamp=22, name="two")
    db_session.add_all([side_1, side_2])
    db_session.commit()

    response = await client.post("/gyro/logs", params={"side": 1})
    assert response.status_code == 201

    given = response.json()
    assert given["side"] == 1
    assert given["sides"]["name"] == "one"
    assert given["sides"]["timestamp"] == 11
    timestamp = given["timestamp"]
    assert timestamp == pytest.approx(time.time(), 1)

    db_log = db_session.query(models.GyroLog).get(timestamp)
    assert db_log.side == 1
    assert db_log.side_timestamp == 11


@pytest.mark.asyncio
async def test_assign_log_to_newest_side(client, db_session, gyro_side_factory):
    side_1_old = gyro_side_factory.create(side=1, timestamp=11, name="old")
    side_1_new = gyro_side_factory.create(side=1, timestamp=12, name="new")
    db_session.add_all([side_1_new, side_1_old])
    db_session.commit()

    response = await client.post("/gyro/logs", params={"side": 1})
    assert response.status_code == 201

    given = response.json()
    assert given["side"] == 1
    assert given["sides"]["name"] == "new"
    assert given["sides"]["timestamp"] == 12
    timestamp = given["timestamp"]
    assert timestamp == pytest.approx(time.time(), 1)

    db_log = db_session.query(models.GyroLog).get(timestamp)
    assert db_log.side == 1
    assert db_log.side_timestamp == 12
