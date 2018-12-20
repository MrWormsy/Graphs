# -*- coding: utf-8 -*-
"""
Created on Wed Dec 19 13:34:46 2018

@author: anton
"""

from BinaryTree import BinaryNode
from BinaryTree import BinaryTree

def main():
    
    """
    
    #Test de construction d'un ABR
    n10 = BinaryTree.BinaryNode(10)
    n9 = BinaryTree.BinaryNode(9)
    n8 = BinaryTree.BinaryNode(8, n9, n10)
    
    n7 = BinaryTree.BinaryNode(7)
    n6 = BinaryTree.BinaryNode(6)
    n5 = BinaryTree.BinaryNode(5, n6, n7)
    
    n4 = BinaryTree.BinaryNode(4, n5, n8)
    
    
    n110 = BinaryTree.BinaryNode(110)
    n19 = BinaryTree.BinaryNode(19)
    n18 = BinaryTree.BinaryNode(18, n19, n110)
    
    n17 = BinaryTree.BinaryNode(17)
    n16 = BinaryTree.BinaryNode(16)
    n15 = BinaryTree.BinaryNode(15, n16, n17)
    
    n14 = BinaryTree.BinaryNode(14, n15, n18)
    
    #We create the binary tree from all the binary nodes
    tree = BinaryTree.BinaryTree(0, n4, n14)
    """
    
    #Test de construction d'un ABR de recherche
    #(0, 1, 3, 5, 6, 9)
    
    n0 = BinaryNode(0)
    n1 = BinaryNode(1, n0, None)
    n5 = BinaryNode(5)
    n3 = BinaryNode(3, n1, n5)
    
    n9 = BinaryNode(9)    
    
    tree = BinaryTree(6, n3, n9)
    
    
    #We display the tree
    tree.display()
    
    #List 
    theList = [5,3,6,9,1, 14, 15 ,18 ,12, 24, 87, 45, 14, 15, 25,26,27,28,29,30,31,32,32,34,35,36,37]
    
    #Print the list
    print("\n",theList, "\n")
    
    #Check if a value exists in the given tree
    numberOfAttempts = 36
    for i in range(0, numberOfAttempts):
        print("Research of", i, "(The first value is the result and the second the number of iterations/recursions):")
        print("Binary tree research:", tree.exists(i))
        print("List research:", existsInList(theList, i))
        print(" ")
      
    binaryTreeAverage = 0
    listAverage = 0 
    for i in range(0, numberOfAttempts):
        binaryTreeAverage += tree.exists(i)[1]
        listAverage += existsInList(theList, i)[1]
    
    print("The average for the Binary tree is :", binaryTreeAverage/numberOfAttempts) #Si on avait N valeurs la moyenne tendrait vers ln(N)
    print("The average for the List is :", listAverage/numberOfAttempts) #Si on avait N valeurs la moyenne tendrait vers N/2
    
    newTree = BinaryNode.fromList(theList)
    
    print("\n\n")
    
    newTree.display()
    
    
    
def existsInList(l, value):
    cpt = 0
    for e in l:
        if(e == value):
            return (True, cpt)
        cpt += 1
    return (False, cpt)


if __name__ == "__main__":
    main()