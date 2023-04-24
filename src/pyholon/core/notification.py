from typing import Any, List, Dict

class Notification:
    """
    This class represents a Notification Oriented Paradigm (NOP) notification.
    Its construction was designed to aid storage (by ids).
    In addition, it has relevant temporal information for analysis.
    """
    def __init__(self, id: str, fromId: str, toId: str, path: str, value: Any, modes: List[str], time: int, activationTime: int):
        """
        Constructor:
        @param id: Unique notification identifier.
        @param fromId: Unique identifier of the Holon that sent the notification.
        @param toId: Unique identifier of the Holon that received the notification.
        @param path: A string. Represents the name of the connection over which the notification was sent.
        @param value: Notification value.
        @param modes: Array of strings, containing notification modes "RENOTIFICATION", "WEAK" or "STRONG".
        @param time: Time in milliseconds that the notification was output from Holon.
        @param activationTime: Time in milliseconds that Holon was activated to generate this notification..
        """
        self.id = id
        self.fromId = fromId
        self.toId = toId
        self.path = path
        self.value = value
        self.modes = modes
        self.time = time
        self.activationTime = activationTime