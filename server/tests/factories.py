import time

import factory
from faker import Factory as FakerFactory

from models import models


faker = FakerFactory.create()
faker.seed(12345678)


class GyroLogFactory(factory.Factory):
    class Meta:
        model = models.GyroLog

    timestamp = factory.LazyAttribute(lambda x: int(time.time() * 1000000))


class GyroSideFactory(factory.Factory):
    class Meta:
        model = models.GyroSide

    timestamp = factory.LazyAttribute(lambda x: int(time.time() * 1000000))
    side = factory.LazyAttribute(lambda x: faker.pyint(min_value=1, max_value=4))
    name = factory.LazyAttribute(lambda x: faker.sentence())
