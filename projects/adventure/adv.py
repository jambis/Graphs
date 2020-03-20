from room import Room
from player import Player
from world import World

from util import Queue
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "projects/adventure/maps/test_cross.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)
print("THE ROOMS ", world.rooms)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

opposite_directions = {
    'n':'s',
    's':'n',
    'e':'w',
    'w':'e'
}

def dft_recursive(starting_room):
    
    def dft_recursive_helper(room, visited):
        visited.add(room.id)
        path = []

        for direction in room.get_exits():
            next_room = room.get_room_in_direction(direction)
            if next_room.id not in visited:
                next_room_path = dft_recursive_helper(next_room, visited)
                if next_room_path:
                    # print("next_room_path: ", next_room_path)
                    new_path = [direction, *next_room_path, opposite_directions[direction]]
                    # print("new_path in IF: ", new_path)
                else:
                    new_path = [direction, opposite_directions[direction]]
                    # print("new_path in else: ", new_path)

                path = [*path, *new_path]
        return path

    visited = set()
    path = dft_recursive_helper(starting_room, visited)
    print(path)

    return path


# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = dft_recursive(player.current_room)



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
