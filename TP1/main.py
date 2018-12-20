from RTree import RTree

def main():
    
    #We first create a RTree where rt0 is the root
    rt5 = RTree('n5')
    rt11 = RTree('n11')
    rt10 = RTree('n10', [rt11])
    rt4 = RTree('n4')
    rt3 = RTree('n3')
    rt2 = RTree('n2')
    rt7 = RTree('n7', [rt10])
    rt9 = RTree('n9')
    rt6 = RTree('n6', [rt7])
    rt8 = RTree('n8', [rt6])
    rt1 = RTree('n1', [rt4, rt5, rt8, rt9])
    rt0 = RTree('n0', [rt1, rt2, rt3])
    
    #Display the Depth
    print("\nDisplay through Depth")
    rt0.displayDepth()
    
    #Display the Width
    print("\nDisplay through Width")
    rt0.displayWidth()
    
    #Get the childrens
    print("\nGet the childrens")
    for children in rt0.getChildrens():
        print(children.getContent())
        
    #Get the father
    print("\nGet the father")
    print(rt0.getFather(rt1).getContent())

    #Get the descendents (childs, grand childs ect)
    print("\nGet the descendents")
    #Filter the RTree that are in more than once
    listToPrint = []
    for children in rt0.getDescending():
        if(children not in listToPrint):
            listToPrint.append(children)
            print(children.getContent())
    
    #Get the ascendents (father, grand father)
    print("\nGet the Ascendents")
    for fathers in rt0.getAscending(rt0.getRoot(), rt11):
        print(fathers.getContent())
        
    #Check if a RTree is a leaf or not
    print("\nKnow if this is a leaf")
    print(rt0.isLeaf())
    print(rt2.isLeaf())
    
    #Get the degree of a RTree
    print("\nGet the degree of the RTree")
    print(rt0.getDegree())
    
    """
    print("\nGet the Depth of the RTree")
    print(rt0.getDepth())
    """

if __name__ == "__main__":
    main()   