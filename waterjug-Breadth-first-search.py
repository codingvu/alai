#Breadth First Search
from collections import deque
def main():
    starting_node = [[0, 0]]
    jugs = [5, 3]
    goal_amount = 4
    check_dict = {}
    search(starting_node, jugs, goal_amount, check_dict)
def get_index(node):
    return pow(7, node[0]) * pow(5, node[1])
def is_goal(path, goal_amount):
    return path[-1][0] == goal_amount or path[-1][1] == goal_amount
def been_there(node, check_dict):
    return check_dict.get(get_index(node), False)
def next_transitions(jugs, path, check_dict):
    result = []
    next_nodes = []
    node = []
    a_max = jugs[0]
    b_max = jugs[1]
    a = path[-1][0]
    b = path[-1][1]
    node.append(a_max)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(a)
    node.append(b_max)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(min(a_max, a + b))
    node.append(b - (node[0] - a))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(min(a + b, b_max))
    node.insert(0, a - (node[0] - b))
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(0)
    node.append(b)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    node = []
    node.append(a)
    node.append(0)
    if not been_there(node, check_dict):
        next_nodes.append(node)
    for i in range(0, len(next_nodes)):
        temp = list(path)
        temp.append(next_nodes[i])
        result.append(temp)
    return result
def print_path(path):
    print(f"0: {path[0]}")
    for i in range(0, len(path) - 1):
        print(i+1, ":", path[i+1])
def search(starting_node, jugs, goal_amount, check_dict):
    goal = []
    solved = False
    q = deque()
    q.appendleft(starting_node)
    while len(q) != 0:
        path = q.popleft()
        check_dict[get_index(path[-1])] = True
        if is_goal(path, goal_amount):
            solved = True
            goal = path
            break
        next_moves = next_transitions(jugs, path, check_dict)
        for i in next_moves:
            q.append(i)
    if solved:
        print_path(goal)
    else:
        print("Problem cannot be solved.")
if __name__ == '__main__':
    main()
