#!/usr/bin/env python

# ---------------------------
# projects/pfd/PFD.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

# ------------
# pfd_read_f2
# ------------
def pfd_read_f2 (r, a) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a = [0, 0]
    a[0] = int(l[0]) ## number of nodes
    a[1] = int(l[1]) ## number of lines
    assert a[0] > 0
    assert a[1] > 0
    return True
    
# --------------
# pfd_read_line
# --------------
def pfd_read_line (r, adj_matrix) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    
    no  

# ------------
# pfd_read
# ------------

def pfd_read (r, adjacency_list) :
    """
    reads two ints into a[0] and a[1]
    r is a  reader
    a is an array of int
    return true if that succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    a = [0, 0]
    a[0] = int(l[0]) ## number of nodes
    a[1] = int(l[1]) ## number of lines
    assert a[0] > 0
    assert a[1] > 0
    
    internal_list = [0] * (a[0]+1)
    adjacency_list = [internal_list] * (a[0]+1)
    
    ##we have to read a[1] lines
    for i in range(a[1]) :
           
        s = r.readline()
        if s == "" :
            return False
        l = s.split()
        node = l[0]   
        n_predec = l[1]
        
        for j in range(2,n_predec+2) :
            node_to = l[j] 
            adjacency_list[node][node_to] = 1
           
    return True

# ------------
# pfd_eval
# ------------

def pfd_eval (i, j, c) :
    """
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    c is the cache for previously calculate cycle lengths
    return the max cycle length in the range [i, j]
    """
    assert i > 0
    assert j > 0
    # <Your code goes here>
    assert high > 0
    return high

# -------------
# pfd_print
# -------------

def pfd_print (w, i, j, v) :
    """
    prints the values of i, j, and v
    w is a writer
    i is the beginning of the range, inclusive
    j is the end       of the range, inclusive
    v is the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read, eval, print loop
    r is a reader
    w is a writer
    """
    
    adjacent_list = []
    collatz_read(r, adjacent_list) :
        v = collatz_eval()
        collatz_print(w, )
        
