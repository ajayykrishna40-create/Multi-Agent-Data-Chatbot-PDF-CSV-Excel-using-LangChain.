# agents/router.py

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview")

def route_query(query):

    prompt = f"""
    Classify the query into ONE word:
    - pdf
    - csv

    Query: {query}
    """

    response = llm.invoke(prompt).content.lower()

    if "pdf" in response:
        return "pdf"
    return "csv"