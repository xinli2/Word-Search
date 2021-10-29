"""
    File: list_of_rows_0_on_top.py
    Author: Xin Li
    Purpose: This program deals with a list of lists. It's
    inner lists are rows. y=0 are the top of the grid.
"""
def build_rect(wid, hei):
    assert wid >= 3
    assert hei >= 3
    lst=[]
    data=[]
    lst.append(' ')
    for index in range(wid-2):
        lst.append('T')
    lst.append(' ')
    data.append(lst)

    for i in range(hei-1):
        if i >= 1:
            lst =[]
            for j in range (wid):
                if j<1:
                    lst.append('L')
                elif j>(wid-2):
                    lst.append('R')
                else:
                    lst.append('.')
            data.append(lst)

    lst= []
    lst.append(' ')
    for g in range(wid-2):
        lst.append('B')
    lst.append(' ')
    data.append(lst)

    return data


def print_rect(data):
    for i in range(len(data)):
        print()
        for k in range(len(data[i])):
            print(data[i][k],end='')
    print()


def update(data, x,y ,c):
    data[y][x] = c
