import unittest
from unittest.mock import MagicMock
from src.GitLab import GitLab

class TestGitLab(unittest.TestCase):
    def test_import_project_success(self):
        # Mock the necessary dependencies
        gitlab_url = "https://gitlab.com"
        gitlab_access_token = "abc123"
        file_path = "tests/exports/example_project.tar.gz"
        group_id = 123

        # Create a mock for GitLab class
        gitlab = GitLab(gitlab_url, gitlab_access_token)
        gitlab.make_request = MagicMock(return_value={"status_code": 201})  # Mocking a successful response

        # Call the method under test
        with open(file_path, "rb") as file:
            response = gitlab.import_project(file.name, group_id)  # Use file.name to get the file path

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(response["status_code"], 201)

    def test_import_project_failure(self):
        # Mock the necessary dependencies
        gitlab_url = "https://gitlab.com"
        gitlab_access_token = "abc123"
        file_path = "tests/exports/example_project.tar.gz"
        group_id = 123

        # Create a mock for GitLab class
        gitlab = GitLab(gitlab_url, gitlab_access_token)
        gitlab.make_request = MagicMock(return_value={"status_code": 401})  # Mocking an unauthorized response

        # Call the method under test
        with open(file_path, "rb") as file:
            response = gitlab.import_project(file.name, group_id)  # Use file.name to get the file path

        # Assertions
        self.assertIsNone(response)
        if response is not None and response.get("status_code") == 401:
            self.assertEqual(response["status_code"], 401)

if __name__ == "__main__":
    unittest.main()
