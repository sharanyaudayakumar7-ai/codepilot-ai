from fastapi import APIRouter
from pydantic import BaseModel

from services.repo_reader import clone_repo
from agents.repository_analysis_agent import analyze_repository

router = APIRouter()


class RepoRequest(BaseModel):
    repo_url: str


@router.post("/analyze")
def analyze_repo(data: RepoRequest):

    repo_path = clone_repo(data.repo_url)

    analysis = analyze_repository(repo_path)

    return {
        "analysis": analysis
    }