import time

import pytest

from models import models


@pytest.mark.asyncio
async def test_save_a_log(client, db_session, gyro_side_factory):
    side_1 = gyro_side_factory.create(side=1, timestamp=11, name="one")
    db_session.add(side_1)
    db_session.commit()

    response = await client.post("/gyro/logs", params={"side": 1})
    assert response.status_code == 200

    given = response.json()
    assert given["side"] == 1
    assert given["sides"]["name"] == "one"
    timestamp = given["timestamp"]
    assert timestamp == pytest.approx(time.time(), 1)

    db_log = db_session.query(models.GyroLog).get(timestamp)
    assert db_log.side == 1
