#!/usr/bin/env python

# ---------------------------
# projects/pfd/PFD.py
# Copyright (C) 2012
# Glenn P. Downing
# ---------------------------

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
    num_nodes = int(l[0])
    num_lines = int(l[1])
    assert num_nodes > 0
    assert num_lines >= 0
    
    # Initialize the adjacency matrix to the correct size (filled with 0's)
    adj_matrix += [[0 for i in range(num_nodes + 1)] for j in range(num_nodes + 1)]
    
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

def pfd_eval (adj_matrix) :
    """
    adj_matrix is the complete (likely unordered) adjacency matrix
    return the ordered list of nodes following the precedence rules
    """
    assert adj_matrix is not None
    
    ord_list = []
    nodes = len(adj_matrix)
    while len(ord_list) != (nodes - 1) :
        for node_index in range(1, nodes) :
            hasPred = False
            if node_index not in ord_list :
                for pred_index in range(1, nodes) :
                    if adj_matrix[node_index][pred_index] == 1 :
                        hasPred = True
                        break
                if not hasPred :
                    ord_list += [node_index]
                    for i in range(1, nodes) :
                        adj_matrix[i][node_index] = 0
                    break        
        
    assert ord_list is not None
    assert len(ord_list) == (nodes - 1) 
    
    return ord_list

# -------------
# pfd_print
# -------------

def pfd_print (w, v) :
    """
    prints the values in v
    w is a writer
    v is the ordered list of the tasks cast as strings
    """
    for i in range(0, len(v)) :
        if i != (len(v) - 1) :
            w.write(str(v[i]) + " ")
        else :
            w.write(str(v[i]) + "\n")

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read, eval, print
    r is a reader
    w is a writer
    """
    adj_matrix = []
    pfd_read(r, adj_matrix)
    v = pfd_eval(adj_matrix)
    pfd_print(w, v)
