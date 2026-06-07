from services.llm_service import ask_llm

response = ask_llm(
    "Explain FastAPI in one sentence."
)

print(response)