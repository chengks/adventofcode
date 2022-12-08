from File import File
from Node import Node
import re

input = []
with open("input.txt") as file:
    while (line := file.readline().rstrip()):
        input.append(line)

regexCd = re.compile(r'^\$ cd ([a-z\./]+)$', flags=re.IGNORECASE)
regexDir = re.compile(r'^dir ([a-z]+)', flags=re.IGNORECASE)
regexFile = re.compile(r'^([0-9]+) ([a-z\.]+)', flags=re.IGNORECASE)
regexLs = re.compile(r'^\$ ls$', flags=re.IGNORECASE)

tree = Node(_name = "/", _parent=None, _files=[], _children=[] )
currentNode = tree

def runCd(path):
    global currentNode
    if path[0] == "..":
        currentNode = currentNode.parent
        return
    
    for c in currentNode.children:
        if c.name == path[0]:
            currentNode = c
    
def runDir(dir):
    node = None
    if len(currentNode.children) > 0: 
        for n in currentNode.children:
            node = n if n.name == dir[0] else None
    
    if node == None:
        currentNode.children.append(Node(_name = dir[0], _parent = currentNode, _files=[], _children=[]))

def runFile(file_info):
    currentNode.files.append(File(file_info[0][1], int(file_info[0][0])))

for ip in input:
    if regexCd.search(ip):
        runCd(regexCd.findall(ip))
    
    if regexDir.search(ip):
        runDir(regexDir.findall(ip))
    
    if regexFile.search(ip):
        runFile(regexFile.findall(ip))

def calculateNodeSize(node) -> int:
    for n in node.children:
        node.size += calculateNodeSize(n)
        
    totalSize = 0
            
    for f in node.files:
        totalSize += f.size
     
    node.size += totalSize
    return node.size

def findAnswer(node, spaceNeeded, spacesAvailableToDelete) -> int:
    if node.size > spaceNeeded:
        spacesAvailableToDelete.append(node.size)

    for n in node.children:
        findAnswer(n, spaceNeeded, spacesAvailableToDelete)
    
    return sorted(spacesAvailableToDelete)[0]

calculateNodeSize(tree)
spaceNeeded = 30000000 - (70000000 - tree.size)
print(findAnswer(tree, spaceNeeded, []))