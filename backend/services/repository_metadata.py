import os

def get_repo_metadata(repo_path):
    total_files = 0

    for root, dirs, files in os.walk(repo_path):
        total_files += len(files)

    return {
        "files": total_files
    }