import os


def get_python_files(repo_path):

    python_files = []

    for root, dirs, files in os.walk(repo_path):

        for file in files:

            if file.endswith(".py"):

                full_path = os.path.join(root, file)

                python_files.append(full_path)

    return python_files