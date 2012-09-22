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
        r = StringIO.StringIO("1 0\n")
        al = []
        b = pfd_read(r, al)
        self.assert_(b    ==  True)
        self.assert_(al[0][0] ==  0)
        self.assert_(al[1][1] ==  0)
		
    def test_read_3 (self) :
        r = StringIO.StringIO("5 4\n2 1 1\n3 1 2\n4 1 3\n5 1 4\n")
        al = []
        b = pfd_read(r, al)
        self.assert_(b    == True)
        self.assert_(al[0][0] ==  0)
        self.assert_(al[5][5] ==  0)
        self.assert_(al[2][1] ==  1)
        self.assert_(al[3][2] ==  1)
        self.assert_(al[4][3] ==  1)
        self.assert_(al[5][4] ==  1)
        self.assert_(al[4][2] ==  0)
        
    def test_read_4 (self) :
        r = StringIO.StringIO("")
        al = []
        b = pfd_read(r, al)
        self.assert_(b    == False)

    # # ----
    # # eval
    # # ----
    
    def test_eval_1 (self) :
        al= [[0 for i in range(6)] for j in range(6)]
        al[3][1] = 1
        al[3][5] = 1
        al[2][5] = 1
        al[2][3] = 1
        al[4][3] = 1
        al[5][1] = 1
        ord_list = pfd_eval(al)
        self.assert_(ord_list[0] == 1)
        self.assert_(ord_list[1] == 5)
        self.assert_(ord_list[2] == 3)                 
        self.assert_(ord_list[3] == 2)
        self.assert_(ord_list[4] == 4)                

    def test_eval_2 (self) :
        al= [[0 for i in range(2)] for j in range(2)]
        ord_list = pfd_eval(al)
        self.assert_(ord_list[0] == 1)

    def test_eval_3 (self) :
        al= [[0 for i in range(6)] for j in range(6)]
        al[2][1] = 1
        al[3][2] = 1
        al[4][3] = 1
        al[5][4] = 1
        ord_list = pfd_eval(al)
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
        self.assert_(w.getvalue() == "1 5 3 2 4\n")
		
    def test_print_2 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [])
        self.assert_(w.getvalue() == "")
		
    def test_print_3 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1])
        self.assert_(w.getvalue() == "1\n")
        
    def test_print_4 (self) :
        w = StringIO.StringIO()
        pfd_print(w, [1, 2, 3, 4, 5])
        self.assert_(w.getvalue() == "1 2 3 4 5\n")

    # # -----
    # # solve
    # # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("5 4\n3 2 1 5\n2 2 5 3\n4 1 3\n5 1 1\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 5 3 2 4\n")
		
    def test_solve_2 (self) :
        r = StringIO.StringIO("1 0\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1\n")
		
    def test_solve_3 (self) :
        r = StringIO.StringIO("5 4\n2 1 1\n3 1 2\n4 1 3\n5 1 4\n")
        w = StringIO.StringIO()
        pfd_solve(r, w)
        self.assert_(w.getvalue() == "1 2 3 4 5\n")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
