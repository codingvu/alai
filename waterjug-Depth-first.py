#Depth First Search
from collections import deque
def main():
    starting_node = [(0, 0)]
    jugs = (5, 3)
    goal_amount = 4
    check_set = set()
    search(starting_node, jugs, goal_amount, check_set)
def get_index(node):
    return pow(7, node[0]) * pow(5, node[1])
def is_goal(path, goal_amount):
    return path[-1][0] == goal_amount or path[-1][1] == goal_amount
def been_there(node, check_set):
    return get_index(node) in check_set
def next_transitions(jugs, path, check_set):
    result = []
    a_max, b_max = jugs
    a, b = path[-1]
    next_nodes = [(a_max, b), (a, b_max), (min(a_max, a + b), b - (min(a_max, a + b) - a)),
                  (min(a + b, b_max), a - (min(a + b, b_max) - b)), (0, b), (a, 0)]
    result = [list(path) + [node]
              for node in next_nodes if not been_there(node, check_set)]
    return result
def print_path(path):
    print(f"0: {path[0]}")
    for i, node in enumerate(path[1:], 1):
        print(f"{i}: {node}")
def search(starting_node, jugs, goal_amount, check_set):
    goal = []
    solved = False
    q = deque()
    q.appendleft(starting_node)
    while len(q) != 0:
        path = q.popleft()
        check_set.add(get_index(path[-1]))
        if is_goal(path, goal_amount):
            solved = True
            goal = path
            break
        next_moves = next_transitions(jugs, path, check_set)
        q.extendleft(next_moves)
    if solved:
        print_path(goal)
    else:
        print("Problem cannot be solved.")
if __name__ == '__main__':
    main()
