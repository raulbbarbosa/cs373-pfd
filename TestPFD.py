#!/usr/bin/env python

# -------------------------------
# projects/PFD/TestPFD.py
# Copyright (C) 2012
# Glenn P. Downing
# -------------------------------

"""
To test the program:
    % python TestPFD.py >& TestPFD.py.out
    % chmod ugo+x TestPFD.py
    % TestPFD.py >& TestPFD.py.out
"""

# -------
# imports
# -------

import StringIO
import heapq
import unittest

from PFD import pfd_read, pfd_eval, pfd_print, pfd_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        al = {}
        h = []
        td = {}
        b = pfd_read(r, al, h, td)
        self.assert_(b     == True)
        self.assert_(al[1] == [3, 5])
        self.assert_(al[2] == [])
        self.assert_(al[3] == [2, 4])
        self.assert_(al[4] == [])
        self.assert_(al[5] == [3, 2])
        
    def test_read_2 (self) :
        r = StringIO.StringIO("1 0\n")
        al = {}
        h = []
        td = {}
        b = pfd_read(r, al, h, td)
        self.assert_(b    ==  True)
        self.assert_(al[1] ==  [])
		
    def test_read_3 (self) :
        r = StringIO.StringIO("5 4\n2 1 1\n3 1 2\n4 1 3\n5 1 4\n")
        al = {}
        h = []
        td = {}
        b = pfd_read(r, al, h, td)
        self.assert_(b    == True)
        self.assert_(al[1] == [2])
        self.assert_(al[2] == [3])
        self.assert_(al[3] == [4])
        self.assert_(al[4] == [5])
        self.assert_(al[5] == [])
        
    def test_read_4 (self) :
        r = StringIO.StringIO("")
        al = []
        h = []
        td = {}
        b = pfd_read(r, al, h, td)
        self.assert_(b    == False)

    # # ----
    # # eval
    # # ----
    
    def test_eval_1 (self) :
        al= {}
        al[1] = [3, 5]
        al[2] = []
        al[3] = [2,4]
        al[4] = []
        al[5] = [3,2]
        td = {}
        td[1] = [0,1]
        td[2] = [2,2]
        td[3] = [2,3]
        td[4] = [1,4]
        td[5] = [1,5]
        heap = []    
        heapq.heappush(heap, td[1])
        heapq.heappush(heap, td[2])
        heapq.heappush(heap, td[3])
        heapq.heappush(heap, td[4])
        heapq.heappush(heap, td[5])
        ord_list = pfd_eval(al, heap, td)
        self.assert_(ord_list[0] == 1)
        self.assert_(ord_list[1] == 5)
        self.assert_(ord_list[2] == 3)                 
        self.assert_(ord_list[3] == 2)
        self.assert_(ord_list[4] == 4)                

    def test_eval_2 (self) :
        al= {}
        al[1] = []
        td = {}
        td[1] = [0,1]
        heap = []    
        heapq.heappush(heap, td[1])
        ord_list = pfd_eval(al, heap, td)
        self.assert_(ord_list[0] == 1)

    def test_eval_3 (self) :
        al= {}
        al[1] = [2]
        al[2] = [3]
        al[3] = [4]
        al[4] = [5]
        al[5] = []
        td = {}
        td[1] = [0,1]
        td[2] = [1,2]
        td[3] = [1,3]
        td[4] = [1,4]
        td[5] = [1,5]
        heap = []    
        heapq.heappush(heap, td[1])
        heapq.heappush(heap, td[2])
        heapq.heappush(heap, td[3])
        heapq.heappush(heap, td[4])
        heapq.heappush(heap, td[5])
        ord_list = pfd_eval(al, heap, td)
        self.assert_(ord_list[0] == 1)
        self.assert_(ord_list[1] == 2)
        self.assert_(ord_list[2] == 3)                 
        self.assert_(ord_list[3] == 4)
        self.assert_(ord_list[4] == 5)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        v = [1, 5, 3, 2, 4]
        pfd_print(w, v)
        self.assert_(w.getvalue() == "1 5 3 2 4\n\n")
		
    def test_print_2 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [])
        self.assert_(w.getvalue() == "")
		
    def test_print_3 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1])
        self.assert_(w.getvalue() == "1\n\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1, 2, 3, 4, 5])
        self.assert_(w.getvalue() == "1 2 3 4 5\n\n")

    # # -----
    # # solve
    # # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n\n")
		
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 0\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1\n\n")
		
    def test_solve_3 (self) :
        r = StringIO.StringIO("5 4\n2 1 1\n3 1 2\n4 1 3\n5 1 4\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3 4 5\n\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
