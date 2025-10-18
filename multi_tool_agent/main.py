# main.py
from multi_tool_agent.agent import ask

def main():
    print("===== Agentic AI MVP Demo =====")
    prompt = "Run a BigQuery query: SELECT * FROM `agentailearn.agent_demo.kb` LIMIT 1;"
    
    try:
        response = ask(prompt)
        print("Agent Response:")
        print(response)
    except Exception as e:
        print("Error running agent:", e)

if __name__ == "__main__":
    main()
