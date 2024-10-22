#!/usr/bin/python3
import unittest
from models.base import Base
"""import unittest to run tests on class base"""


class TestBase(unittest.TestCase):
    """Test Base instantiation"""
    def test_no_arg(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_three_bases(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_None(self):
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_unique_id(self):
        self.assertEqual(12, Base(12).id)

    def test_nb_instances_after_unique_id(self):
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_private_id(self):
        b = Base(12)
        b.id = 13
        self.assertEqual(13, b.id)

    def test_string(self):
        self.assertEqual("base", Base("base").id)

    def test_float(self):
        self.assertEqual(12.2, Base(12.2).id)

    def test_private_instance(self):
        with self.assertRaises(AttributeError):
            print(Base(12).__nb_instances)

    def test_complex_id(self):
        self.assertEqual(complex(12), Base(complex(12)).id)

    def test_dict_id(self):
        self.assertEqual({"b1": 1, "b2": 2}, Base({"b1": 1, "b2": 2}).id)

    def test_bool_id(self):
        self.assertEqual(True, Base(True).id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_frozenset_id(self):
        self.assertEqual(frozenset({1, 2, 3}), Base(frozenset({1, 2, 3})).id)

    def test_range_id(self):
        self.assertEqual(range(5), Base(range(5)).id)

    def test_bytes_id(self):
        self.assertEqual(b'Python', Base(b'Python').id)

    def test_bytearray_id(self):
        self.assertEqual(bytearray(b'Python'), Base(bytearray(b'Python')).id)

    def test_memoryview_id(self):
        self.assertEqual(memoryview(b'Python'), Base(memoryview(b'Python')).id)

    def test_inf_id(self):
        self.assertEqual(float('inf'), Base(float('inf')).id)

    def test_NaN_id(self):
        self.assertNotEqual(float('nan'), Base(float('nan')).id)

    def test_two_args(self):
        with self.assertRaises(TypeError):
            Base(12, 13)


if __name__ == '__main__':
    unittest.main()
