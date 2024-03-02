import logging
import redis
import apache_beam as beam
from apache_beam.io import iobase
from apache_beam.transforms import (
    DoFn, PTransform, Reshuffle
)
from apache_beam.options.value_provider import ValueProvider, StaticValueProvider


class ReadFromRedis(PTransform):
    def __init__(self, **kwargs):
        pass
