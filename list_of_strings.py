"""
    File: list_of_strings.py
    Author: Xin Li
    Purpose: This program deals with a A list of strings.
    Each string represents a single row of the grid, and
    y = 0 is the top of the grid.

"""
def build_rect(wid, hei):
    assert wid >= 3
    assert hei >= 3
    lst=[]
    data=[]
    string = ''
    lst.append(' ')
    for index in range(wid-2):
        lst.append('T')
    lst.append(' ')
    for k in lst:
        string += str(k)
    data.append(string)

    string = ''
    for i in range(hei-1):
        if i >= 1:
            lst =[]
            string=''
            for j in range (wid):
                if j<1:
                    lst.append('L')
                elif j>(wid-2):
                    lst.append('R')
                else:
                    lst.append('.')
            for k in lst:
                string += str(k)
            data.append(string)

    string=''
    lst= []
    lst.append(' ')
    for g in range(wid-2):
        lst.append('B')
    lst.append(' ')
    for k in lst:
        string += str(k)
    data.append(string)


    return data


def print_rect(data):
    for i in range(len(data)):
        print()
        for k in range(len(data[i])):
            print(data[i][k],end='')
    print()


def update(data, x,y ,c):
    string= ''
    for i in range(len(data)):
        if i==y:
            for k in range(len(data[i])):
                if k == x:
                    string += str(c)
                else:
                    string += str(data[i][k])
            data[i] = string
