import os
import json

from services.llm_service import ask_llm
from services.repository_info import get_repository_structure


def analyze_repository(repo_path):

    readme_content = ""

    readme_path = os.path.join(
        repo_path,
        "README.md"
    )

    if os.path.exists(readme_path):

        with open(
            readme_path,
            encoding="utf-8",
            errors="ignore"
        ) as file:

            readme_content = file.read()

    structure = get_repository_structure(repo_path)

    prompt = f"""
Analyze this GitHub repository.

README:
{readme_content[:2000]}

PROJECT STRUCTURE:
{structure[:1000]}

Return ONLY raw JSON.

Do NOT use markdown.

Do NOT use ```json.

Do NOT explain anything.

Return exactly this format:

{{
  "purpose":"",
  "tech_stack":"",
  "architecture":"",
  "summary":"",
  "complexity":"Low | Medium | High"
}}
"""

    response = ask_llm(prompt)

    print("\n========== LLM RESPONSE ==========\n")
    print(response)
    print("\n==================================\n")

    response = response.replace(
        "```json",
        ""
    )

    response = response.replace(
        "```",
        ""
    )

    response = response.strip()

    try:

        return json.loads(response)

    except Exception as e:

        print("JSON PARSE ERROR:", e)

        return {
            "purpose": "Unable to parse",
            "tech_stack": "Unknown",
            "architecture": "Unknown",
            "summary": response,
            "complexity": "Unknown"
        }