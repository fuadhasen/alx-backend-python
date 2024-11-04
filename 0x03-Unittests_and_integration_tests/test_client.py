#!/usr/bin/env python3
"""unittest to test client module methods.
"""
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixture import Test_payload


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
        mock_get_json.return_value = [{'name': 'repositary1'},
                                      {'name': 'repositary2'}]
        with patch.object(GithubOrgClient, '_public_repos_url',
                          new_callable=PropertyMock) as mock_public_url:
            mock_public_url.return_value = 'url'
            obj = GithubOrgClient('google')
            _list = obj.public_repos()

            self.assertEqual(_list, ['repositary1', 'repositary2'])
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


# Task 8
@parameterized_class({
    'org_payload': Test_payload[0][0],
    'repos_payload': Test_payload[0][1],
    'expected_repos': [repo['name'] for repo in Test_payload[0][1]],
    'apache2_repos': [repo['name'] for repo in Test_payload if repo.get(
        'license', {}
    ).get('key') == "apache-2.0"]
})
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up mock for requests.get."""
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        # Configure side_effect for different URLs
        cls.mock_get.side_effect = lambda url: {
            "https://api.github.com/orgs/some_org": cls.org_payload,
            "https://api.github.com/orgs/some_org/repos": cls.repos_payload
        }.get(url, {})

    @classmethod
    def tearDownClass(cls):
        """Stop the requests.get patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test that GithubOrgClient.public_repos returns expected repos."""
        client = GithubOrgClient("some_org")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test that public_repos with license filter."""
        client = GithubOrgClient("some_org")
        self.assertEqual(client.public_repos(
            license="apache-2.0"), self.apache2_repos)
