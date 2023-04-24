from abc import ABC, abstractmethod
from collections.abc import Callable, Awaitable
from typing import Any, List, Dict
from ..core.notification import Notification

class AbstractGraph(ABC):
    """
    An abstract class that represents a graph.
    Its function is to store notifications between Holons.
    The abstract methods of this graph are useful for explanation-generating algorithms.
    """
    @abstractmethod
    def __init__(self, params:dict):
        """
        Constructor:
        @param params: A dict structure that contains initialization information.
        """
        pass
    @abstractmethod
    def add(self, notification:Notification) -> None | Awaitable[None]:
        """
        Save a notification to the graph.
        @param notification: Instance of class "Notification".
        """
        pass
    @abstractmethod
    def get(self, filters:dict[str,Any]) -> List[Notification] | Awaitable[List[Notification]]:
        """
        Returns a list of saved notifications.
        @param filters: A dict structure that contains the filters to return the notifications.
                        Here are the filters:
                        {
                            'fromId': Holon who sent the notification.
                            'toId': Holon who received the notification
                            'path': Name of the connection over which the notification was sent
                            'values': Array of notification values to look for.
                            'minTime': Lower limit for out time.
                            'maxTime': Upper limit for out time.
                            'minActivationTime': Lower limit for activation time.
                            'maxActivationTime': Upper limit for activation time.
                            'limit': Maximum number of notifications to return.
                        }
        """
        pass