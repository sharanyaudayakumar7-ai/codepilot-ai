import os


def get_repository_structure(repo_path):

    structure = []

    for root, dirs, files in os.walk(repo_path):

        depth = root.replace(repo_path, "").count(os.sep)

        if depth > 2:
            continue

        structure.append(root)

    return "\n".join(structure)