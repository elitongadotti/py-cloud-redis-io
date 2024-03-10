import redis
import logging
import apache_beam as beam
from apache_beam.io import iobase
from misc import get_redis_client

# TODO: add cluster-client - https://redis.readthedocs.io/en/stable/connections.html#cluster-client

class ReadFromRedis(beam.DoFn):
    """Reads from redis and returns the value of the key.
    The input can be either a PColl of string, list of keys or tuples (first pos is the key).
    Output is either a string or a list.
    """
    def __init__(self, credentials: dict = {}):
        self.redis: redis.Redis = None
        self.credentials = credentials

    def setup(self):
        self.redis = get_redis_client(self.credentials)
        
    def process(self, element):
        if isinstance(element, str):
            yield self.redis.get(element)
        elif isinstance(element, list):
            yield self.redis.mget(element)
        elif isinstance(element, tuple):
            yield self.redis.get(element[0])
        
    def teardown(self):
        self.redis.close()


class WriteToRedisDoFn(beam.DoFn):
    def __init__(self, credentials: dict):
        self.redis: redis.Redis = None
        self.credentials = credentials

    def setup(self):
        self.redis = get_redis_client(self.credentials)
        
    def process(self, element):
        key, value = element
        self.redis.set(key, value)
        yield key, value

    def teardown(self):
        self.redis.close()


@beam.ptransform_fn
def WriteToRedis(pcoll, credentials: dict = {}):
    return (
        pcoll 
        | beam.ParDo(WriteToRedisDoFn(credentials))
    )
