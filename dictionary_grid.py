"""
    File: dictionary_grid.py
    Author: Xin Li
    Purpose: This program deals with a dictionary, where the
    keys are (x,y) tuples, and the values are the characters.
    In this progeam, y=0 is the top of the grid.
"""
def build_rect(wid, hei):
    assert wid >= 3
    assert hei >= 3
    lst=[]
    data=[]
    new_data ={}
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

    for y in range(len(data)):
        for x in range(len(data[y])):
            new_data[(x,y)] = data[y][x]


    return new_data


def print_rect(data):
    lst_x=[]
    lst_y=[]
    for key in data:
        if isinstance(key,tuple)==True:
            lst_x.append(key[0])
            lst_y.append(key[1])

    for k in range(len(lst_y)):
        print()
        for i in range(len(lst_x)):
            print(data[(i,k)],end='')
    print()


def update(data, x,y ,c):
    lst_x=[]
    lst_y=[]
    for key in data:
        if isinstance(key,tuple)==True:
            lst_x.append(key[0])
            lst_y.append(key[1])
    if x in lst_x:
        if y in lst_y:
            data[(x,y)] = c
