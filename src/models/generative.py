"""
Generative model
"""
from abc import ABC, abstractmethod

class GenerativeModel(ABC):
    """
    Abstract class for generative model proxies.
    """

    @abstractmethod
    def prompt(self, input, **kwargs) -> str:
        """
        Prompt the generative model.
        """
        pass

    @abstractmethod
    def prompt_with_context(self, input, context: str, **kwargs) -> str:
        """
        Prompt the generative model with context.
        """
        pass