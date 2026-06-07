from services.repo_reader import clone_repo

repo = clone_repo(
    "https://github.com/tiangolo/fastapi"
)

print(repo)