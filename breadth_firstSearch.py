# Breadth-first search
"""
O(V+E) -- (vertices and edges in a graph)

BFS is to solve the existence of path and shortest-path problems in graphs

A  models a set of connections
graphs are made up of nodes and edges

Stack is LIFO structure data
Queue is FIFO structure data.

"""
from collections import deque

graph = {}
graph.update({
    "you": ["alice", "bob", "claire"],
    "bob": ["anuj", "peggy"],
    "alice": ["peggy"],
    "claire": ["thom", "jonny"],
    "anuj": [],
    "peggy": [],
    "thom": [],
    "jonny": [],
})


def breadth_first_search(start_name):
    search_queue = deque()
    search_queue += graph[start_name]
    # without a searched list, it will end up a infinite loop
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(person + " is a mango seller!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


def person_is_seller(name):
    return name[-1] == 'm'


breadth_first_search("you")
