'''
from
https://github.com/moozer/nwdesign/blob/master/nwdesign/graphOut/l2Graph.py
'''

import functools
import graphviz as gv

def newGraph():
    return functools.partial(gv.Graph, format='png', engine="neato")()

def addNodes( graph, nodes ):
    # aplphabetically sorted node list
    nodes = sorted( nodes )

    # first add all nodes
    for node in nodes:
        graph.node( node )

def addConnections( graph, connections ):
    for conn in connections:
        graph.edge( conn[0], conn[1] )

def output( graph, graphname ):
    graph.render( "%s.%s"%(graphname, 'dot') )
    graph.save( "%s.dot"%graphname )

if __name__ == "__main__":    
    graph = newGraph()
    addNodes( graph, ["nodeA", "nodeB"])
    addConnections( graph, [("nodeA", "nodeB")])
    output( graph, "test")
