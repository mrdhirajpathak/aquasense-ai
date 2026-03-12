from ibm_watsonx_ai.foundation_models import ModelInference
from config import IBM_API_KEY, IBM_PROJECT_ID, IBM_URL, MODEL_ID
from ai_modules.rag_engine import retrieve_context

credentials = {
    "url": IBM_URL,
    "apikey": IBM_API_KEY
}

model = ModelInference(
    model_id=MODEL_ID,
    credentials=credentials,
    project_id=IBM_PROJECT_ID
)


def ask_watson(question, context=""):

    rag_context = retrieve_context(question)

    prompt = f"""
You are an AI assistant specialized in water sustainability.

Knowledge base information:
{rag_context}

User question:
{question}

Answer clearly using the knowledge base.
"""

    response = model.generate(prompt)

    answer = response["results"][0]["generated_text"]

    return answer