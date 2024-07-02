import os
import time
from RateLimitManager import RateLimitManager

class GitLabProject:
    """
    Class to manage GitLab projects.
    """
    
    def __init__(self, project_id, gitlab_url, gitlab_access_token):
        """
        Initializes the GitLabProject class with project ID, GitLab URL, and access token.

        Args:
            project_id (int): The project ID.
            gitlab_url (str): The GitLab URL.
            gitlab_access_token (str): The GitLab access token.
        """
        self.project_id = project_id
        self.gitlab_url = gitlab_url
        self.gitlab_access_token = gitlab_access_token

    def export_project(self):
        """
        Exports a project from GitLab.

        Returns:
            str: The path of the exported file.
        """
        base_url = f"{self.gitlab_url}/api/v4"
        export_url = f"{base_url}/projects/{self.project_id}/export"
        payload = {"upload[http_method]": "PUT"}
        headers = {"PRIVATE-TOKEN": self.gitlab_access_token}

        response = RateLimitManager().make_request(export_url, "POST", headers=headers, data=payload)

        if response.status_code == 202:
            print("Project export initiated successfully.")
        else:
            print(f"Failed to initiate project export. Status code: {response.status_code}")
            return None

        export_status_url = f"{base_url}/projects/{self.project_id}/export"
        export_status = None

        while export_status != "finished":
            time.sleep(5)
            status_response = RateLimitManager().make_request(export_status_url, "GET", headers=headers)

            if status_response.status_code == 200:
                export_status = status_response.json().get("export_status")
                if export_status == "finished":
                    download_url = status_response.json().get("_links").get("api_url")
                    project_name = status_response.json().get("name")
                    break
                else:
                    print("Project export still in progress. Status:", export_status)
            else:
                print(f"Failed to get export status. Status code: {status_response.status_code}")
                return None

        export_dir = "./exports"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir)

        print("Project export completed. Downloading the exported file...")

        export_response = RateLimitManager().make_request(download_url, "GET", headers=headers)
        if export_response.status_code == 200:
            file_path = os.path.join(export_dir, f"{project_name}.tar.gz")
            with open(file_path, "wb") as file:
                file.write(export_response.content)

            print(f"Exported file downloaded as '{file_path}'.")
            return file_path
        else:
            print(f"Failed to download the exported file. Status code: {export_response.status_code}")
            return None
