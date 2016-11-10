'''
from
https://github.com/moozer/nwdesign/blob/master/nwdesign/graphOut/l2Graph.py
'''

import functools
import graphviz as gv

class L2Diagram:
    def __init__( self ):
        self._graph = functools.partial(gv.Graph, format='png', engine="neato")()

    def addNodes( self, nodes ):
        # aplphabetically sorted node list
        nodes = sorted( nodes )

        # first add all nodes
        for node in nodes:
            self._graph.node( node )

    def addConnections( self, connections ):
        for conn in connections:
            try:
                self.addConnection( conn )
            except AttributeError, ex:
                # if either dst or src is None
                pass

    def addConnection( self, connection ):
        # all connections are in duplex, so skipping one
        if connection[0] > connection[1]:
            return

        src = connection[0].split(".")
        dst = connection[1].split(".")
        self._graph.edge( src[0], dst[0] )


    def generateOutput( self, graphname ):
        self._graph.render( "%s.%s"%(graphname, 'dot') )
        self._graph.save( "%s.dot"%graphname )

if __name__ == "__main__":
    graph = L2Diagram()
    graph.addNodes( ["nodeA", "nodeB"])
    graph.addConnections( [("nodeA", "nodeB")])
    graph.generateOutput( "test")
