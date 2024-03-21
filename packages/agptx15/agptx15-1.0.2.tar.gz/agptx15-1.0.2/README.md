Hey, Akshat this side!
The sole purpose of this library is to help you quickly prototype your projects and deploy them on different platforms. It simplifies managing the root path of your project directory across all your Python files, allowing you to effortlessly import and export project paths on your system or server. Below are the functions you can use:



--> set_project_path(project_name:str, project_directory_path:str)

Use this function to set the path of your project directory.
    The function "get_project_path" can be used later to import the complete path of your project directory in any file.
    
    Args: 
    project_name : Name of your project.
    project_directory_path : Path to your project's root directory

    Returns: Nothing to return ehh!



--> get_project_path(project_name:str)

Fetch the path of a project.
    
    Args:
    - project_name (str): Name of the project.
    
    Returns:
    - str or None: Path of the project if found, None otherwise.



--> remove_project_path(project_name:str)

Removes the given project_name and project_path
    
    Args: 
    project_name : Name of your project that you wish to remove.

    Returns: Nothing to return ehh!



--> show_project_paths()

Shows the list of all the projects and projects paths added till date