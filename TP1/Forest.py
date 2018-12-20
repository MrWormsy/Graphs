class Forest():

    """
    A Forest is represented as a list of RTree
    """

    def __init__(self, content):
        self.rTrees = content
    
    """
    Return true if the Forest is empty
    isEmpty : Forest --> boolean
    """
    
    def isEmpty(self):
        if (self.rTrees == []):
            return True
        else:
            return False
        
    """
    Return the first RTree from a Forest
    getFirstRTree : Forest --> RTree
    """
        
    def getFirstRTree(self):
        return self.rTrees[0]
    
    """
    Return all the RTRee of a Forest except the first one
    getRest : Forest --> List of RTree
    """
    
    def getRest(self):
        rest = self.rTrees
        rest.pop(0)
        return rest
    
    
    """
    Print the content of a Forest using depth algorithm
    displayDepth : Forest --> void
    """
    
    def displayDepth(self):
        # do nothing if the forest is empty
        if self.isEmpty():
            return
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree().getRoot()
            
            #We print the content
            print(n.getContent())
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            
            #build the new forest for depth first
            f = Forest(st + r)
            
            # call the coresponding method on the forest
            return f.displayDepth()
    
    """
    Print the content of a Forest using width algorithm
    displayWidth : Forest --> void
    """
        
    def displayWidth(self):
        # do nothing if the forest is empty
        if self.isEmpty():
            return
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree().getRoot()
            
            #We print the content
            print(n.getContent())
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            
            #build the new forest for depth first
            f = Forest(r + st)
            
            # call the coresponding method on the forest
            return f.displayWidth()
        
    """
    Return the father of a given Forest
    getFatherOfTree : Forest, RTree --> RTree
    """
    def getFatherOfTree(self, tree):
        if self.isEmpty():
            return
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree().getRoot()
            
            #If the tree we are looking for is in the list of childrens of the current tree, we return it
            if (tree in n.getChildrens()):
                return n
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            
            #build the new forest for depth first
            f = Forest(st + r)
            
            # call the coresponding method on the forest
            return f.getFatherOfTree(tree)
        
    """
    Return a list of RTree of a given Forest which are all the childs, grand childs ect
    getDescending : Forest --> List of RTree
    """
    def getDescending(self):
        if self.isEmpty():
            return []
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree().getRoot()
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            
            #build the new forest for depth first
            f = Forest(st + r)
            
            # call the coresponding method on the forest
            return f.getDescending() + n.getChildrens()
    
    """
    Return a list of fathers of a given Forest which are the father, grand father ect
    getAscending : Forest, RTree, RTree --> List of RTree
    """
    def getAscending(self, root, tree):
        if self.isEmpty():
            return []
        else:
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()

            # get the rest of the forest: the forest without the first tree
            r = self.getRest()

            #build the new forest for depth first
            f = Forest(st + r)
            
            # call the coresponding method on the forest
            if (root.getFather(tree) != None):
                return f.getAscending(root, root.getFather(tree)) + [root.getFather(tree)]
            else:
                return []


    """
    Return the degree of a given Forest
    getDegree : Forest --> int
    """            
    def getDegree(self):
        if self.isEmpty():
            return 0
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree().getRoot()
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            
            #build the new forest for depth first
            f = Forest(st + r)
                    
            df  = f.getDegree()
            
            #If the degree of the forest is greater than the degree of the current RTree we return df, else we return the degree of the current RTree
            if (n.getChildrens().__len__() <= df):
                return df
            else:
                return n.getChildrens().__len__()
            
    """
    
    TODO
    
            
    def getDepth(self):
        # do nothing if the forest is empty
        if self.isEmpty():
            return 0
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree()
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            #build the new forest for depth first
            f = Forest(st + r)
            
            fdd = f.getDepth()
            fdn = Forest(r).getDepth()
            
            print(n.getContent(), fdd, fdn)
            
            if (fdd < fdn):
                return fdn + 1
            else:
                return fdd + 1
            
    def getWidth(self):
        # do nothing if the forest is empty
        if self.isEmpty():
            return 0
        else:
            # get the current node: the root of the first tree of the forest
            n = self.getFirstRTree()
            
            # get the sub tree of the first tree of the forest
            st = self.getFirstRTree().getSubTree()
            # get the rest of the forest: the forest without the first tree
            r = self.getRest()
            #build the new forest for depth first
            f = Forest(r + st)
            
            fwd = f.getDepth()
            fwn = Forest(r).getDepth()
            
            print(n.getContent(), fwd, fwn)
            
            if (fwd < fwn):
                return fwn + 1
            else:
                return fwd + 1
            
    """
            
        
        
        
        
        