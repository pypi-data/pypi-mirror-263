# python-state-manager
A simple state machine to handle states of programs.

# Usage

Example:

```python
from python_state_manager import StateManager
stateids = ["state1", "state2", "state3"]
statevalues = [1, 2, 3]
metadatas = [{"a": 1}, {"b": 2}, {"c": 3}]
sm = StateManager(stateids, statevalues, metadatas, currentstateid="state1")
print(sm.get_current_state().stateid)
# output: state1
sm.complete_state()
print(sm.is_finished())
# output: False
print(sm.get_current_state().stateid)
# state2
```

Enjoy!