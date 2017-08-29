"""Docstring."""
import unittest
from compare_json import CompareJSON

class BasicsTests(unittest.TestCase):
    """ """
    global comparator
    comparator = CompareJSON('string1', 'string2')

    def test_is_null(self):
        """ """
        # TODO discover what the object[null] value type is in py
        # self.assertEqual(True, comparator.is_null(None))
        self.assertEqual(False, comparator.is_null(str()))

    def test_is_bool(self):
        """ """
        self.assertEqual(True, comparator.is_bool(True))
        self.assertEqual(True, comparator.is_bool(False))
        self.assertEqual(False, comparator.is_bool(str()))

    def test_is_int(self):
        """ """
        self.assertEqual(True, comparator.is_int(int()))
        self.assertEqual(False, comparator.is_int(str()))

    def test_is_str(self):
        """ """
        self.assertEqual(True, comparator.is_str(str()))
        self.assertEqual(False, comparator.is_str(int()))


    def test_is_list(self):
        """ """
        self.assertEqual(True, comparator.is_list(list()))
        self.assertEqual(False, comparator.is_list(str()))


    def test_is_dict(self):
        """ """
        self.assertEqual(True, comparator.is_dict(dict()))
        self.assertEqual(False, comparator.is_dict(str()))

    def test_strings_are_equal(self):
        """Test that strings are equivalent."""
        string1 = 'this is the first string'
        string2 = 'this is the first string' # ==, !is
        string3 = 'this is the second string'
        self.assertEqual(True, comparator.strings_are_equal(string1, string2))
        self.assertEqual(False, comparator.strings_are_equal(string1, string3))

    def test_types_are_equal(self):
        """Test that types for two values match."""
        self.assertEqual(True, comparator.types_are_equal(None, None))
        self.assertEqual(True, comparator.types_are_equal(True, True))
        self.assertEqual(True, comparator.types_are_equal(True, False))
        self.assertEqual(True, comparator.types_are_equal(int(), int()))
        self.assertEqual(False, comparator.types_are_equal(int(), str()))
        self.assertEqual(True, comparator.types_are_equal(str(), str()))
        self.assertEqual(True, comparator.types_are_equal(list(), list()))
        self.assertEqual(True, comparator.types_are_equal(dict(), dict()))

    def test_hash_json(self):
        """Test that hash returns expected value for a string."""
        pass

    def test_explode_json(self):
        """Test that valid JSON string explodes into valid object."""
        pass

    def test_implode_json(self):
        """Test that valid JSON object implodes into valid string."""
        pass

    def test_is_leaf(self):
        """Test whether current node is a leaf type."""
        self.assertEqual(True, comparator.is_leaf(None))
        self.assertEqual(True, comparator.is_leaf(True))
        self.assertEqual(True, comparator.is_leaf(False))
        self.assertEqual(True, comparator.is_leaf(int()))
        self.assertEqual(True, comparator.is_leaf(str()))
        self.assertEqual(False, comparator.is_leaf(list()))
        self.assertEqual(False, comparator.is_leaf(dict()))

    def test_compare_keys(self):
        """Test comparison of keys from two dict nodes."""
        dict1 = {"a":1 , "b":2 , "c":3}
        dict2 = {"b":1 ,"a":2 , "c":3}
        dict3 = {"b":1 ,"d":2 , "c":3}
        self.assertEqual(True, comparator.compare_keys(dict1, dict2))
        self.assertEqual(False, comparator.compare_keys(dict2, dict3))

if __name__ == '__main__':
    unittest.main()
