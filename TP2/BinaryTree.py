# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:38:09 2018

@author: MrWormsy (AKA Antonin ROSA-MARTIN)
"""

import math
"""
A BinaryNode is made of a value, a leftNode and a rightNode which both are BinaryNodes
"""
class BinaryNode:
    
    #Constructor
    """
    Construct the BinaryNode from a value and a leftNode and a rightNode if needed
    __init__ : BinaryNode, int, BinaryNode, BinaryNode --> None
    """
    def __init__(self, value, leftNode = None, rightNode = None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        
    #Getters and Setters
    """
    Set the value of a BinaryNode
    setValue : BinaryNode, int --> Node
    """
    def setValue(self, value):
        self.value = value
        
    """
    Get the value from a BinaryNode
    getValue : BinaryNode --> int
    """    
    def getValue(self):
        return self.value
        
    """
    Set the leftNode of a BinaryNode
    setLeftNode : BinaryNode, BinaryNode --> None
    """
    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
        
    """
    Get the leftNode of a BinaryNode
    getLeftNode : BinaryNode --> BinaryNode
    """
    def getLeftNode(self):
        return self.leftNode
        
    """
    Set the rightNode of a BinaryNode
    serRightNode : BinaryNode, BinaryNode--> None
    """
    def setRightNode(self, rightNode):
        self.rightNode = rightNode
        
    """
    Get the rightNode of a BinaryNode
    getRightNode : BinaryNode --> BinaryNode
    """
    def getRightNode(self):
        return self.rightNode
    
    #Methods
    """
    Return True if the BinaryNode is a leaf (its rightNode and leftNode is None)
    isEmpty : BinaryNode --> boolean
    """
    def isEmpty(self):
        return (self.getLeftNode() == None) and (self.getRightNode() == None)
    
    """
    Display the Binary Node's value and its sub nodes' values
    display : BinaryNode --> None
    """
    def display(self, depth = 0):
        #We first print the value (justified is needed)
        print(" ")
        print(self.value.__str__().rjust(5 * depth))
        
        #If the tree is empty we can't go further
        if(self.isEmpty()):
            return
        
        #Then we do the recursion
        if(not self.getLeftNode() == None):
            self.getLeftNode().display(depth + 1)
        
        if(not self.getRightNode() == None):
            self.getRightNode().display(depth + 1)
        
    """
    Get the height of a tree
    getHeight : BinaryTree --> int
    """
    def getHeight(self):
        if(self == None):
            return 0
        else:
            maxL = 0
            maxR = 0
            
            if(not self.getLeftNode() == None):
                maxL = self.getLeftNode().getHeight()
            
            if(not self.getRightNode() == None):
                maxR = self.getRightNode().getHeight()
                
            if(maxR > maxL):
                return maxR + 1
            else:
                return maxL + 1
        
    """
    
    This methods returns true if the value exists in the node and its childrens, but this this for all the object !!!
    
    def exists(self, value):
        if(self.value == value):
            return True
        else:  
            if(not self.getLeftNode() == None and self.getRightNode() == None):
                return self.getLeftNode().exists(value)
            
            elif(not self.getRightNode() == None and self.getLeftNode() == None):
                return self.getRightNode().exists(value)
            
            elif(not self.getLeftNode() == None and not self.getRightNode() == None):
                return self.getLeftNode().exists(value) or self.getRightNode().exists(value)
            
        #If nothing has been returned at this point that is to say we value does not belong to the node and its childrens
        return False
    """ 
        
    
    """
    Know if a value in the tree exists
    exists : BinaryNode --> boolean
    """
    def exists(self, value, cpt = 0):
        if(self.value == value):
            return (True, cpt)
        elif(self.isEmpty()):
            return (False, cpt)
        
        
        #If the value of the root is less than the value we search in the leftNode and if the value of the root is greater than the value we search in the rightNode
        else:
            if(self.getValue() > value):
                
                #If the leftNode is not null we search if the value exists into it
                if(not self.getLeftNode() == None):
                    return self.getLeftNode().exists(value, cpt + 1)
                    
            else:
                #If the rightNode is not null we search if the value exists into it
                if(not self.getRightNode() == None):
                    return self.getRightNode().exists(value, cpt + 1)
                
        
        #If we reach this point the value does not exists
        return (False, cpt)
    
    """
    Get a tree from a list
    fromList : List --> BinartNode
    """
    def fromList(l):
        
        #We first sort the list
        sortedList = sorted(l)
        
        #Then we check what the lenght of the list is
        
        #If the lenght of the list is 0 that is to say this is nothing, thus we return None
        if(l.__len__() == 0):
            return None
        
        #If the lenght of the list is 1 that is to say this is a leaf, thus we return a Node with no childrens
        elif(l.__len__() == 1):
            return BinaryNode(l[0])
    

        #Else the lenght of the list is higher than 1 so we can do the classic thing    
        else:
            
            #We get the median value of this list
            median = sortedList[int(math.floor((l.__len__())/2))]
            #We split the list in two lists, one list before the mdian value and the other one after the median value
            newList = Utils.splitList(sortedList, median)
            
            #Then we return the BinaryNode made from the two lists, the left child is made of the values below the node value and the right one is made of the values higher than the node value
            return BinaryNode(median, BinaryNode.fromList(newList[0]), BinaryNode.fromList(newList[1]))
   
    
    """ I tried to do something using only the tree... But i did not succeed... Here is my code if you want to look at it    
    
    #Balance a tree, this method is only called when we add an element, making a double rotation (left then right)
    def balance(self):
        
        #Height part
        lHeight = 0
        if(not self.getLeftNode() == None):
            lHeight = self.getLeftNode().getHeight()
        
        hHeight = 0
        if(not self.getRightNode() == None):
            hHeight = self.getRightNode().getHeight()
            
        height = lHeight - hHeight
        
        #Here we can see if we need to balance the tree or not
        if(height <= -1 and height >= 1):
            if(height > 1):
                
                #Left rotation
                self = self.rotateRight()
                
            elif(height < 1):
                
                #Right rotation
                self = self.rotateLeft()
                
            
        #TODO KLNLZNOFUBZIUFBZ
        if(not self.getLeftNode() == None):
            self.getLeftNode().balance()
            
            
        if(not self.getRightNode() == None):
            self.getRightNode().balance()
                
                
        #If the tree is already balanced we return self
        return self     
    
    #Rotate the tree by the left
    def rotateLeft(self):
        temp = self.getRightNode()
        tree1 = BinaryNode(self.getValue(), self.getLeftNode(), temp.getLeftNode())
        tree2 = BinaryNode(temp.getValue(), tree1, temp.getRightNode())
        return tree2
        
        
    #Rotate the tree by the right
    def rotateRight(self):
        temp = self.getLeftNode()
        tree1 = BinaryNode(self.getValue(), temp.getRightNode(), self.getRightNode())
        tree2 = BinaryNode(temp.getValue(), temp.getLeftNode(), tree1)
        return tree2
    
    """
    
    """
    Add a node with the value as value (we assume that the node does not already exists)
    addNode : BinaryNode, int--> boolean
    """
    def addNode(self, value):
        
        if(self.getValue() == value):
            #We return false because we could not add it (already exists)
            return False
        
        #We first check the current value
        
        #If the node value is less than the value we want to put we go to the left side
        if(self.getValue() > value):
            #If the left node of the current node is null we add a new one with the value
            if(self.getLeftNode() == None):
                self.setLeftNode(BinaryNode(value))
                return True
                
            #Else we go deeper
            else:
                self.getLeftNode().addNode(value)
                
        #Otherwise the right side
        else:
            #If the right node of the current node is null we add a new one with the value
            if(self.getRightNode() == None):
                self.setRightNode(BinaryNode(value))
                return True
                
            #Else we go deeper
            else:
                self.getRightNode().addNode(value)
        
    #As i can't do the balance methods directly on the tree, I must convert the tree into a list and then recreate this tree only using the fromList method
    """
    Make a tree balanced
    balance : BinaryTree --> BinaryTree
    """
    def balance(self):
        
        #First we need to get the list from the tree and then return the tree from the list we just gathered
        l = self.toList()
        
        return BinaryNode.fromList(l)
        
    """
    Get the list made of the tree's values
    toList : BinaryTree --> List
    """
    def toList(self):
        
        if(self == None):
            return []
            
        lList = []
        rList = []
        
        if(not self.getLeftNode() == None):
            lList = self.getLeftNode().toList()
            
        if(not self.getRightNode() == None):
            rList = self.getRightNode().toList()
          
            
        theList = rList + lList
        theList.append(self.getValue())
        
        return theList    
        
"""
A binary tree is a BinaryNode
"""
class BinaryTree(BinaryNode):    
    #Constructor
    """
    Construct a BinaryTree
    __init__ : BinaryTree, int, BinaryNode, BinaryNode  --> None
    """
    def __init__(self, value, leftNode = None, rightNode = None):
        super().__init__(value, leftNode, rightNode)
        
    #Getters and Setters
    """
    Get the root of a BinaryTree
    getRoot : BinaryTree --> BinaryTree
    """
    def getRoot(self):
        return self
        
class Utils:
    
    
    """
    #Split the list on two, the first part before the value and the last part after the value
    splitList : List, int --> List
    """
    def splitList(l, value):
        l1 = []
        l2 = []
        
        flag = False
        
        for v in l:
            if(v == value):
                flag = True
            else:
                if(flag == False):
                    l1.append(v)
                else:
                    l2.append(v)
        return [l1, l2]
        
            
            
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            