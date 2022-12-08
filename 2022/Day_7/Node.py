class Node:    
    def __init__(self, _name, _parent, _files, _children):
        self.name = _name
        self.files = _files
        self.parent = _parent
        self.children = _children
        self.size = 0