print ("Game of Life")

import sys
import time
import tkinter
from tkinter import *
import numpy as np
from scipy.sparse import csr_matrix

def count(arr, tup, d, x):
    if tup[0] >= 0 and tup[0] < d and tup[1] >= 0 and tup[1] < d :
        if arr[tup] == 1:
            x += 1
    return x

##row = [1,0,1,2,2]
##col = [0,2,2,1,2]
##data = [1,1,1,1,1]
##d = 5
##m = max(max(row), max(col)) + 1
##tup = [(1,0), (0,2), (1,2), (2,1), (2,2)]
##arr = csr_matrix((data, (row, col)), shape=(m,m)).toarray()

def count_neighbours(i, j, row, col, tup):
    c = 0
    
    neighbour = [(i-1, j-1), (i, j-1), (i+1, j-1), (i-1, j), (i+1, j), (i-1, j+1), (i, j+1), (i+1, j+1)]
    
    for n in range(len(neighbour)):
        if neighbour[n] in tup:
            c += 1
    return c

##c = count_neighbours(3, 3, row, col, tup)
##print(c)

def start_game():
    row = []
    col = []
    data = [1]
    
    while 1:
        r = input("Life Cell - row: ")
        if r == 'q': break
        else:
            row += [int(r)]
        c = input("Life Cell - col: ")
        if c == 'q': break
        else:
            col += [int(c)]

    d = len(row)
    data *= d
    m = max(max(row), max(col)) + 1
    arr = csr_matrix((data, (row, col)), shape=(m,m)).toarray()
    print(arr)
    tup_arr = []
    for i in range(len(row)):
            tup_arr.append((row[i],col[i]))
        
    g = 10
    generation(tup_arr, d, data, row, col, g)



def create_grid(live_tup, d, row, col):
    all_tup = []
    for i in range(d):
        for j in range(d):
            all_tup.append((i,j))

    for k in all_tup:
        if k in live_tup:
            t = 1
        else:
            t = 0
        Label(text=t, relief=RIDGE, width=5).grid(row=k[0], column=k[1])
    

    mainloop()


def generation(tup, d, data, row, col, g):
    print(tup)
    tup_del = []
    for i in range(d):
        for j in range(d):
            count = count_neighbours(i, j, row, col, tup)
            if count < 2 or count > 3:
                if (i,j) in tup:
                    tup_del.append((i,j))
                    
            if count == 3:
                tup.append((i,j))
                
    print(tup_del)
    print(tup)
    for n in tup_del:
        if n in tup:
            tup.remove(n)
            
    row = []
    col = []

    for n in tup:
        row.append(n[0])
        col.append(n[1])

    data = [1]*len(row)
    m = max(max(row), max(col)) + 1
    arr = csr_matrix((data, (row, col)), shape=(m,m)).toarray()
    print(arr)
    
    create_grid(tup, d, row, col)

    if g > 1:
        generation(tup, d, data, row, col, g-1)


start_game()
