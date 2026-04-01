import pandas as pd
from langchain_google_genai import ChatGoogleGenerativeAI
import os

def create_csv_excel_agent(file_path):
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith((".xlsx", ".xls")):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a CSV or Excel file.")

    llm = ChatGoogleGenerativeAI(
        model="gemini-3-flash-preview",
        temperature=0.7,
        google_api_key=os.getenv("GOOGLE_API_KEY")
    )

    def run_query(query):
        query_lower = query.lower()
        if "summary" in query_lower or "summarize" in query_lower:
            preview= df.head(10).to_string()

            prompt=f"""
            Analyze the data and provide a clear summary:
            Data Preview:
            {preview}
             Include:
            - What data represents
            - Key insights
            - Any patterns
            """
            return llm.invoke(prompt).content
        
        elif "top" in query_lower:
            return df.head().to_string()

        elif "columns" in query_lower:
            return str(df.columns.tolist())

        else:
            return df.describe().to_string()
        

    return run_query