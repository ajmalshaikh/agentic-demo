# multi_tool_agent/tools.py
from google.cloud import bigquery
from typing import List, Dict

class BigQueryTool:
    def __init__(self):
        # Uses Application Default Credentials in Cloud Run when properly configured
        self.client = bigquery.Client()

    def run_query(self, sql: str) -> List[Dict]:
        """Executes a synchronous query and returns rows as list of dicts"""
        job = self.client.query(sql)
        rows = job.result()
        return [dict(row) for row in rows]
