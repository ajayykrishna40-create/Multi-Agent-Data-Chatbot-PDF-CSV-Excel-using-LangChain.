from pdf_agent import create_pdf_agent
from csv_excel_agent import create_csv_excel_agent
import os

def load_agent(file_path):
    if file_path.endswith(".pdf"):
        print("📄 PDF Agent Loaded")
        return create_pdf_agent(file_path)

    elif file_path.endswith((".csv", ".xlsx", ".xls")):
        print("📊 CSV/Excel Agent Loaded")
        return create_csv_excel_agent(file_path)

    else:
        raise ValueError("❌ Unsupported file format")



def chatbot(agent, query):
    return agent(query)



if __name__ == "__main__":
    file_path = input("📂 Enter file path: ").strip().strip('"').strip("'")

    if not os.path.exists(file_path):
        print("❌ File not found")
        exit()

    agent = load_agent(file_path)

    while True:
        user_input = input("\nAsk something (type 'exit'): ")

        if user_input.lower() == "exit":
            break

        response = chatbot(agent, user_input)
        print("\n🤖:", response)