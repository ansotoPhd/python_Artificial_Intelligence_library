from abc import ABC, abstractmethod
from search_algorithms.problem_definition.state import State


class SearchProblemDefinition(ABC):

    def __init__(self, state_class, initial_state, actions):
        assert initial_state.__class__ == state_class
        assert State in state_class.__bases__

        self.initial_state = initial_state
        self.state_class = state_class
        self.actions = actions

    @abstractmethod
    def successor_func(self, state, prev_action=None):
        assert state.__class__ == self.state_class

    @abstractmethod
    def objective_test(self, state):
        assert state.__class__ == self.state_class

    def get_initial_state(self):
        return self.initial_state

    def get_actions(self):
        return set()

    def apply_successor_function(self, state):
        pass
