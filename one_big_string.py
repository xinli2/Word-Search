"""
    File: one_big_string.py
    Author: Xin Li
    Purpose: This program deals with a single string which
    mixed with newlines. So, print, produces a grid.
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
    string = ''
    for e in data:
        string += str(e) +'\n'
    return string


def print_rect(data):
    print(data)


def update(data, x, y ,c):
    lst = [data]
    lst=lst.split('\n')
    string = ''
    data = ''
    for i in range(len(lst)):
        if i==y:
            for k in range(len(lst[i])):
                if k == x:
                    string += str(c)
                else:
                    string += str(lst[i][k])
            lst[i] = string

    for s in lst:
        data += str(s)+'\n'
