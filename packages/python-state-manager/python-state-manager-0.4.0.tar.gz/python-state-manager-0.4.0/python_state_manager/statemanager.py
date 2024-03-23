from typing import Callable, Dict, List

from .state import State


def init_dependencies(stateids: List[str]):
    dependencies = {}
    for i, stateid in enumerate(stateids):
        dependencies[stateid] = stateids[:i]
    return dependencies

class StateManager:
    def __init__(
        self,
        stateids: List[str] = [],
        statevalues: List[any] = [],
        metadatas: List[Dict] = [],
        currentstateid: str = None,
        callbacks: Dict[str, Dict[str, List[Callable]]] = {},
        dependencies: Dict[str, List[str]] = {},
    ):
        
        assert currentstateid != None and currentstateid in stateids, "currentstateid must be in stateids"

        # if there are callbacks
        if len(callbacks) != 0:
            all_entry_callbacks = [callbacks[stateid]["entry_callbacks"] for stateid in stateids]
            all_exit_callbacks = [callbacks[stateid]["exit_callbacks"] for stateid in stateids]
        else:
            all_entry_callbacks = {stateid: {"entry_callbacks": [], "exit_callbacks": []} for stateid in stateids}
            all_exit_callbacks = {stateid: {"entry_callbacks": [], "exit_callbacks": []} for stateid in stateids}
        
        self.states = {
            stateid: State(stateid, is_current=stateid == currentstateid, value=statevalue, metadata=metadata, entry_callbacks=entry_callbacks, exit_callbacks=exit_callbacks) 
            for stateid, statevalue, metadata, entry_callbacks, exit_callbacks in zip(stateids, statevalues, metadatas, all_entry_callbacks, all_exit_callbacks)
        }

        if len(dependencies) == 0:
            self.dependencies = init_dependencies(stateids)
        else:
            self.dependencies = dependencies

    def get_current_state(self):
        for state in self.states.values():
            if state.is_current:
                return state
            
    def get_state(self, stateid):
        return self.states[stateid]

    def complete_state(self):
        current_state = self.get_current_state()
        current_state.exit()
        current_state.is_current = False
        for state in self.states.values():
            # if the state is not finished and all the dependencies are finished, then enter the state
            if not state.is_finished() and all([self.get_state(dependency).is_finished() for dependency in self.dependencies[state.stateid]]):
                state.is_current = True
                state.enter()
                break
        
    def is_finished(self):
        return all([state.is_finished() for state in self.states.values()])
    
    def is_processing(self):
        return not self.is_finished()
    
    def get_state_values(self):
        return [state.value for state in self.states.values()]
    
    def get_state_metadatas(self):
        return [state.metadata for state in self.states.values()]
    
    def get_state_ids(self):
        return [state.stateid for state in self.states.values()]
    
# if __name__ == "__main__":
    # stateids = ["state1", "state2", "state3"]
    # statevalues = [1, 2, 3]
    # metadatas = [{"a": 1}, {"b": 2}, {"c": 3}]
    # sm = StateManager(stateids, statevalues, metadatas, currentstateid="state1")
    # print(sm.get_current_state().stateid)
    # sm.complete_state()
    # print(sm.is_finished())
    # print(sm.get_current_state().stateid)
    # sm.complete_state()
    # print(sm.is_finished())
    # print(sm.get_current_state().stateid)
    # sm.complete_state()
    # print(sm.is_finished())
    # print(sm.get_current_state().stateid)
    # sm.complete_state()
    # print(sm.is_finished())