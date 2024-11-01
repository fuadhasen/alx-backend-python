#!/usr/bin/env python3
"""unittest for utils.access_nestedmap func.
"""
import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence
import mock
from mock import MagicMock


class TestAccessNestedMap(unittest.TestCase):
    """unittest class to test method-1 on utils"""
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

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, map: Mapping, path: Sequence):
        """test method for exception"""
        with self.assertRaises(KeyError) as ctx:
            access_nested_map(map, path)


class TestGetJson(unittest.TestCase):
    """unittest class to test method-2 on utils"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('requests.get')
    def test_get_json(self, url: str, payload: dict, mock_requests: any):
        """testing get_json method"""
        mocke_response = MagicMock()
        mocke_response.json.return_value = payload
        mock_requests.return_value = mocke_response

        res = get_json(url)
        mock_requests.assert_called_once_with(url)
        self.assertEqual(res, payload)
