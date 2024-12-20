#!/usr/bin/env python3
"""unittest for utils.access_nestedmap func.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from typing import Mapping, Sequence
from unittest.mock import patch
import mock
from mock import MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """unittest class to test method-1 on utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path,
                               expected) -> None:
        """test method"""
        res = access_nested_map(map, path)
        self.assertEqual(res, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map, path):
        """test method for exception"""
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(map, path)
        self.assertEqual(repr(ctx.exception), repr(KeyError(path[-1])))



class TestGetJson(unittest.TestCase):
    """unittest class to test method-2 on utils"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, url, payload, mock_requests):
        """testing get_json method"""
        mocke_response = MagicMock()
        mocke_response.json.return_value = payload
        mock_requests.return_value = mocke_response

        res = get_json(url)
        mock_requests.assert_called_once_with(url)
        self.assertEqual(res, payload)


class TestMemoize(unittest.TestCase):
    """class to test memoize decorator"""
    def test_memoize(self):
        """function to test Decorator"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock_a_method:
            obj1 = TestClass()
            res1 = obj1.a_property
            res2 = obj1.a_property
            self.assertEqual(res1, res2)
            mock_a_method.assert_called_once()
