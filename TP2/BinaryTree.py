# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:38:09 2018

@author: anton
"""

import math

class BinaryNode:
    
    #Constructor
    def __init__(self, value, leftNode = None, rightNode = None):
        self.value = value
        self.leftNode = leftNode
        self.rightNode = rightNode
        
    #Getters and Setters
    def setValue(self, value):
        self.value = value
        
    def getValue(self):
        return self.value
        
    def setLeftNode(self, leftNode):
        self.leftNode = leftNode
        
    def getLeftNode(self):
        return self.leftNode
        
    def setRightNode(self, rightNode):
        self.rightNode = rightNode
        
    def getRightNode(self):
        return self.rightNode
    
    #Methods
    def isEmpty(self):
        return (self.getLeftNode() == None) and (self.getRightNode() == None)
    
    def display(self, depth = 0):
        #We first print the value (justified is needed)
        print(" ")
        print(self.value.__str__().rjust(5 * depth))
        
        
        if(self.isEmpty()):
            return
        
        #Then we do the recursion
        if(not self.getLeftNode() == None):
            self.getLeftNode().display(depth + 1)
        
        if(not self.getRightNode() == None):
            self.getRightNode().display(depth + 1)
        
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
        
    #Add a node with the value as value (we assume that the node does not already exists)
    def addNode(self, value):
        
        #First check if we can add the value
        pass
            
class BinaryTree(BinaryNode):    
    #Constructor
    def __init__(self, value, leftNode = None, rightNode = None):
        super().__init__(value, leftNode, rightNode)
        
    #Getters and Setters
    def getRoot(self):
        return self
        
class Utils:
    
    #Split the list on two, the first part before the value and the lasy part after the value
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
        
            
            
    
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            