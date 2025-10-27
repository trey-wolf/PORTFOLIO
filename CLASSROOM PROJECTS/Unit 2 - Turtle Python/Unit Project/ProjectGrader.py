# run_scripts.py
import os
import subprocess


def run_python_scripts_one_by_one(folder_path):
    """
    Runs each Python file in a given folder, one by one, waiting for user input.
    """
    try:
        # Check if the provided path is a valid directory
        if not os.path.isdir(folder_path):
            print(f"Error: The provided path '{folder_path}' is not a valid directory.")
            return

        # List all files in the directory
        files = os.listdir(folder_path)

        # Filter for files that end with '.py'
        python_files = sorted([f for f in files if f.endswith('.py')])

        if not python_files:
            print(f"No Python files found in the folder '{folder_path}'.")
            return

        print(f"Found {len(python_files)} Python files. Press Enter to run each one.")
        print("-" * 40)

        # Loop through each Python file
        for file_name in python_files:
            file_path = os.path.join(folder_path, file_name)

            # Print the name of the file about to be run
            print(f"\nRunning '{file_name}'...")

            # Wait for the user to press Enter
            input("Press Enter to continue...")

            try:
                # Use subprocess to run the Python file
                # The 'python' command might need to be 'python3' depending on your system
                subprocess.run(['python', file_path], check=True)
                print(f"Successfully ran '{file_name}'.")
            except subprocess.CalledProcessError as e:
                print(f"Error running '{file_name}': {e}")
            except FileNotFoundError:
                print("Error: 'python' command not found. Make sure Python is in your system's PATH.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# --- Usage ---
# Set the path to the folder containing your Python files
scripts_folder = "SCRIPT PATH GOES HERE"  # Change this to your folder's path

# Call the function with the folder path
run_python_scripts_one_by_one(scripts_folder)