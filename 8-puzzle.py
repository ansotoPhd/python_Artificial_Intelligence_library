from search_algorithms.problem_definition.state import State
from search_algorithms.problem_definition.search_problem import SearchProblemDefinition
import numpy as np
import copy
from search_algorithms.IA_search_algorithms import IA_SearchAlgorithm


######################################################################
# PROBLEM DEFINITION
######################################################################

class PuzzleState(State):
    def __init__(self, state_data):
        super().__init__(state_data)

    @staticmethod
    def equals(state_a, state_b):
        return np.array_equal(state_a.get_sliding_parts(), state_b.get_sliding_parts())

    @classmethod
    def create_State(cls, state_data):
        return super().create_State(state_data)

    def __repr__(self):
        super().__repr__()
        return str(self.get_sliding_parts())

    def validate_state(self):
        valid = (("board_size" in self.state_data) and
                 ("sliding_parts" in self.state_data) and
                 (self.get_sliding_parts().shape == (self.get_board_size(), self.get_board_size()))
                 )
        return valid

    def get_sliding_parts(self):
        return self.state_data["sliding_parts"]

    def get_board_size(self):
        return int(self.state_data["board_size"])


class PuzzleProblemDefinition(SearchProblemDefinition):
    def objective_test(self, state):
        super(PuzzleProblemDefinition, self).objective_test(state)

        return np.array_equal(state.state_data["sliding_parts"],
                              np.matrix([[None, 1, 2],
                                         [3, 4, 5],
                                         [6, 7, 8]]))

    def successor_func(self, state, prev_action=None):
        super(PuzzleProblemDefinition, self).objective_test(state)

        def do_action(action, i, j, cur_state_data):
            sliding_parts = cur_state_data["sliding_parts"]
            if action == "up":
                sliding_parts[i, j] = sliding_parts[i - 1, j]
                sliding_parts[i - 1, j] = None
            if action == "down":
                sliding_parts[i, j] = sliding_parts[i + 1, j]
                sliding_parts[i + 1, j] = None
            if action == "left":
                sliding_parts[i, j] = sliding_parts[i, j - 1]
                sliding_parts[i, j - 1] = None
            if action == "right":
                sliding_parts[i, j] = sliding_parts[i, j + 1]
                sliding_parts[i, j + 1] = None
            return cur_state_data

        action_state_list = []

        sliding_parts = state.get_sliding_parts()
        board_size = state.get_board_size()

        # Find empty position
        i, j = np.where(sliding_parts == None);
        i = i[0];
        j = j[0]

        # Go up
        if i != 0 and prev_action != "down":
            action_state_list.append(("up", PuzzleState(do_action("up", i, j, copy.deepcopy(state.state_data)))))
        # Go down
        if i != (board_size - 1) and prev_action != "up":
            action_state_list.append(("down", PuzzleState(do_action("down", i, j, copy.deepcopy(state.state_data)))))
        # Go left
        if j != 0 and prev_action != "right":
            action_state_list.append(("left", PuzzleState(do_action("left", i, j, copy.deepcopy(state.state_data)))))
        # Go right
        if j != (board_size - 1) and prev_action != "left":
            action_state_list.append(("right", PuzzleState(do_action("right", i, j, copy.deepcopy(state.state_data)))))

        return action_state_list


puzzle_actions = {"up", "down", "left", "right"}

######################################################################
# EXAMPLE PROBLEMS
######################################################################

initial_state_data = {
    "board_size": 3,
    "sliding_parts": np.matrix([[1, 2, None],
                                [4, 5, 3],
                                [7, 8, 6]])
}

initial_state_data = {
    "board_size": 3,
    "sliding_parts": np.matrix([[6, 4, 7],
                                [8, None, 1],
                                [3, 5, 2]])
}

initial_state_data = {
    "board_size": 3,
    "sliding_parts": np.matrix([[6, 4, 7],
                                [8, 5, None],
                                [3, 2, 1]])
}

objective_state_data = {
    "board_size": 3,
    "sliding_parts": np.matrix([[None, 1, 2],
                                [3, 4, 5],
                                [6, 7, 8]])
}

# d=21
#      8 3 1 0 2 5 6 7 4
initial_state_data = {
    "board_size": 3,
    "sliding_parts": np.matrix([[8, 3, 1],
                                [None, 2, 5],
                                [6, 7, 4]])
}

initial_state = PuzzleState(initial_state_data)
objective_state = PuzzleState(objective_state_data)

puzzle_problem = PuzzleProblemDefinition(PuzzleState, initial_state, puzzle_actions)

print(initial_state.validate_state())
print(puzzle_problem.objective_test(initial_state))
print(puzzle_problem.objective_test(objective_state))

a = puzzle_problem.successor_func(initial_state)

b = puzzle_problem.successor_func(initial_state, prev_action="right")
print(b)

# https://github.com/wolfchimneyrock/8-Puzzle-Solver/blob/master/3x3.txt

ia_search = IA_SearchAlgorithm(puzzle_problem,
                               {"strategy": "depth-first",
                                "treat_repeated_states": True,
                                "maximum_length": 22}
                               )

# ia_search = IA_SearchAlgorithm(puzzle_problem,
#                                {"strategy": "breadth-first",
#                                 "treat_repeated_states": True})

a = ia_search.start()

print(str(a))
