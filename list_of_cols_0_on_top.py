"""
    File: list_of_cols_0_on_top.py
    Author: Xin Li
    Purpose: This program deals with e inner lists are the columns
    .y = 0 is the top of the grid.
"""
def build_rect(wid, hei):
    assert wid >= 3
    assert hei >= 3
    lst=[]
    data=[]
    for i in range(wid):
        lst =[]
        for j in range (hei):
            if i < 1:
                if j < 1:
                    lst.append(' ')
                elif j>(wid-2):
                    lst.append(' ')
                else:
                    lst.append('L')
            elif i > wid-2:
                if j <1 :
                    lst.append(' ')
                elif j>(wid-2):
                    lst.append(' ')
                else:
                    lst.append('R')
            else:
                if j < 1:
                    lst.append('T')
                elif j>(wid-2):
                    lst.append('B')
                else:
                    lst.append('.')

        data.append(lst)


    return data


def print_rect(data):
    i = 0
    for k in range(len(data[i])):
        print()
        for i in range(len(data)):
            print(data[i][k],end='')

    print()


def update(data, x,y ,c):
    data[x][y] = c
