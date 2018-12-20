from Node import Node
from Forest import Forest

class RTree(Node):
    
    """
    A RTree is represented by its root Node
    """
    def __init__(self, labels, sub_RTree = []):
        super().__init__(labels, sub_RTree)

    """
    Return the root of a given RTree
    getRoot : RTree --> RTree
    """
        
    def getRoot(self):
        return self
    
    """
    Return the subTrees of a given RTree
    getRoot : RTree --> List of RTree
    """
    
    def getSubTree(self):
        return self.getChildrens()
    
    """
    Return True if the given RTree is empty
    isEmpty : RTree --> boolean
    """
    
    def isEmpty(self):
        if (self.content == None):
            return True
        else:
            return False
    
    """
    Return the father of a given RTree
    getFather : RTree, RTree --> RTree
    """
    
    def getFather(self, tree):
        if (self.isEmpty()):
            return
        else:
            
            f = Forest([self])
            
            return f.getFatherOfTree(tree)
    
    """
    Print the content of a RTree using depth algorithm
    displayDepth : RTree --> void
    """
    def displayDepth(self):
        # do nothing if the rooted tree is empty
        if self.isEmpty():
            return
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.displayDepth()
        
    """
    Print the content of a RTree using width algorithm
    displayWidth : RTree --> void
    """
    def displayWidth(self):
        # do nothing if the rooted tree is empty
        if self.isEmpty():
            return
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.displayWidth()
    
    """
    Return a list of RTree of a given RTree which are all the childs, grand childs ect
    getDescending : RTree --> List of RTree
    """
    def getDescending(self):
        if self.isEmpty():
            return []
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.getDescending()
        
        
    """
    Return a list of fathers of a given Rtree which are the father, grand father ect
    getAscending : RTree, RTree, RTree --> List of RTree
    """
    def getAscending(self, root, tree):
        if self.isEmpty():
            return []
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.getAscending(root, tree)
      
    """
    Return True if the given RTree is a leaf
    isLeaf : Rtree --> boolean
    """
    def isLeaf(self):
        return self.getChildrens() == []
    
    
    """
    Return the degree of a given RTree
    getDegree : Rtree --> int
    """ 
    def getDegree(self):
        if self.isEmpty():
            return 0
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.getDegree()
        
        
    """
        
    def getDepth(self):
        if self.isEmpty():
            return 0
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.getDepth()
        
    def getWidth(self):
        if self.isEmpty():
            return 0
        else:
            # transform the rooted tree in forest
            f = Forest([self])
            # call the coresponding method on the forest
            return f.getWidth()
    
    """
    
    
    