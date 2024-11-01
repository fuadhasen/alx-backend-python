#!/usr/bin/env python3
"""unittest to test client module methods.
"""
import unittest
from unittest.mock import patch
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class for unittest"""
    @parameterized.expand([
        'google',
        'abc'
    ])
    @patch('client.get_json')
    def test_org(self, org, mock_get_json):
        obj = GithubOrgClient(org)
        obj.org
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org}")
