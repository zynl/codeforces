#!/bin/python

queenList = [-1] * 8

#check before row is ok
def check(col, row):
    for tempCol in range(col):
        tempRow = queenList[tempCol]
        if tempRow == row or col + row == tempCol + tempRow or col - row == tempCol - tempRow:
            return False
    return True

flag = False
sum = 0

#find row for 8 cols
def Try(tempCol):
    global flag
    global sum
    if tempCol == 8:
        flag = True
    else:
        for i in range(8):
            if check(tempCol, i):   #if position is ok
                queenList[tempCol] = i
                Try(tempCol + 1)
            if flag == True:
                break

Try(0)
for i in range(8):
    for j in range(8):
        if i == queenList[j]:
            print('1', end = ' ')
        else:
            print('0', end = ' ')
    print()
