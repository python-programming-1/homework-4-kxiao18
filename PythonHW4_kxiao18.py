# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:58:03 2019

@author: Hui(karen) Xiao
"""
#Part 1
def iterateList(myList):
    formatted = ''
    for i in range(len(myList)-1):
        formatted += myList[i] + ', '
    formatted = formatted + 'and ' + myList[-1] + '.'
    return formatted


vegetables = ['carrot', 'lettuce', 'onion', 'radish']
iterateList(vegetables)        


#Part 2
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

gridResult= ''
for columns in range(6):
    for rows in range(9):
        gridResult += grid[rows][columns]
    print(gridResult)
    gridResult=''




