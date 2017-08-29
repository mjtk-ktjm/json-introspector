# -*- utf-8 -*-
"""Compare two json objects recursively.

Two json strings enter, a truthy tuple is returned.

If the two json strings differ only on dict key ordering,
return indicates True, they match. Else, the first mismatching
leaf is returned along with False indicator for matching.

"""


class CompareJSON(object):
    """Compare two json objects.

    Recurse into equivalent nodes of both json objects.
    Stringify child graphs and take a hash.
    If hashes are equal, return (True,),
    else return (False, mismatch:`str`) where mismatch is the
    first non-matching leaf hash.
    On False, stop recursion.

    Attributes:
        json_string_1 (str): First JSON object in string format.
        json_string_2 (str): Second JSON object in string format.

    """

    def __init__(self, json_string_1, json_string_2):
        """Inits the CompareJSON class with two json strings."""
        self.json_string_1 = json_string_1
        self.json_string_2 = json_string_2

    def is_null(self, value):
        """Return whether input `value` is a null."""
        if value is None:
            return True
        else:
            return False

    def is_bool(self, value):
        """Return whether input `value` is a null.

        Args:
            value (any): A None, bool, int, str, list, or dict to type test.

        Returns:
            bool: True if `value` evaluates to a bool.

            False if `value` evaluates to a null, int, str, list, or dict.

        """
        if type(value) is bool:
            return True
        else:
            return False

    def is_int(self, value):
        """Return whether input `value` is an int."""
        if type(value) is int:
            return True
        else:
            return False

    def is_str(self, value):
        """Return whether input `value` is a string."""
        if type(value) is str:
            return True
        else:
            return False

    def is_list(self, value):
        """Return whether input `value` is a list."""
        if type(value) is list:
            return True
        else:
            return False

    def is_dict(self, value):
        """Return whether input `value` is a dictionary."""
        if type(value) is dict:
            return True
        else:
            return False

    def strings_are_equal(self, string1, string2):
        """Evaluate whether string1 and string2 are the same."""
        # check that inputs are strings, else raise TypeError
        # 
        if type(string1) is not str or type(string2) is not str:
            raise TypeError
        if string1 == string2:
            return True
        else:
            return False

    def types_are_equal(self, value1, value2):
        """Evaluate whether types of value1 and value2 are the same."""
        if type(value1) == type(value2):
            return True
        else:
            return False

    def hash_json(self, json_obj):
        """Hash a branch of a nested JSON object."""
        pass

    def explode_json(self, json_str):
        """Explode a JSON string into an object."""
        return False

    def implode_json(self, json_obj):
        """Implode a JSON object into a string."""
        pass

    def is_leaf(self, node):
        """Evaluate whether the current node a leaf type."""
        if self.is_null(node) or \
            self.is_bool(node) or \
            self.is_int(node) or \
            self.is_str(node):
            return True
        elif self.is_list(node) or self.is_dict(node):
            return False
        else:
            raise TypeError

    def compare_keys(self,node1, node2):
        """Check dict1 and dict2 keys are equal."""
        if type(node1) is not dict or type(node2) is not dict:
            raise TypeError
        if sorted(node1.keys())==sorted(node2.keys()):
            return True
        return False

if __name__ == '__main__':
    CompareJSON()
