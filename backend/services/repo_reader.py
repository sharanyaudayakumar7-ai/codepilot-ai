import git
import os

def clone_repo(repo_url):

    repo_name = repo_url.split("/")[-1]

    if repo_name.endswith(".git"):
        repo_name = repo_name[:-4]

    path = os.path.join("repos", repo_name)

    if not os.path.exists(path):
        git.Repo.clone_from(repo_url, path)

    return path