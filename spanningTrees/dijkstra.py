"""
Andrea Murphy
The root bridge of the Spanning Tree 
Prim's spanning tree & Dijkstra's shortest path algorithm
Python 3
Date: March 6, 2019

"""


import sys

from functools import total_ordering


@total_ordering
class Vertex:
    def __init__(self, node):
        # id == bridge id
        self.id = node
        self.adjacent = {}

        # Assign to every node a tentative distance value
        #Set distance to infinity for all nodes
        self.distance = sys.maxsize

        # Mark all nodes unvisited        
        self.visited = False  

        # Predecessor
        self.previous = None

    def __lt__(self, other):
        if isinstance(other, self.__class__):
            return self.distance < other.distance
        return NotImplemented

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

def shortest(v, path):
    ''' make shortest path from v.previous'''
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return

import heapq

def dijkstra(aGraph, start):
    print('''Dijkstra's shortest path''')

    # For the starting node, initialization
    # Set the distance for the start node to zero 
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(),v) for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance 
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        #for next in v.adjacent:
        for next in current.adjacent:
            # if visited, skip
            if next.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next)
            
            if new_dist < next.get_distance():
                next.set_distance(new_dist)
                next.set_previous(current)
                print('updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))
            else:
                print('not updated : current = %s next = %s new_dist = %s' \
                        %(current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(),v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


if __name__ == '__main__':

    g = Graph()

    # root node, because 0 is the lowest priority
    # making the bridge id the lowest 
    g.add_vertex('0.1234.1234.1234')
    g.add_vertex('1.1111.1111.1111')
    g.add_vertex('1.222.222.222')
    g.add_vertex('2.1212.1212.1212')
    g.add_vertex('3.1111.1111.1111')
    g.add_vertex('4.1234.1235.2321')

    g.add_edge('0.1234.1234.1234', '1.1111.1111.1111', 7)  
    g.add_edge('0.1234.1234.1234', '1.222.222.222', 9)
    g.add_edge('0.1234.1234.1234', '4.1234.1235.2321', 14)
    g.add_edge('1.1111.1111.1111', '1.222.222.222', 10)
    g.add_edge('1.1111.1111.1111', '2.1212.1212.1212', 15)
    g.add_edge('1.222.222.222', '2.1212.1212.1212', 11)
    g.add_edge('1.222.222.222', '4.1234.1235.2321', 2)
    g.add_edge('2.1212.1212.1212', '3.1111.1111.1111', 6)
    g.add_edge('3.1111.1111.1111', '4.1234.1235.2321', 9)

    print ('Graph data:')
    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

            
    dijkstra(g, g.get_vertex('0.1234.1234.1234'))

    for t in ['2.1212.1212.1212','3.1111.1111.1111','4.1234.1235.2321']:
        target = g.get_vertex(t)
        path = [t]
        shortest(target, path)
        print ('The shortest path for %s : %s' %(t, path[::-1]))


