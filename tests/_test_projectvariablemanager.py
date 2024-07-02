import unittest
from unittest.mock import MagicMock
from src.ProjectVariableManager import ProjectVariableManager

class TestProjectVariableManager(unittest.TestCase):
    def test_create_project_variable_success(self):
        # Mock the necessary dependencies
        project_id = 123
        access_token = "abc123"
        variable = {"key": "example_key", "value": "example_value"}
        gitlab_url = "https://gitlab.com"
        project_variable_manager = ProjectVariableManager(gitlab_url, access_token, gitlab_url, access_token)
        project_variable_manager.make_request = MagicMock(return_value={"status_code": 201})

        # Call the method under test
        project_variable_manager.create_project_variable(project_id, variable)

        # Assertions
        project_variable_manager.make_request.assert_called_once()

    def test_create_project_variable_failure(self):
        # Mock the necessary dependencies
        project_id = 123
        access_token = "abc123"
        variable = {"key": "example_key", "value": "example_value"}
        gitlab_url = "https://gitlab.com"
        project_variable_manager = ProjectVariableManager(gitlab_url, access_token, gitlab_url, access_token)
        project_variable_manager.make_request = MagicMock(return_value={"status_code": 500})

        # Call the method under test
        project_variable_manager.create_project_variable(project_id, variable)

        # Assertions
        project_variable_manager.make_request.assert_called_once()

if __name__ == "__main__":
    unittest.main()
