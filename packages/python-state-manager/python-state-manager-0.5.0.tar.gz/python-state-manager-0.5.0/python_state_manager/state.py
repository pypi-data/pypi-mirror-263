from typing import Callable, Dict, List


class State:

    def __init__(
        self,
        stateid: str,
        is_current: bool = False,
        value: any = None,
        metadata: Dict = {},
        entry_callbacks: List[Callable] = [],
        exit_callbacks: List[Callable] = [],
    ):
        self.stateid = stateid
        self.is_current = is_current
        self.value = value
        self.metadata = metadata
        self.entry_callbacks = entry_callbacks
        self.exit_callbacks = exit_callbacks
        self.status = {
            "entered": False,
            "processing": False,
            "exited": False,
        }

    def __str__(self):
        return self.stateid

    def enter(self):
        self.status["entered"] = True
        for callback in self.entry_callbacks:
            callback()

    def exit(self):
        self.status["exited"] = True
        for callback in self.exit_callbacks:
            callback()

    def is_finished(self):
        return self.status["exited"]
    
    def is_processing(self):
        return self.status["processing"]
    
    def is_entered(self):
        return self.status["entered"]
    
    def is_exited(self):
        return self.status["exited"]