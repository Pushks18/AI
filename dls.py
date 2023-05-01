class Node:
    def __init__(self, state, parent, move):
        self.state = state
        self.parent = parent
        self.move = move
        
    def __str__(self):
        return str(self.state)

def depth_limited_search(start_state, goal_state, limit):
    start_node = Node(start_state, None, None)

    if start_state == goal_state:
        return start_node

    frontier = [start_node]
    explored = []
    depth = 0

    while frontier:
        if depth > limit:
            return None

        node = frontier.pop(0)
        explored.append(node)
        for move, new_state in get_successors(node.state):
            if new_state == goal_state:
                return Node(new_state, node, move)
            if not any(new_state == n.state for n in explored) and not any(new_state == n.state for n in frontier):
                child_node = Node(new_state, node, move)
                frontier.append(child_node)
                print(child_node)

        if not frontier:
            return None
        depth = node_depth(frontier[0])
    return None

def get_successors(state):
    successors = []
    blank_index = state.index(0)
    if blank_index not in [0, 1, 2]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 3] = new_state[blank_index - 3], new_state[blank_index]
        successors.append(('UP', new_state))
    if blank_index not in [6, 7, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 3] = new_state[blank_index + 3], new_state[blank_index]
        successors.append(('DOWN', new_state))
    if blank_index not in [0, 3, 6]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index - 1] = new_state[blank_index - 1], new_state[blank_index]
        successors.append(('LEFT', new_state))
    if blank_index not in [2, 5, 8]:
        new_state = state[:]
        new_state[blank_index], new_state[blank_index + 1] = new_state[blank_index + 1], new_state[blank_index]
        successors.append(('RIGHT', new_state))

    return successors

def node_depth(node):
    depth = 0
    while node.parent:
        depth += 1
        node = node.parent
    return depth

def print_tree(node):
    if node.parent:
        print_tree(node.parent)
    print(node)

if __name__ == '__main__':
    start_state = [2, 8, 3, 1, 6, 4, 7, 0, 5]
    goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]
    depth_limit = int(input("Enter depth limit: "))
    solution = depth_limited_search(start_state, goal_state, depth_limit)
    if solution:
        print("Solution found at depth:", node_depth(solution))
        print_tree(solution)
    else:
        print("Solution not found within depth limit.")
