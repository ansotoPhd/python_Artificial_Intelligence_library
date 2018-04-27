from search_algorithms.problem_definition.search_problem import SearchProblemDefinition
from search_algorithms.search_tree.node import TreeNode
import math
import queue


class IA_SearchAlgorithm:

    strategies = {"breadth-first", "depth-first"}

    def __init__(self, problem, strategy_definition):

        # => Strategy definition
        #       · Tree search algorithm
        self.strategy = strategy_definition["strategy"]
        assert self.strategy in self.strategies
        #       · Repeated states treatment
        self.treat_repeated_states = strategy_definition["treat_repeated_states"]
        #       · Maximum length
        self.maximum_length = strategy_definition["maximum_length"] if "maximum_length" in strategy_definition else math.inf

        # => Problem definition
        self.problem = problem
        assert isinstance(problem, SearchProblemDefinition)

        # => Initializations
        #       · Queue construction - based on search strategy
        if self.strategy == "breadth-first":
            self.queue = queue.Queue()
        if self.strategy == "depth-first":
            self.queue = queue.LifoQueue()

    def start(self):

        # · Enqueue initial node
        initial_node = self._make_node(self.problem.get_initial_state())
        self.queue.put(initial_node)

        # · Main search loop
        iter = 1
        filtered_nodes = 0
        filtered_frontier = 0
        filtered_path_loop = 0
        while 1:

            if self.queue.empty():
                return None

            # · Getting node from queue
            cur_node = self.queue.get()

            # · Checking if objective is reached
            if self.problem.objective_test(cur_node.state):
                return cur_node

            # => Filtering repeated states
            expanding = True
            if self.treat_repeated_states:
                # · Depth-first strategy
                if self.strategy == "depth-first":
                    # - The repeated state is in the structure of open nodes
                    # - Avoid loops in the same path
                    dupl_in_frontier = self._has_duplicate_states_frontier_depth_first(cur_node)
                    dupl_in_path = self._has_duplicate_states_path_depth_first(cur_node)

                    filtered_frontier += int(dupl_in_frontier)
                    filtered_path_loop += int(dupl_in_path)

                    expanding = (not dupl_in_frontier) and (not dupl_in_path)
                    if not expanding:
                        filtered_nodes += 1

            # · Expanding node
            if expanding and cur_node.depth < self.maximum_length:
                child_nodes = self._expand_node(cur_node)
                [self.queue.put(x) for x in child_nodes]

            if iter % 100 == 0:
                print("Iteration: " + str(iter))
                print("\tCurrent node depth: " + str(cur_node.depth))
                print("\tFrontier size: " + str(self.queue.qsize()))
                print("\tFiltered_nodes: " + str(filtered_nodes))
                print("\t\tFrontier: " + str(filtered_frontier))
                print("\t\tPath (loops): " + str(filtered_path_loop))

            iter += 1

    def _has_duplicate_states_frontier_depth_first(self, node):
        duplicates = False
        for f_node in list(self.queue.queue):
            duplicates = self.problem.state_class.equals(node.state, f_node.state) and \
                            node.cost >= f_node.cost
            if duplicates:
                break

        return duplicates

    def _has_duplicate_states_path_depth_first(self, node):
        cur_state = node.state
        duplicates = False
        parent = node.parent
        while not duplicates and parent is not None:
            duplicates = self.problem.state_class.equals(cur_state, parent.state)
            parent = parent.parent
        return duplicates

    def _make_node(self, state, prev_node=None, action=None, cost=None):
        if prev_node:
            return TreeNode(state, prev_node, action, cost, prev_node.depth + 1)
        return TreeNode(state, prev_node, None, 0, 1)

    def _expand_node(self, node):
        """
            Expands a tree node
        """
        if node.parent:
            successors = self.problem.successor_func(node.state, prev_action=node.action)
        else:
            successors = self.problem.successor_func(node.state)
        successors_nodes = []
        for action, next_state in successors:
            successors_nodes.append(self._make_node(next_state, node, action, node.cost + 0))
        return successors_nodes
