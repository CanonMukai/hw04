# coding:utf-8

import networkx as nx
import matplotlib.pyplot as plt

# file -> graph
def make_graph(pages_file, links_file):
    graph = nx.DiGraph()
    return graph


# test of make_graph
def test_make_graph(pages_file, links_file):
    graph = make_graph(pages_file, links_file)
    nx.draw_networkx(graph)
    plt.show()


# shortest path from start point to destination
def shortest_path(start_node, destination_node):
    return "Not Found"


# tests
def run_Test():
    test_make_graph("a.txt", "b.txt")

    
run_Test()

# main
graph = make_graph("pages.txt", "links.txt")
print shortest_path("Google", "渋谷") 
