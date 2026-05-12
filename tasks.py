from crewai import Task
from pydantic import BaseModel, Field
from typing import List
from agents import TradingAgents

# --- Structured Output Models ---

class AnalystReport(BaseModel):
    summary: str = Field(..., description="A concise summary of the market data found.")
    reasoning: str = Field(..., description="Chain-of-thought reasoning on how this affects NIFTY 50.")
    impact_score: int = Field(..., description="Impact score from -5 (Very Bearish) to 5 (Very Bullish).")

class ManagerOutlook(BaseModel):
    market_bias: str = Field(..., description="Final bias: BULLISH, BEARISH, or NEUTRAL.")
    key_drivers: List[str] = Field(..., description="List of top 3-5 reasons for the bias.")
    final_summary: str = Field(..., description="Comprehensive actionable summary for an intraday trader.")
    analyst_summaries: List[str] = Field(..., description="Brief summaries of the 4 analysts' views.")

# --- Tasks ---

class TradingTasks:
    def __init__(self, agents):
        self.agents = agents

    def us_market_task(self):
        return Task(
            description=(
                "1. Search for overnight US market closing data (S&P 500, Nasdaq, Dow).\n"
                "2. Analyze any FOMC/Fed announcements or key US economic data released overnight.\n"
                "3. Reason how these movements will influence global sentiment and specifically the NIFTY 50.\n"
                "4. Assign an impact score from -5 (Very Bearish) to 5 (Very Bullish)."
            ),
            expected_output="A structured report with summary, reasoning and impact score.",
            output_json=AnalystReport,
            agent=self.agents.us_market_analyst(),
        )

    def asian_market_task(self):
        return Task(
            description=(
                "1. Analyze current GIFT NIFTY levels and trend.\n"
                "2. Check Nikkei 225 and Hang Seng performance.\n"
                "3. Reason if the NIFTY 50 is likely to open with a gap up, gap down, or flat.\n"
                "4. Assign an impact score from -5 (Very Bearish) to 5 (Very Bullish)."
            ),
            expected_output="A structured report with summary, reasoning and impact score.",
            output_json=AnalystReport,
            agent=self.agents.asian_market_analyst(),
        )

    def indian_macro_task(self):
        return Task(
            description=(
                "1. Gather overnight domestic news from India (Political, Regulatory, RBI).\n"
                "2. Analyze any significant corporate news for NIFTY 50 heavyweights (e.g., Reliance, HDFC Bank, ICICI Bank).\n"
                "3. Reason how this domestic sentiment overrides or supports global trends.\n"
                "4. Assign an impact score from -5 (Very Bearish) to 5 (Very Bullish)."
            ),
            expected_output="A structured report with summary, reasoning and impact score.",
            output_json=AnalystReport,
            agent=self.agents.indian_macro_analyst(),
        )

    def commodity_currency_task(self):
        return Task(
            description=(
                "1. Check Brent Crude oil prices and USD/INR exchange rate.\n"
                "2. Analyze Gold price movements.\n"
                "3. Reason if current commodity prices create inflationary pressure or favorable conditions for Indian equities.\n"
                "4. Assign an impact score from -5 (Very Bearish) to 5 (Very Bullish)."
            ),
            expected_output="A structured report with summary, reasoning and impact score.",
            output_json=AnalystReport,
            agent=self.agents.commodity_currency_analyst(),
        )

    def manager_review_task(self):
        return Task(
            description=(
                "1. Review the reports from the US, Asian, Indian Macro, and Commodity analysts.\n"
                "2. Identify contradictions (e.g., US is bullish but Domestic is bearish).\n"
                "3. Synthesize a final, coherent market outlook for today's NIFTY 50 trading.\n"
                "4. Determine the final Market Bias: BULLISH, BEARISH, or NEUTRAL.\n"
                "5. Provide a concise actionable summary for an intraday option trader."
            ),
            expected_output="A final executive summary including bias, drivers and final summary.",
            output_json=ManagerOutlook,
            agent=self.agents.investment_manager(),
        )
