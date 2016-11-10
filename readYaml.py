'''
from
  https://stackoverflow.com/questions/14359557/reading-yaml-in-python
'''

import yaml

def readYaml( filename ):
    stream = open(filename, "r")
    docs = yaml.load(stream)
    return docs


if __name__ == "__main__":
    docs = readYaml( "test/inputA.yml" )
    for doc in docs:
        print doc, " -> ", docs[doc]
