import os
from crewai import Agent
from dotenv import load_dotenv
from tools import TradingTools

load_dotenv()

# Agent Definitions
class TradingAgents:
    def __init__(self):
        self.llm = "gpt-4o" # Defaulting to a strong reasoning model
        self.tools = TradingTools()
        self.search_tool = self.tools.get_search_tool()

    def us_market_analyst(self):
        return Agent(
            role='US Market Analyst',
            goal='Analyze overnight US market performance and Fed announcements to determine impact on NIFTY 50.',
            backstory='Expert in US Equities and Macroeconomics. You specialize in translating S&P 500, Nasdaq, and Dow Jones movements into potential sentiment for the Indian markets.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool]
        )

    def asian_market_analyst(self):
        return Agent(
            role='Asian Market Analyst',
            goal='Analyze Asian market trends and GIFT NIFTY movements to predict NIFTY 50 open.',
            backstory='Specialist in Asia-Pacific markets. You focus on the Nikkei 225, Hang Seng, and specifically GIFT NIFTY as the primary lead indicator for the Indian open.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool]
        )

    def indian_macro_analyst(self):
        return Agent(
            role='Indian Macro Analyst',
            goal='Analyze domestic Indian news, RBI updates, and corporate actions affecting NIFTY 50 components.',
            backstory='Deeply connected to the Indian economic landscape. You monitor SEBI, RBI, and key NIFTY 50 heavyweights like Reliance and HDFC Bank.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool]
        )

    def commodity_currency_analyst(self):
        return Agent(
            role='Commodity & Currency Analyst',
            goal='Analyze Brent Crude, USD/INR and Gold prices to determine macroeconomic pressure on India.',
            backstory='Expert in commodities and FX. You understand how oil price spikes or USD/INR volatility impact Indian inflation and equity markets.',
            verbose=True,
            allow_delegation=False,
            llm=self.llm,
            tools=[self.search_tool]
        )

    def investment_manager(self):
        return Agent(
            role='Investment Manager',
            goal='Review all analyst reports and provide a final market bias and actionable summary for NIFTY 50.',
            backstory='Chief Investment Officer with a track record of successful intraday trading. You synthesize complex data, resolve contradictions, and decide the final daily bias.',
            verbose=True,
            allow_delegation=True,
            llm=self.llm
        )
