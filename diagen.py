from readYaml import readYaml
from outputDot import L2Diagram


def addNodes( graph, topology ):
    print "Adding devices"
    nodes = topology.keys()
    print "- ", nodes
    graph.addNodes( nodes )

def addConnections( graph, topology ):
    print "Adding connections"
    for device in topology:
        print "- ", device, " -> ", topology[device]["interfaces"]
        for localInterface in topology[device]["interfaces"].keys():
            #graph.addConnections(
            #print localInterface
            conn = (device+"."+localInterface, topology[device]["interfaces"][localInterface])
            graph.addConnections( [conn] )

if __name__ == "__main__":
    # init part
    graph = L2Diagram()

    # handle inpu
    topology = readYaml( "test/inputA.yml" )

    # "business logic"
    addNodes( graph, topology )
    addConnections( graph, topology )

    # output step
    graph.generateOutput("test")
