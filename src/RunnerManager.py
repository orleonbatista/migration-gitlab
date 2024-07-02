import json
from RateLimitManager import RateLimitManager

class RunnerManager:
    """
    Class to manage shared runners for GitLab projects.
    """

    def __init__(self, gitlab_url, access_token):
        """
        Initializes the RunnerManager class with the GitLab URL and access token.

        Args:
            gitlab_url (str): The GitLab URL.
            access_token (str): The GitLab access token.
        """
        self.gitlab_url = gitlab_url
        self.access_token = access_token

    def enable_shared_runners(self, project_id):
        """
        Enable shared runners for a specified project.

        Args:
            project_id (int): The project ID.

        Returns:
            dict: The response from the GitLab API.
        """
        url = f"{self.gitlab_url}/api/v4/projects/{project_id}"
        headers = {
            "PRIVATE-TOKEN": self.access_token,
            "Content-Type": "application/json"
        }
        data = {
            "shared_runners_enabled": True
        }

        response = RateLimitManager().make_request(url, "PUT", headers=headers, data=json.dumps(data))

        if response.status_code == 200:
            print("Shared runners enabled successfully.")
            return response
        else:
            print(f"Failed to enable shared runners: {response.status_code} - {response.reason}")
            return None