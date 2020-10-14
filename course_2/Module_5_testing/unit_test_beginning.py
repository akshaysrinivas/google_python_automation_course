#!/usr/bin/env python3

from name_interchange import swapper
import unittest
import re

class TestSwapper(unittest.TestCase):       

    def test_basic(self):
        testcase = "Srinivas, Akshay"
        expected = "Akshay, Srinivas"
        self.assertEqual(swapper(testcase), expected)

 
    def test_empty(self):
        testcase = ""
        expected = ""
        self.assertEqual(swapper(testcase), expected)

    def test_double_name(self):
        testcase = "Cornel.M, John"
        expected = "John, Cornel.M"
        self.assertEqual(swapper(testcase), expected)

    def test_numeric(self):
        testcase = "1234"
        expected = "Wrong input"
        self.assertEqual(swapper(testcase), expected)  

    def test_single_name(self):
        testcase = "Akshay"
        expected = "Akshay"
        self.assertEqual(swapper(testcase), expected)  

unittest.main()
