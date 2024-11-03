#!/usr/bin/env python3
"""unittest to test client module methods.
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized


class TestGithubOrgClient(unittest.TestCase):
    """class for unittest"""
    # Task 4
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

    # Task 5
    def test_public_repos_url(self):
        """mock property attributes"""
        with patch.object(GithubOrgClient, 'org') as mock_org:
            mock_org.__getitem__.return_value = {'repos_url': 'value'}
            obj = GithubOrgClient('google')
            res = obj._public_repos_url
            self.assertEqual(res,  {'repos_url': 'value'})

    # Task 6
    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """more patching"""
        mock_get_json.return_value = [{'name': '@hasfuad'}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = 'url'
            res = GithubOrgClient('google')
            _list = res.public_repos(self)


            self.assertEqual(_list, [])
            mock_public_url.assert_called_once()
        mock_get_json.assert_called_once()

    # Task 7
    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, arg1, arg2, expected):
        """parameterized testing"""
        res = GithubOrgClient.has_license(arg1, arg2)
        self.assertEqual(res, expected)

    # Task 8 coming soon inshalah