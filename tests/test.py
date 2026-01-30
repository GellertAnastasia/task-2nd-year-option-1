import unittest
import sys
import os

from src.list import List

def create_list(values):
    lst = List()
    for val in values:
        lst.append(val)
    return lst

class TestLinkedList(unittest.TestCase):
    def test_empty_list(self):
        lst = List()
        self.assertTrue(lst.is_symmetric())
    
    def test_single_element(self):
        lst = List()
        lst.append(5)
        self.assertTrue(lst.is_symmetric())
    
    def test_symmetric_odd(self):
        lst = create_list([1, 2, 3, 2, 1])
        self.assertTrue(lst.is_symmetric())
    
    def test_symmetric_even(self):
        lst = create_list([1, 2, 2, 1])
        self.assertTrue(lst.is_symmetric())
    
    def test_not_symmetric(self):
        lst = create_list([1, 2, 3, 4, 5])
        self.assertFalse(lst.is_symmetric())

if __name__ == '__main__':
    unittest.main(verbosity=2)