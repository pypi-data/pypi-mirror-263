import json
import os

JSON_PATH = os.path.join(os.path.dirname(__file__), 'project_paths.json')

def get_project_path(project_name:str):
    """
    Fetch the path of a project.
    
    Args:
    - project_name (str): Name of the project.
    
    Returns:
    - str or None: Path of the project if found, None otherwise.
    """
    json_file_path = JSON_PATH
    # If the JSON file doesn't exist or is empty, return None
    if not os.path.exists(json_file_path) or os.path.getsize(json_file_path) == 0:
        print(f"No projects found with this name")
        return None
    
    # Read existing data from the JSON file
    with open(json_file_path, "r") as json_file:
        projects = json.load(json_file)
    
    # Search for the project name in the projects list
    for project in projects:
        if project.get("project_name") == project_name:
            return project.get("project_path")
    
    print(f"Project '{project_name}' not found")
    return None




def remove_project_path(project_name:str):
    """
    Removes the given project_name and project_path
    
    Args: 
    project_name : Name of your project that you wish to remove.

    Returns: Nothing to return ehh!
    """

    file_path = JSON_PATH

    with open(file_path, 'r') as f:
        projects = json.load(f)
    
    new_projects = [project for project in projects if project['project_name'] != project_name]
    
    with open(file_path, 'w') as f:
        json.dump(new_projects, f, indent=4)
        print(f"'{project_name}' has been removed from your saved project paths!")




def set_project_path(project_name:str, project_directory_path:str):
    """
    Use this function to set the path of your project directory.
    The function "get_project_path" can be used later to import the complete path of your project directory in any file.
    
    Args: 
    project_name : Name of your project.
    project_directory_path : Path to your project's root directory

    Returns: Nothing to return ehh!
    """

    json_file_path = JSON_PATH

    # Prepare dictionary with the new project information
    new_project = {"project_name": project_name, "project_path": project_directory_path}
    
    # If the JSON file doesn't exist, create a new one and write the new project data
    if not os.path.exists(json_file_path):
        with open(json_file_path, "w") as json_file:
            json.dump([new_project], json_file, indent=4)
    else:
        # Read existing data from the JSON file
        with open(json_file_path, "r") as json_file:
            projects = json.load(json_file)
        
        # Append the new project data to the existing projects
        projects.append(new_project)
        
        # Write the updated projects back to the JSON file
        with open(json_file_path, "w") as json_file:
            json.dump(projects, json_file, indent=4)

    print(f"""\n\nProject Path has been saved!\nUse the function 'get_project_path({project_name})' in your codebase across the whole system to get the path to your project's root directory\n\n""")


def show_project_paths():
    """
    Shows the list of all the projects and projects paths added till date
    """
    file_path = JSON_PATH
    counter = 0
    try:
        with open(file_path, "r") as json_file:
            json_data = json.load(json_file)
            for item in json_data:
                for key, value in item.items():
                    if counter % 2 == 0:
                        print('\n')
                    print(f"{key}: {value}")
                    counter += 1
        print('\n')
    
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
    
    except json.JSONDecodeError:
        print(f"File '{file_path}' contains invalid JSON data.")