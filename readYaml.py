#
# from
#   https://stackoverflow.com/questions/14359557/reading-yaml-in-python


import yaml

def readYaml( filename ):
    stream = open(filename, "r")
    docs = yaml.load_all(stream)
    return docs


if __name__ == "__main__":
    docs = readYaml( "test/inputA.yml" )
    for doc in docs:
        for k,v in doc.items():
            print k, "->", v
        print "\n",
