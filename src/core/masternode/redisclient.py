import redis

class RedisClient:
    """
    Class send data received in master node to application example.
    """
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis = redis.Redis(host=host, port=port, db=db)

    def save(self, data_json, client_id):
        channel_name = ("Chasar-Client:%s" % client_id)
        self.redis.ZADD([channel_name, data_json])