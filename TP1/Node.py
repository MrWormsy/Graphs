class Node:
    
    """
    Node class that represents nodes in rooted tree
    
    A Node is composed of
        - A content which can be anything 
        - A list of Node (childrens)
    """
    
    def __init__(self, content, childrens = []):
        self.content = content
        self.childrens = childrens
    
    """
    Return the content of a Node
    getContent : Node --> Object
    """
    
    def getContent(self):
        return self.content
    
    """
    Return the childrens of a Node
    getChildrens : Node --> List of Node
    """
    
    def getChildrens(self):
        return self.childrens

        
        
    