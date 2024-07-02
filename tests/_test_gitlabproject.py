import unittest
from unittest.mock import MagicMock
from src.GitLabProject import GitLabProject

class TestGitLabProject(unittest.TestCase):
    def test_export_project_success(self):
        # Mock the necessary dependencies
        project_id = 123
        gitlab_url = "https://gitlab.com"
        gitlab_access_token = "abc123"
        gitlab_project = GitLabProject(project_id, gitlab_url, gitlab_access_token)
        gitlab_project.make_request = MagicMock(return_value={"status_code": 202})

        # Call the method under test
        response = gitlab_project.export_project()

        # Assertions
        self.assertIsNotNone(response)
        self.assertEqual(response["status_code"], 202)

    def test_export_project_failure(self):
        # Mock the necessary dependencies
        project_id = 123
        gitlab_url = "https://gitlab.com"
        gitlab_access_token = "abc123"
        gitlab_project = GitLabProject(project_id, gitlab_url, gitlab_access_token)
        gitlab_project.make_request = MagicMock(return_value={"status_code": 500})

        # Call the method under test
        response = gitlab_project.export_project()

        # Assertions
        self.assertIsNone(response)
        self.assertEqual(response["status_code"], 500)

if __name__ == "__main__":
    unittest.main()
