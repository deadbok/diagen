from readYaml import readYaml
from outputDot import L2Diagram

if __name__ == "__main__":
    topology = readYaml( "test/inputA.yml" )

    graph = L2Diagram()

    print "Adding devices"
    nodes = topology.keys()
    print "- ", nodes
    graph.addNodes( nodes )

    print "Adding connections"
    for device in topology:
        print "- ", device, " -> ", topology[device]["interfaces"]
        for localInterface in topology[device]["interfaces"].keys():
            #graph.addConnections(
            #print localInterface
            conn = (device+"."+localInterface, topology[device]["interfaces"][localInterface])
            graph.addConnections( [conn] )
            
    graph.generateOutput("test")
