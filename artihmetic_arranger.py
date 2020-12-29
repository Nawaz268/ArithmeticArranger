#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:20:49 2020

@author: nawaz
"""

def arithmetic_arranger(problems, needAnswer = False):
    #Situation 1 Error: More than 5 problems
    if len(problems) >5:
        return ("Error: Too many problems.")
    line1=line2=line3=line4= ''
    for i in problems:
        split_prob = i.split()
        num1 = split_prob[0]
        operator=split_prob[1]
        num2 = split_prob[2]
        if (operator!='+' and operator!='-'):
            print("Error: Operator must be '+' or '-'.")
        if num1.isdigit() == 0 or num2.isdigit()== 0:
            print("Error: Numbers must only contain digits.")
        else:
            if len(num1)>4 or len(num1)>4:
                print("Error: Numbers cannot be more than four digits.")
                break
        space = max(len(num1), len(num2))

        line1 += num1.rjust(space + 2)
        line2 += operator + ' ' + num2.rjust(space)
        line3 += '-' * (space + 2)
        print(line1)
        print(line2)
        print(line3)
        """
        if needAnswer == False:
            if operator == '+':
                line4 += str(num1 + num2).rjust(space + 2)
            else:
                line4 += str(num1 - num2).rjust(space + 2)

         """   
        
    """
    #2 Checking correct operators
    correctOperators = "+" or "/"
    for i in range(0, len(problems)):
        if !=correctOperators in problems[i]:
            print("Wrong!")
    
    """
    
    
    


(arithmetic_arranger(["1234 + 698", "2 - 2", "45 + 43", "123 + 49"]))