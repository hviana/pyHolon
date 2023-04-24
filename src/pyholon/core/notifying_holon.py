from notification import Notification
from typing import Any, List, Dict
from collections.abc import Callable, Awaitable
import asyncio

class NotifyinfHolon:
    """
    This class represents a standardized structure for notifying processing, for the Notification Oriented Paradigm (NOP).
    """
    holons = {}
    def __init__(self, id:str, f:Callable[[dict], Any | Awaitable[Any]], onNotification:Callable[[Notification], None | Awaitable[None]], diff:dict, initialInputMem:dict[str,Any], initialOutMem:Any):
        """
        Constructor:
        @param id: Unique Holon identifier.
        @param f: Reference to a function. Represents the operation performed by the Holon.
        @param onNotification: Reference to a function. Represents the callback function for each notification.
        @param diff: A dict structure. Contains the functions for comparing notifications.
                     To use this parameter, you must use the pattern below:
                     {
                         'default' : Diff function for all notifications, from input and output memory.
                         'in' : Diff function for all input memory connections.
                         'paths' : {
                             'connection_name_1': Diff function for an input memory connection.
                             ...
                         }
                         'out' : Compare function for output memory.
                     }
                     The keys in this dict are optional and composable. 
                     Async diff functions are supported.
                     When using a more specific diff function, the more generic diff function is overridden.
                     The Diff function must return "true" if it is pertinent to propagate the notification.
                     You can, for example, consider that close numbers are equal, so as not to trigger a new notification.
                     Criteria not based on similarity can also be used.
                     An example would be propagating the notification according to a propagation probability.
        @param initialInputMem: A dict structure. Represents the initial value for input memory. Example:
                                {
                                    'connection_name_1': value1
                                    ...
                                }
        @param initialOutMem: Represents the Initial Value for the output memory.
        """
        self.id = id
        self.f = f
        self.onNotification = onNotification
        self.diff = diff
        self.im = initialInputMem
        self.om = initialOutMem
        self.__lock = asyncio.Lock()
    def connect(self, paths: dict[str, str], modes: List[str]) -> None:
        """
        Connect Holons.
        @param paths: A dict structure. Example:
                      {
                          'connection1': 'holonId1',
                          ...
                      }
        @param modes: Array of strings, containing notification modes "RENOTIFICATION", "WEAK" or "STRONG".
        """
        pass
    def receive(self, notifications: dict[str, Notification | Any], modes: List[str]) -> None:
        """
        @param notifications: Incoming notifications in a dict structure. Example:
                              {
                                  'connection1': "Notification" instance or any value
                                  ...
                              }
        @param modes: Array of strings, containing notification modes "RENOTIFICATION", "WEAK" or "STRONG".
        """
        self.__processInput(notifications, modes)
    async def __processInput(self, notifications: dict[str, Notification | Any], modes: List[str]) -> Awaitable[None]:
        try:
            await self.__lock.acquire()
            #todo
        except Exception as e:
            print(e)
        finally:
            self.__lock.release()