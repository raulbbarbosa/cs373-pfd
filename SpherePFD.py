#!/usr/bin/env python

# ------------------------------
# projects/pfd/SpherePFD.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To run the program
    % python SpherePFD.py < RunPFD.in > RunPFD.out
    % chmod ugo+x SpherePFD.py
    % SpherePFD.py < RunPFD.in > RunPFD.out

To document the program
    % pydoc -w PFD
"""

# -------
# imports
# -------

import sys

# ------------
# pfd_read
# ------------

def pfd_read (r, adj_matrix) :
    """
    reads and interprets the rules from the input into the adjacency matrix
    r is a reader
    adj_matrix is a list
    return true if the read succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    l = s.split()
    num_nodes = int(l[0]) ## number of nodes
    num_lines = int(l[1]) ## number of lines
    assert num_nodes > 0
    assert num_lines >= 0
    
    # Initialize the adjacency matrix to the correct size (filled with 0's)
    internal_list = [0] * (num_nodes + 1)
    adj_matrix += [internal_list] * (num_nodes + 1)
    
    # Read num_lines lines to generate an adjacency matrix of "rules"
    for i in range(num_lines) :
        s = r.readline()
        if s == "" :
            return False
        l = s.split()
        node = int(l[0])
        num_pred = int(l[1])
        assert node > 0
        assert num_pred > 0
        for j in range(2, num_pred + 2) :
            pred_node = int(l[j])
            adj_matrix[node][pred_node] = 1
           
    return True

# ------------
# pfd_eval
# ------------

# def pfd_eval (adj_matrix) :
    # """
    # adj_matrix is the complete (likely unordered) adjacency matrix
    # return the ordered list of nodes following the precedence rules
    # """
    # assert 
    # # <Your code goes here>
    # assert 
    # return ord_list

# -------------
# pfd_print
# -------------

def pfd_print (w, v) :
    # """
    # prints the values in v
    # w is a writer
    # v is the ordered list of the tasks cast as strings
    # """
    w.write(" ".join(v) + "\n")

# -------------
# pfd_solve
# -------------

# def pfd_solve (r, w) :
    # """
    # read, eval, print
    # r is a reader
    # w is a writer
    # """
    
    # adj_matrix = []
    # pfd_read(r, adj_matrix)
    # v = pfd_eval(adj_matrix)
    # pfd_print(w, v)

# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)
