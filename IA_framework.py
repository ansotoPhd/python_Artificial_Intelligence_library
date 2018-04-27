


class search_problem():

    def __init__(self, initial_state, state_class, sucessor_func):
        self.initial_state = initial_state
        self.state_class = state_class
        self.sucessor_func = sucessor_func

    def get_initial_state(self):
        pass

    def create_state(self, state_data):
        pass

    def actions(self):
        return set()

    def apply_successor_function(self, state):
        pass


