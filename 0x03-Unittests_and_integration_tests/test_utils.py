#!/usr/bin/env python3
"""unittest for utils.access_nestedmap func.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map
from typing import Mapping, Sequence


class TestAccessNestedMap(unittest.TestCase):
    """unittest class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map: Mapping, path: Sequence,
                               expected: any):
        """test method"""
        res = access_nested_map(map, path)
        self.assertEqual(res, expected)
