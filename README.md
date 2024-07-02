# GitLab Migration Tool

## Overview
The GitLab Migration Tool is a versatile Python program designed to facilitate seamless migration and management of projects between GitLab instances. Whether you're transferring projects from one GitLab environment to another or managing project variables, this tool streamlines the process with efficiency and reliability.

## Key Features

1. **Rate Limit Manager**: The Rate Limit Manager ensures optimal performance by controlling the number of API requests made within specified intervals, preventing the program from exceeding GitLab API rate limits.

2. **GitLab Integration**: Seamlessly integrate with GitLab APIs to export and import projects between GitLab instances. Enjoy smooth project migration while preserving data integrity.

3. **Project Export/Import**: Effortlessly export projects from a source GitLab instance and import them into a destination instance. Transfer code, issues, milestones, and more between GitLab environments with ease.

4. **Project Variable Management**: Manage project variables effectively by transferring variables between GitLab projects. Customize project configurations and settings during migration or replication.

5. **Shared Runners Management**: Enable shared runners for projects.

6. **Configurable Settings**: Easily configure the program's behavior using the `config.json` file. Specify GitLab URLs, access tokens, group IDs, and project mappings to adapt to different GitLab environments.

7. **Testing Framework**: Ensure code quality and reliability with the included testing framework. Verify functionality and prevent regressions during development with comprehensive testing capabilities.

8. **Cross-Platform Compatibility**: Enjoy the versatility of running the program on multiple platforms, including Linux, macOS, and Windows. Experience broad compatibility for diverse computing environments.

## Installation
1. Clone the repository: `git clone https://github.com/username/repository.git`
2. Navigate to the project directory: `cd project_name`
3. Install dependencies: `pip install -r requirements.txt`

## Usage
1. Create a new `config.json` file in the root directory of the project.
2. Add the necessary configuration parameters to `config.json`.
3. Run the main script: `python src/main.py`

## Configuration File (`config.json`)
Example `config.json` structure:
```json
{
  "token_info": {
    "src_gitlab_url": "https://source.gitlab.com",
    "src_gitlab_access_token": "your-source-access-token",
    "dest_gitlab_url": "https://destination.gitlab.com",
    "dest_gitlab_access_token": "your-destination-access-token",
    "group_id": 123
  },
  "projects": [
    {
      "src_project_id": 456
    },
    {
      "src_project_id": 789
    }
  ]
}
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

