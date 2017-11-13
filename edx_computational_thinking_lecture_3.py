# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:15:06 2017

@author: rahul
"""

class Node:
    
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return ''.join(('Node<', self.name, '>'))


class Edge:
    
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
    def __str__(self):
        return ''.join((self.source.name, '->', self.dest.name))


class DiGraph:
    
    """ edges is a dict mapping a node to a list of its children 
    """
    
    def __init__(self):
        self.edges = {}
    
    def add_node(self, node):
        if node in self.edges:
            raise ValueError('Duplicate node: ' + node.name)        
        self.edges[node] = []
    
    def add_edge(self, edge):
        src = edge.source
        dest = edge.dest
        if src not in self.edges:
            raise ValueError('Source Node not in graph: ' + str(src))
        if dest not in self.edges:
            raise ValueError('Destination Node not in graph: ' + str(dest))
        self.edges[src].append(dest)
    
    def children_of(self, node):
        if node not in self.edges:
            raise ValueError('Node not in graph: ' + node)
        return self.edges[node]
    
    def has_node(self, node):
        return node in self.edges
    
    def get_node(self, name):
        for node in self.edges:
            if node.name == name:
                return node
        raise NameError(' '.join('No node with name', name))
    
    def __str__(self):
        result = []
        for node, children in self.edges.items():
            result.append(''.join((node.name, ' -> ', str([nd.name for nd in children]))))
        return '\n'.join(result)
            

class Graph(DiGraph):
    
    def add_edge(self, edge):
        super().add_edge(edge)
        rev = Edge(source=edge.dest, dest=edge.source)
        super().add_edge(rev)


def build_city_graph(graph_type):
    boston = Node('Boston')
    providence = Node('Providence')
    new_york = Node('New York')
    chicago = Node('Chicago')
    denver = Node('Denver')
    phoenix = Node('Phoenix')
    los_angeles = Node('Los Angeles')
    
    edges = {}
    edges[boston] = [providence, new_york]
    edges[providence] = [new_york, boston]
    edges[new_york] = [chicago]
    edges[chicago] = [denver, phoenix]
    edges[denver] = [new_york, phoenix]
    edges[phoenix] = []
    edges[los_angeles] = [boston]
    
    route_graph = graph_type()
    for node in edges.keys():
        route_graph.add_node(node)
        
    for source, children in edges.items():        
        for child in children:
            route_graph.add_edge(Edge(source=source, dest=child))
    
    return route_graph


print(build_city_graph(DiGraph))







        
    
    
                        