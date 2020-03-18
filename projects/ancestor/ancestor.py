from util import Stack

def earliest_ancestor(ancestors, starting_node):
    #[(Parent,Child)]
    s = Stack()
    s.push([starting_node])

    longest_path = []
    
    visited = set()

    while s.size() > 0:
        path = s.pop()
        node = path[-1]

        if len(path) > len(longest_path):
            longest_path = path
        
        if len(path) == len(longest_path) and path[-1] < longest_path[-1]:
            longest_path = path

        if node not in visited:
            visited.add(node)

            for pair in ancestors:
                if pair[1] == node:
                    new_path = [*path, pair[0]]
                    s.push(new_path)

    if longest_path[-1] == starting_node:
        return -1

    return longest_path[-1]
    
    