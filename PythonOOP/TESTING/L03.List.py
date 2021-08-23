from extended_list import IntegerList

import unittest
from unittest import TestCase, main

class MyTestCase(TestCase):
    def test_init_inputs(self):
        list_integers = IntegerList(5, 6, 7)
        self.assertEqual([5,6,7], list_integers._IntegerList__data)

    def test_init_takes_non_int(self):
        list_integers = IntegerList(5, 6.5, 'A')
        self.assertEqual([5], list_integers._IntegerList__data)

    def test_add_int(self):
        list_integers = IntegerList(5, 6, 7)
        result = list_integers.add(100)
        self.assertEqual([5, 6, 7, 100], result)

    def test_add_if_raises_ValueError(self):
        list_integers = IntegerList(5, 6, 7)
        with self.assertRaises(Exception) as ex:
            list_integers.add('Y')
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_remove_by_idx(self):
        list_integers = IntegerList(5, 6, 7)
        result = list_integers.remove_index(0)
        self.assertEqual(5, result)
        self.assertEqual([6,7], list_integers._IntegerList__data)

    def test_add_if_raises_IndexError(self):
        list_integers = IntegerList(5, 6, 7)
        with self.assertRaises(Exception) as ex:
            list_integers.remove_index(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_specific_element(self):
        list_integers = IntegerList(5, 6, 7)
        result = list_integers.get(2)
        self.assertEqual(7, result)

    def test_get_sepc_element_IndexError(self):
        list_integers = IntegerList(5, 6, 7)
        with self.assertRaises(Exception) as ex:
            list_integers.get(3)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_sepc_element_err_type(self):
        list_integers = IntegerList(5, 6, 7)
        with self.assertRaises(IndexError) as ex:
            list_integers.insert(4, 1)
        self.assertEqual("Index is out of range", str(ex.exception))
        with self.assertRaises(ValueError) as ex:
            list_integers.insert(2, 'Q')
        self.assertEqual("Element is not Integer", str(ex.exception))

if __name__ == '__main__':
    main()
