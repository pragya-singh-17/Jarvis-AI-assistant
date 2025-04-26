import os
import subprocess
import sys

def create_github_repo(repo_name, description):
    """
    Creates a new GitHub repository.  Requires that the user is already
    authenticated with the GitHub CLI.

    Args:
        repo_name (str): The name of the repository to create.
        description (str): A short description of the repository.

    Returns:
        bool: True on success, False on failure.
    """
    try:
        # Use subprocess.run for better error handling and output capture
        result = subprocess.run(
            ["gh", "repo", "create", repo_name, "--description", description, "--public"],
            check=True,  # Raise an exception for non-zero exit codes
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True  # Ensure output is returned as text
        )
        print(f"Successfully created repository {repo_name} on GitHub.")
        print(f"Output: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error creating repository: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except FileNotFoundError:
        print("Error: GitHub CLI (gh) not found. Please install it and authenticate with your GitHub account.")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False



def create_readme(repo_name, description, video_names=None):
    """
    Creates a README.md file with a description of the project and placeholders
    for video demos.

    Args:
        repo_name (str): The name of the repository.
        description (str): A description of the project.
        video_names (list, optional): A list of video file names.  Defaults to None.
    """
    readme_content = f"""
# Jarvis - Your Personal AI Assistant

## Description
{description}

This is a Python-based personal AI assistant, "Jarvis," that can perform various tasks, including:

* Opening websites (YouTube, Google, Wikipedia, etc.)
* Playing music files
* Telling the current time
* Opening specific folders (ML folder, VS Code)
* Chatting with a large language model (using Gemini)
* Saving chat logs
* Voice commands using speech recognition
* Text-to-speech output

## Features Implemented
The following features are implemented:
* Opening websites by voice command.
* Playing music files from a specified directory.
* Telling the time.
* Opening specific folders.
* Chatting with a large language model.
* Saving chat logs to files.

## Code Description
The core code consists of the following python script:
* `config.py`: Holds the API key for the Gemini.
* `main.py`: Main script to run the Jarvis AI.

## Dependencies
* `speech_recognition`: For voice recognition.
* `pywin32`: For text-to-speech on Windows.
* `webbrowser`: For opening websites.
* `google.generativeai`: For interacting with the Gemini API.
* `datetime`: For getting current time.
* `os`: For interacting with the operating system.
* `sys`: For system-specific parameters and functions.

## Setup Instructions
1.  **Install Dependencies:**
    ```bash
    pip install SpeechRecognition pypiwin32 google-generativeai
    ```
2.  **Configure API Key:**
    * Create a file named `config.py` in the same directory as `main.py`.
    * Add your Google Gemini API key to `config.py` as follows:
        ```python
        apiKey = "YOUR_API_KEY"  # Replace with your actual API key
        ```
3.  **Set Music Paths (Optional):**
    * Modify the `musics` list in `main.py` to point to the correct paths of your music files.
4.  **Run Jarvis:**
    ```bash
    python main.py
    ```

## Video Demos
{ " " if video_names is None else "Here are the video demos:"}
"""
    if video_names:
        for video_name in video_names:
            readme_content += f"\n### {video_name}\n\n[Demo Video of {video_name}](https://github.com/{repo_name}/blob/master/{video_name}.mp4)\n\n" #Changed the path.

    readme_path = "README.md"
    try:
        with open(readme_path, "w", encoding="utf-8") as f:
            f.write(readme_content)
        print(f"Successfully created README.md in the current directory.")
        return readme_path #returning the path.
    except Exception as e:
        print(f"Error creating README.md: {e}")
        return None

def git_init_and_commit(repo_path, initial_commit_message="Initial commit"):
    """
    Initializes a Git repository, adds all files, and makes an initial commit.

    Args:
        repo_path (str): The path to the repository.
        initial_commit_message (str): The message for the initial commit. Defaults to "Initial commit".
    Returns:
        bool: True on success, False on failure.
    """
    try:
        # Initialize the Git repository
        subprocess.run(["git", "init"], cwd=repo_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Add all files to the repository
        subprocess.run(["git", "add", "."], cwd=repo_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # Commit the changes
        subprocess.run(["git", "commit", "-m", initial_commit_message], cwd=repo_path, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Successfully initialized git and made the first commit")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error initializing Git or committing: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False



def upload_to_github(repo_name, repo_path):
    """
    Uploads the local repository to the specified GitHub repository.
    Assumes the repo has already been created.

    Args:
        repo_name (str): The name of the repository on GitHub.
        repo_path (str): The local path to the repository.

    Returns:
        bool: True on success, False on failure.
    """
    try:
        # Add the remote origin
        subprocess.run(
            ["git", "remote", "add", "origin", f"https://github.com/{repo_name}.git"], # changed the url to include .git
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        # Push the code to GitHub
        subprocess.run(
            ["git", "push", "-u", "origin", "master"],  # Or "main", depending on your branch
            cwd=repo_path,
            check=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        print(f"Successfully pushed to {repo_name} on GitHub.")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error pushing to GitHub: {e}")
        print(f"Stderr: {e.stderr}")
        return False
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return False



def main():
    """
    Main function to orchestrate the process of creating a GitHub repository,
    creating a README file, and uploading the code.
    """
    repo_name = input("Enter the name of your repository on GitHub (e.g., JarvisAI): ")
    description = input("Enter a short description for your project (e.g., 'A Python-based AI assistant'): ")
    # Get the current directory, which is where the code should be located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    #video file names
    video_names = ["Jarvis 1", "Jarvis 2"]

    # 1. Create GitHub repository
    if not create_github_repo(repo_name, description):
        print("Failed to create GitHub repository. Exiting.")
        sys.exit(1)

    # 2. Create README.md
    readme_path = create_readme(repo_name, description, video_names)
    if readme_path is None:
        print("Failed to create README.md.  Continuing, but it's recommended to have one.")

    # 3. Initialize Git and Commit
    if not git_init_and_commit(script_dir, "Initial commit of Jarvis AI project"):
        print("Failed to initialize Git repository or commit. Exiting.")
        sys.exit(1)

    # 4. Upload to GitHub
    if not upload_to_github(repo_name, script_dir):
        print("Failed to upload to GitHub.  Please check your setup and try again.")
        sys.exit(1)

    print("Successfully uploaded your code to GitHub!")
    print(f"Your repository is located at: https://github.com/{repo_name}") #Prints the github repo.


if __name__ == "__main__":
    main()

