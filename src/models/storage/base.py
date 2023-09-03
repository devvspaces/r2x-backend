
from abc import ABC, abstractmethod


class ContextStorage(ABC):
    """
    Abstract class for context storage.
    """

    @abstractmethod
    def get(self, context_id):
        """
        Get context by id.
        """
        pass

    @abstractmethod
    def create(self, context: str):
        """
        Create context
        """
        pass

    @abstractmethod
    def update(self, context_id, context: str):
        """
        Update context by id.
        """
        pass


