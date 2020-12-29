#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 22:20:49 2020

@author: nawaz
"""

def checker(problems):
    if len(problems) >5:
        return ("Error: Too many problems.")
    for i in problems:
        split_prob = i.split()
        num1 = split_prob[0]
        operator=split_prob[1]
        num2 = split_prob[2]
        if (operator!='+' and operator!='-'):
            return ("Error: Operator must be '+' or '-'.")
        if num1.isdigit() == 0 or num2.isdigit()== 0:
            return ("Error: Numbers must only contain digits.")
        if len(num1)>4 or len(num1)>4:
            return("Error: Numbers cannot be more than four digits.")
    return "No Issues Found"
    
def arithmetic_arranger(problems, needAnswer = False):
    #If more than 5 problems
    if len(problems) >5:
        return ("Error: Too many problems.")
    line1=line2=line3=line4= ""
    start = True
    side_space = "    "
    exp = checker(problems)
    print (exp)
    #If checker function and previous length check did not throw up any errors
    if exp == "No Issues Found":
        for i in problems:
            #Split the string into its individual bit for every iteration of every problem
            split_prob = i.split()
            num1 = split_prob[0]
            operator=split_prob[1]
            num2 = split_prob[2]
            
            #Count the max space required based on max of either the top or bottom for addition or subtraction
            space = max(len(num1), len(num2))
            num1_int = int(num1)
            num2_int = int(num2)
            #For the first equation
            if start == True:
                   line1 += num1.rjust(space + 2)
                   line2 += operator + ' ' + num2.rjust(space)
                   line3 += '-' * (space + 2)
                   if needAnswer == True:
                       if operator == '+':
                           line4 += str(num1_int + num2_int).rjust(space + 2)
                       else:
                           line4 += str(num1_int - num2_int).rjust(space + 2)
                   start = False
            # For the second and next iterations
            else:
                line1 += num1.rjust(space + 6)
                line2 += operator.rjust(5) + ' ' + num2.rjust(space)
                line3 += side_space + '-' * (space + 2)
                if needAnswer == True:
                    if operator == '+':
                        line4 += side_space + str(num1_int + num2_int).rjust(space + 2)
                    else:
                        line4 += side_space + str(num1_int - num2_int).rjust(space + 2)
        else:
            return exp
        #If the flag is True which means arithmetic calculation takes place
        if needAnswer == True:
            return( line1 + '\n' + line2 + '\n' + line3 + '\n' + line4)
        return( line1 + '\n' + line2 + '\n' + line3)

print(arithmetic_arranger(["1234 + 698X", "2000 - 2", "45 + 43", "123 + 49"], True))