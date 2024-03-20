import os
import re
from .app import get_config

def run(script_name):
    cli_command = get_config()['scripts'][script_name]

    if not cli_command:
        print(f"Script '{script_name}' not found")
        return

    cwd = os.getcwd() # Get the current working directory

    # if get_config()['smart_cd']:
    # Check if the command has a change directory command
    has_change_directory_command = re.search(r'(^|\s)cd\s\w*', cli_command)
    if not has_change_directory_command:
        # Searches for the 'python' command along with the script path
        python_command = re.search(r'python.*\.py', cli_command)
        if python_command:
            # Get the python path
            python_path = re.search(r'\S*\.py', python_command[0])
            if python_path:
                # Get the first dir in python path
                targ_dir = re.search(f'^\w*(.|\|/)(?!py)', python_path[0])
                if targ_dir:
                    # Join the target dir with the current working directory
                    cwd = os.path.join(cwd, targ_dir[0][:-1])
                    # Remove targ_dir from python_path
                    cli_command = cli_command.replace(python_path[0],python_path[0].replace(targ_dir[0], ""))
                        
    os.chdir(cwd) # Change the current working directory
    os.system(cli_command) # Run the command