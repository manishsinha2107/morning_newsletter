import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager:
    def __init__(self):
        url: str = os.environ.get("SUPABASE_URL")
        key: str = os.environ.get("SUPABASE_SERVICE_KEY")
        if not url or not key:
            raise ValueError("SUPABASE_URL and SUPABASE_SERVICE_KEY must be set in environment")
        self.supabase: Client = create_client(url, key)

    def save_market_report(self, summary, bias, manager_notes, agent_results):
        """
        Saves the final manager report and detailed agent analysis.
        agent_results should be a list of dicts: [{'agent': '...', 'reasoning': '...', 'content': '...', 'score': 0}]
        """
        # 1. Insert final summary
        data = {
            "summary": summary,
            "market_bias": bias,
            "manager_notes": manager_notes
        }
        response = self.supabase.table("daily_summaries").insert(data).execute()

        if not response.data:
            return None

        report_id = response.data[0]['id']

        # 2. Insert individual agent reports
        agent_data = []
        for res in agent_results:
            agent_data.append({
                "report_id": report_id,
                "agent_name": res['agent'],
                "reasoning": res['reasoning'],
                "content": res['content'],
                "impact_score": res['score']
            })

        if agent_data:
            self.supabase.table("agent_reports").insert(agent_data).execute()

        return report_id
