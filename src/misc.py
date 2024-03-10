import redis
import logging

def get_redis_client(redis_credentials: dict):
    try:
        assert isinstance(redis_credentials, dict), \
            f"redis_credentials must be a dictionary. type sent is: {type(redis_credentials)}"

        if redis_credentials.get("url"):
            return redis.from_url(redis_credentials['url'], decode_responses=True)
        else:
            host = redis_credentials.get('host', 'localhost')
            port = int(redis_credentials.get('port', 6379))
            password = redis_credentials.get('password', None)
            return redis.Redis(
                host=host, 
                port=port,
                password=password,
                decode_responses=True
            )
    except Exception as e:
        logging.error(f"Failed to connect to Redis: {str(e)}")
        raise e
