"""
    File: list_of_rows_0_on_bottom.py
    Author: Xin Li
    Purpose: This program deals with a A list of lists, where
    the inner lists are the rows. y = 0 is the bottom of the
    grid.
"""
def build_rect(wid, hei):
    assert wid >= 3
    assert hei >= 3
    new_data=[]
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

    for k in range(len(data)-1,-1,-1):
        new_data.append(data[k])


    return new_data


def print_rect(data):
    for i in range(len(data)):
        print()
        for k in range(len(data[i])):
            print(data[len(data)-1-i][k],end='')
    print()


def update(data, x,y ,c):
    data[y][x] = c
