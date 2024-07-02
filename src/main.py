import json
from GitLabProject import GitLabProject
from GitLab import GitLab
from RunnerManager import RunnerManager
from ProjectVariableManager import ProjectVariableManager

def main():
    """
    Main function to execute the script.
    """
    with open('config.json', 'r') as file:
        config = json.load(file)

    token_info = config.get('token_info', {})
    projects = config.get('projects', [])

    src_gitlab_url = token_info.get('src_gitlab_url')
    src_gitlab_access_token = token_info.get('src_gitlab_access_token')
    dest_gitlab_url = token_info.get('dest_gitlab_url')
    dest_gitlab_access_token = token_info.get('dest_gitlab_access_token')
    group_id = token_info.get('group_id')

    dest_gitlab = GitLab(dest_gitlab_url, dest_gitlab_access_token)
    runner_manager = RunnerManager(dest_gitlab_url, dest_gitlab_access_token)


    for project_data in projects:
        src_project_id = project_data.get('src_project_id')

        print("Exporting source project...")
        src_project = GitLabProject(src_project_id, src_gitlab_url, src_gitlab_access_token)
        exported_file = src_project.export_project()
        if not exported_file:
            print("Failed to export project.")
            continue

        print("Importing destination project...")
        dest_project_data = dest_gitlab.import_project(exported_file, group_id)
        if not dest_project_data:
            print("Failed to import project.")
            continue

        dest_project_id = dest_project_data.get("id")
        print("Transferring variables to destination project...")
        variable_manager = ProjectVariableManager(src_gitlab_url, src_gitlab_access_token, dest_gitlab_url, dest_gitlab_access_token)
        variables = variable_manager.get_project_variables(src_project_id)
        if variables:
            for var_data in variables:
                variable_manager.create_project_variable(dest_project_id, var_data)

        print("Enabling shared runners for the destination project...")
        runner_manager.enable_shared_runners(dest_project_id)

if __name__ == "__main__":
    main()
