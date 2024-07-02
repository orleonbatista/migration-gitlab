import os
from RateLimitManager import RateLimitManager

class GitLab:
    """
    Class for interacting with GitLab.
    """

    def __init__(self, gitlab_url, gitlab_access_token):
        """
        Initializes the GitLab class with GitLab URL and access token.

        Args:
            gitlab_url (str): The GitLab URL.
            gitlab_access_token (str): The GitLab access token.
        """
        self.gitlab_url = gitlab_url
        self.gitlab_access_token = gitlab_access_token

    def import_project(self, file_path, group_id):
        """
        Imports a project to GitLab.

        Args:
            file_path (str): The path of the exported file.
            group_id (int): The ID of the group to import the project.

        Returns:
            dict: The imported project data.
        """
        base_url = f"{self.gitlab_url}/api/v4"
        import_url = f"{base_url}/projects/import"
        params = {"path": os.path.basename(file_path).split(".")[0], "namespace": group_id}
        headers = {"PRIVATE-TOKEN": self.gitlab_access_token}
        files = {"file": open(file_path, "rb")}

        response = RateLimitManager().make_request(import_url, "POST", headers=headers, data=params, files=files)

        if response.status_code == 201:
            print(f"Project imported successfully. It will be available in a few seconds. Status code: {response.status_code}")
            return response.json()
        else:
            print(f"Failed to import project. Status code: {response.status_code}")
            return None
