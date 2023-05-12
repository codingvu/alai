import random


class EightPuzzle:
    GOAL_STATE = [1, 2, 3, 4, 5, 6, 7, 8, 0]

    def __init__(self, state=None):
        if state is None:
            self.state = self.random_state()
        else:
            self.state = state

    def random_state(self):
        state = self.GOAL_STATE.copy()
        random.shuffle(state)
        return state

    def is_goal_state(self):
        return self.state == self.GOAL_STATE

    def get_successors(self):
        successors = []
        i = self.state.index(0)
        if i not in [0, 1, 2]:  # Move the blank up
            new_state = self.state.copy()
            new_state[i], new_state[i-3] = new_state[i-3], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [0, 3, 6]:  # Move the blank left
            new_state = self.state.copy()
            new_state[i], new_state[i-1] = new_state[i-1], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [6, 7, 8]:  # Move the blank down
            new_state = self.state.copy()
            new_state[i], new_state[i+3] = new_state[i+3], new_state[i]
            successors.append(EightPuzzle(new_state))
        if i not in [2, 5, 8]:  # Move the blank right
            new_state = self.state.copy()
            new_state[i], new_state[i+1] = new_state[i+1], new_state[i]
            successors.append(EightPuzzle(new_state))
        return successors

    def heuristic(self):
        return sum([1 if self.state[i] != self.GOAL_STATE[i] else 0 for i in range(9)])

    def __lt__(self, other):
        return self.heuristic() < other.heuristic()

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def __str__(self):
        return f"{self.state[:3]}\n{self.state[3:6]}\n{self.state[6:]}\n"


def hill_climbing(problem):
    current = problem
    while True:
        print(current)
        if current.is_goal_state():
            return current
        successors = current.get_successors()
        if not successors:
            return current  # Local maxima or plateau
        best = min(successors)
        if best.heuristic() >= current.heuristic():
            return current  # Local maxima or plateau
        current = best


initial_state_a = [1, 2, 3, 4, 5, 6, 7, 0, 8]  # Solution is found
initial_state_b = [1, 2, 3, 4, 0, 5, 7, 8, 6]  # Local maxima or plateau

problem_a = EightPuzzle(initial_state_a)
solution_a = hill_climbing(problem_a)
print(f"Solution found:\n{solution_a}")

problem_b = EightPuzzle(initial_state_b)
local_maxima_or_plateau = hill_climbing(problem_b)
print(f"Local maxima or plateau:\n{local_maxima_or_plateau}")
