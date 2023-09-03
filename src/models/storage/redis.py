
from .base import ContextStorage
import redis

class RedisContextStorage(ContextStorage):
    """
    Redis context storage.
    """

    def __init__(self, connection_string):
        self.__redis_client = redis.Redis.from_url(connection_string)

    def get(self, context_id):
        """
        Get context by id.
        """
        return self.__redis_client.get(context_id)

    def create(self, context: str):
        """
        Create context
        """
        self.__redis_client.set(context.id, context)

    def update(self, context_id, context: str):
        """
        Update context by id.
        """
        current = self.get(context_id)
        if current:
            context = current + context
        self.__redis_client.set(context_id, context)
