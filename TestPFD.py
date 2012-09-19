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

from PFD import PFD_read, PFD_eval, PFD_print, PFD_solve

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
        b = PFD_read(r, al)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] == 10)
		
    def test_read_2 (self) :
        r = StringIO.StringIO("")
        a = [0, 0]
        b = PFD_read(r, a)
        self.assert_(b    == False)
        self.assert_(a[0] ==  0)
        self.assert_(a[1] ==  0)
		
    def test_read_3 (self) :
        r = StringIO.StringIO("1 1000000 1 10\n")
        a = [0, 0]
        b = PFD_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  1000000)
		
    def test_read_4 (self) :
        r = StringIO.StringIO("1 1000000\n")
        a = [0, 0]
        b = PFD_read(r, a)
        self.assert_(b    == True)
        self.assert_(a[0] ==  1)
        self.assert_(a[1] ==  1000000)

    # ----
    # eval
    # ----
    
    def test_eval_1 (self) :
        v = PFD_eval(1, 10, [0] * 1000000)
        self.assert_(v == 20)

    def test_eval_2 (self) :
        v = PFD_eval(100, 200, [0] * 1000000)
        self.assert_(v == 125)

    def test_eval_3 (self) :
        v = PFD_eval(201, 210, [0] * 1000000)
        self.assert_(v == 89)

    def test_eval_4 (self) :
        v = PFD_eval(900, 1000, [0] * 1000000)
        self.assert_(v == 174)
		
    def test_eval_5 (self) :
        v = PFD_eval(5, 5, [0] * 1000000)
        self.assert_(v == 6)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO.StringIO()
        PFD_print(w, 1, 10, 20)
        self.assert_(w.getvalue() == "1 10 20\n")
		
    def test_print_2 (self) :
        w = StringIO.StringIO()
        PFD_print(w, 100, 200, 125)
        self.assert_(w.getvalue() == "100 200 125\n")
		
    def test_print_3 (self) :
        w = StringIO.StringIO()
        PFD_print(w, 900, 1000, 174)
        self.assert_(w.getvalue() == "900 1000 174\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO.StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")
		
    def test_solve_2 (self) :
        r = StringIO.StringIO("5 5\n")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "5 5 6\n")
		
    def test_solve_3 (self) :
        r = StringIO.StringIO("")
        w = StringIO.StringIO()
        PFD_solve(r, w)
        self.assert_(w.getvalue() == "")

# ----
# main
# ----

print "TestPFD.py"
unittest.main()
print "Done."
