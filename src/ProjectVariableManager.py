from RateLimitManager import RateLimitManager

class ProjectVariableManager:
    """
    Class to manage project variables in GitLab.
    """

    def __init__(self, src_gitlab_url, src_gitlab_access_token, dest_gitlab_url, dest_gitlab_access_token):
        """
        Initializes the ProjectVariableManager class with source and destination GitLab URLs and access tokens.

        Args:
            src_gitlab_url (str): The source GitLab URL.
            src_gitlab_access_token (str): The source GitLab access token.
            dest_gitlab_url (str): The destination GitLab URL.
            dest_gitlab_access_token (str): The destination GitLab access token.
        """
        self.src_gitlab_url = src_gitlab_url
        self.src_gitlab_access_token = src_gitlab_access_token
        self.dest_gitlab_url = dest_gitlab_url
        self.dest_gitlab_access_token = dest_gitlab_access_token

    def get_project_variables(self, project_id):
        """
        Gets variables of a project.

        Args:
            project_id (int): The project ID.

        Returns:
            list: A list of project variables.
        """
        url = f"{self.src_gitlab_url}/api/v4/projects/{project_id}/variables"
        headers = {"PRIVATE-TOKEN": self.src_gitlab_access_token}
        response = RateLimitManager().make_request(url, "GET", headers=headers)
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to fetch project variables.")
            return None

    def create_project_variable(self, project_id, variable):
        """
        Creates a variable in a project.

        Args:
            project_id (int): The project ID.
            variable (dict): The data of the variable to be created.
        """
        url = f"{self.dest_gitlab_url}/api/v4/projects/{project_id}/variables"
        headers = {"PRIVATE-TOKEN": self.dest_gitlab_access_token}
        response = RateLimitManager().make_request(url, "POST", headers=headers, data=variable)
        if response.status_code == 201:
            print(f"Variable {variable['key']} created successfully.")
        else:
            print(f"Failed to create variable {variable['key']}.")
