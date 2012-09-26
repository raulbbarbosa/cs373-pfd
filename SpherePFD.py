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
import heapq

REMOVED = True

# ------------
# pfd_read
# ------------

def pfd_read (r, adj_matrix, heap, tuple_dict) :
    """
    reads and interprets the rules from the input into the adjacency matrix
    r is a reader
    adj_matrix is a list
    return true if the read succeeds, false otherwise
    """
    s = r.readline()
    if s == "" :
        return False
    elif s == "\n" :
        return pfd_read(r, adj_matrix, heap, tuple_dict)
    l = s.split()
    num_nodes = int(l[0])
    num_lines = int(l[1])
    assert num_nodes > 0
    assert num_lines >= 0
    
    # Initialize the adjacency matrix to the correct size (filled with 0's)
    adj_matrix += [[0 for i in range(num_nodes + 1)] for j in range(num_nodes + 1)]
    free_node = [1 for i in range(num_nodes + 1)]
        		 
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
        tuple_dict[node] = [num_pred, node]       	
        heapq.heappush(heap, tuple_dict[node])
        free_node[node] = 0
        for j in range(2, num_pred + 2) :
            pred_node = int(l[j])
            adj_matrix[node][pred_node] = 1
    
    for i in range(1, num_nodes + 1) :
        if free_node[i] == 1 :
            tuple_dict[i] = [0, i]
            heapq.heappush(heap, tuple_dict[i])
            # free_node[node] = 0
           
    return True

# ------------
# pfd_eval
# ------------

def pfd_eval (adj_matrix, heap, tuple_dict) :
    """
    adj_matrix is the complete (likely unordered) adjacency matrix
    return the ordered list of nodes following the precedence rules
    """
    assert adj_matrix is not None
    
    ord_list = []
    nodes = len(adj_matrix)
    while True :
        try :
            current_node = heapq.heappop(heap)
            if current_node[-1] is REMOVED : continue
        except IndexError:
            break
        node_index = current_node[1]
        ord_list += [node_index]
        for i in range(1, nodes) :
            if adj_matrix[i][node_index] == 1 :
                #tuple_dict[i][0] -=  1
                tuple_dict[i][-1] = REMOVED
                tuple_dict[i] = [tuple_dict[i][0]-1, i]
                heapq.heappush(heap, tuple_dict[i])            
         
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
            w.write(str(v[i]) + "\n\n")

# -------------
# pfd_solve
# -------------

def pfd_solve (r, w) :
    """
    read, eval, print
    r is a reader
    w is a writer
    """
    while True :
        adj_matrix = []
        heap = []
        tuple_dict = {}
        if not pfd_read(r, adj_matrix, heap, tuple_dict) :
            break
        v = pfd_eval(adj_matrix, heap, tuple_dict)
        pfd_print(w, v)
    
# ----
# main
# ----

pfd_solve(sys.stdin, sys.stdout)
