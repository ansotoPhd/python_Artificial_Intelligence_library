class TreeNode():
    """ Data structure for representing a Node in a searth tree. """

    def __init__(self, state, parent, action, cost, depth):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.depth = depth

    def __repr__(self):

        if not self.parent:
            return "Initial State: \n" + str(self.state)
        else:
            return self.parent.__repr__() + " \nAction: " + str(self.action) + "\n\nState: \n" + str(self.state)

    def __hash__(self):
        return self.state.__hash__()
