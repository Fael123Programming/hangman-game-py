class Status:

    __slots__ = ["_status"]

    _defeat = -1
    _victory = 1
    _in_progress = 0
    _not_started = None

    def __init__(self):
        self._status = Status._not_started

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        if status == self._defeat or status == self._victory or status == self._in_progress:
            self._status = status
        else:
            raise ValueError("Unknown status")

    @classmethod
    def defeat(cls):
        return cls._defeat

    @classmethod
    def victory(cls):
        return cls._victory

    @classmethod
    def in_progress(cls):
        return cls._in_progress
