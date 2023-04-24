from abc import ABC, abstractmethod
from ..core.notification import Notification

class InMemoryGraph:
    """
    A graph that saves all notifications in RAM. Useful for academic purposes.
    For an application in production, it can generate a prohibitive cost of RAM memory.
    """