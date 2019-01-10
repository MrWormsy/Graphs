# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:11:44 2019

@author: MrWormsy (AKA Antonin ROSA-MARTIN)
"""

from Idule import Idule

def main():
    
    print("Usage :")
    print(" ")
    print("GET test EXCLUDES a")
    print("GET http://www.google.com/test.txt CONTAINS money")
    print("STATS a UNION b DIFF c")
    print(" ")
    print(" ")
    
    myIdule = Idule()
    while(myIdule.getCommandLine()):
        print("")
    
    
if __name__ == "__main__":
    main() 