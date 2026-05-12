from crewai import Crew, Process
from agents import TradingAgents
from tasks import TradingTasks

class TradingCrew:
    def __init__(self):
        self.agents = TradingAgents()
        self.tasks = TradingTasks(self.agents)

    def run(self):
        # Assemble the crew
        crew = Crew(
            agents=[
                self.agents.us_market_analyst(),
                self.agents.asian_market_analyst(),
                self.agents.indian_macro_analyst(),
                self.agents.commodity_currency_analyst(),
                self.agents.investment_manager()
            ],
            tasks=[
                self.tasks.us_market_task(),
                self.tasks.asian_market_task(),
                self.tasks.indian_macro_task(),
                self.tasks.commodity_currency_task(),
                self.tasks.manager_review_task()
            ],
            # Hierarchical process ensures the Investment Manager reviews and approves the work
            process=Process.hierarchical,
            manager_agent=self.agents.investment_manager(),
            verbose=True
        )

        return crew.kickoff()

if __name__ == "__main__":
    trading_crew = TradingCrew()
    result = trading_crew.run()
    print("\n\n########################")
    print("## FINAL MARKET OUTLOOK ##")
    print("########################\n")
    print(result)
