# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 08:13:45 2019

@author: MrWormsy (AKA Antonin ROSA-MARTIN)
"""

import ply.lex as lex
import ply.yacc as yacc

#GET http://www.t.t/t.t CONTAINS slt

class Idule:

    def __init__(self):
        tokens = ['GET', 'CONTAINS', 'EXCLUDES', 'AND', 'OR', 'URI', 'VARIABLE', 'STATS', 'UNION', 'INTERSECT', 'DIFF']
        t_ignore = ' \t'
        t_GET = 'GET'
        t_CONTAINS = 'CONTAINS'
        t_EXCLUDES = 'EXCLUDES'
        t_AND = 'AND'
        t_OR = 'OR'
        t_STATS = 'STATS'
        t_UNION = 'UNION'
        t_INTERSECT = 'INTERSECT'
        t_DIFF = 'DIFF'
        t_URI = r'(http:\/\/)(www)[\.][a-z0-9]+[\.][a-z0-9]+([\/][a-z0-9]+)*[\.][a-z0-9]+'
        t_VARIABLE = r'(?!http:\/\/)[a-z0-9]+'
        
        
        self.lex = lex.lex() #Build the lexer
        
        def p_idule(p):
            '''
            idule : getall
                  | statall
            '''
            print("Your syntaxe is correct")
            
        def p_statall(p):
            '''
            statall : STATS VARIABLE uid VARIABLE
                    | STATS VARIABLE uid uids VARIABLE
            '''
        def p_uids(p):
            '''
            uids : VARIABLE uid
                 |
            '''
        
        def p_uid(p):
            '''
            uid : UNION
                | INTERSECT
                | DIFF
            '''
        
        def p_getall(p):
            '''getall : GET from constraint VARIABLE constraints'''
            
        def p_from(p):
            '''
            from : URI
                 | VARIABLE
            '''
            
        def p_constraint(p):
            '''
            constraint : CONTAINS 
                       | EXCLUDES
            '''
        
        def p_constraints(p):
            '''
            constraints : andor VARIABLE constraints
                        |
            '''
        
        def p_andor(p):
            '''
            andor : AND
                  | OR
            '''
        
        self.yacc = yacc.yacc()
        
    
    def getCommandLine(self):
        theInput = input(">> ")
        if(not theInput == "EXIT"):
            self.lex.input(theInput)
            try:
                while True:
                    tok = self.lex.token() #lecture du prochain token ou none    
                    if not tok: break
            except:
                print("ERROR, a word is not correct in the sentence \"", theInput, "\"")
                return True
            try:
                self.yacc.parse(theInput)
            except:
                print("ERROR, a word is illegal")
                return True
            
            return True
        else:
            return False
            

        