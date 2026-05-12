import os
from crewai_tools import SerperDevTool
from dotenv import load_dotenv

load_dotenv()

class TradingTools:
    def __init__(self):
        # Ensure SERPER_API_KEY is set in environment
        api_key = os.environ.get("SERPER_API_KEY")
        if not api_key:
            print("WARNING: SERPER_API_KEY not found. Search tools will fail.")

        self.search_tool = SerperDevTool()

    def get_search_tool(self):
        return self.search_tool
