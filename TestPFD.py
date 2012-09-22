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
import unittest

from PFD import pfd_read, pfd_eval, pfd_print#, pfd_solve

# -----------
# TestPFD
# -----------

class TestPFD (unittest.TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        al = []
        b = pfd_read(r, al)
        self.assert_(b     == True)
        self.assert_(al[3][1] == 1)
        self.assert_(al[3][5] == 1)
        self.assert_(al[2][5] == 1)
        self.assert_(al[2][3] == 1)
        self.assert_(al[4][3] == 1)
        self.assert_(al[5][1] == 1)
        self.assert_(al[0][0] == 0)
        self.assert_(al[3][2] == 0)
		
    def test_read_2 (self) :
        r = StringIO.StringIO("2 0\n")
        al = []
        b = pfd_read(r, al)
        self.assert_(b    ==  True)
        self.assert_(al[0][0] ==  0)
        self.assert_(al[1][1] ==  0)
		
    # def test_read_3 (self) :
        # r = StringIO.StringIO("1 1000000 1 10\n")
        # a = [0, 0]
        # b = pfd_read(r, a)
        # self.assert_(b    == True)
        # self.assert_(a[0] ==  1)
        # self.assert_(a[1] ==  1000000)

    # # ----
    # # eval
    # # ----
    
    def test_eval_1 (self) :
    
        adj_matrix = [([0] * (6))] * (6)
        adj_matrix[3][1] = 1
        adj_matrix[3][5] = 1
        adj_matrix[2][5] = 1
        adj_matrix[2][3] = 1
        adj_matrix[4][3] = 1
        adj_matrix[5][1] = 1
        
        ord_list = pfd_eval(adj_matrix)
        self.assert_(ord_list[0] == 1)
        self.assert_(ord_list[1] == 5)
        self.assert_(ord_list[2] == 3)                 
        self.assert_(ord_list[3] == 2)
        self.assert_(ord_list[4] == 4)                

    # def test_eval_2 (self) :
        # v = pfd_eval(100, 200, [0] * 1000000)
        # self.assert_(v == 125)

    # def test_eval_3 (self) :
        # v = pfd_eval(201, 210, [0] * 1000000)
        # self.assert_(v == 89)

    # # -----
    # # print
    # # -----

    # def test_print_1 (self) :
        # w = StringIO.StringIO()
        # pfd_print(w, 1, 10, 20)
        # self.assert_(w.getvalue() == "1 10 20\n")
		
    # def test_print_2 (self) :
        # w = StringIO.StringIO()
        # pfd_print(w, 100, 200, 125)
        # self.assert_(w.getvalue() == "100 200 125\n")
		
    # def test_print_3 (self) :
        # w = StringIO.StringIO()
        # pfd_print(w, 900, 1000, 174)
        # self.assert_(w.getvalue() == "900 1000 174\n")

    # # -----
    # # solve
    # # -----

    # def test_solve_1 (self) :
        # r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        # w = StringIO.StringIO()
        # pfd_solve(r, w)
        # self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
		
    # def test_solve_2 (self) :
        # r = StringIO.StringIO("5 5\n")
        # w = StringIO.StringIO()
        # pfd_solve(r, w)
        # self.assert_(w.getvalue() == "5 5 6\n")
		
    # def test_solve_3 (self) :
        # r = StringIO.StringIO("")
        # w = StringIO.StringIO()
        # pfd_solve(r, w)
        # self.assert_(w.getvalue() == "")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
