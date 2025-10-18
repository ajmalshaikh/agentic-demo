# multi_tool_agent/agent.py
# Minimal ADK-style agent that registers a BigQuery tool.
# NOTE: adjust imports if ADK package names differ in your environment.

from google.adk.agents import Agent   # ADK import pattern
from tools import BigQueryTool

def build_agent():
    agent = Agent(name="simple-demo-agent", description="Minimal ADK demo agent")
    bq_tool = BigQueryTool()
    # register tool callable for the agent to call
    agent.register_tool("bigquery_query", bq_tool.run_query)
    return agent

# Expose a simple ask() helper that the WSGI layer will call.
_agent = build_agent()

def ask(prompt: str):
    # The exact ADK call pattern may differ; this is a generic "invoke agent" placeholder.
    # For ADK quickstart, replace with proper method (eg. agent.run(prompt) or agent.act(prompt))
    # Try agent.run(prompt) or agent.create_session(...). If import error occurs, tell me the error.
    response = _agent.run(prompt)   # may need change depending on ADK version
    return response
