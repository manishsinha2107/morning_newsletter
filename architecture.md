# Architecture Document

## System Components

### 1. Agent Layer
- **Global Market Agent:** Monitors S&P 500, Nasdaq, Dow Jones, and US Fed commentary.
- **Regional/Proxy Agent:** Monitors GIFT NIFTY, Asian markets (Nikkei, Hang Seng).
- **Domestic Agent:** Monitors SEBI, RBI, Indian political news, and corporate earnings.
- **Macro Agent:** Monitors Crude Oil, USD/INR, Gold, and Bond yields.
- **Team Manager Agent:** Aggregates all inputs, resolves contradictions, and creates the final summary. (Implemented as `Investment Manager` in `agents.py`).

### 2. Data Flow
`Serper.dev API` $\rightarrow$ `Specialized Agents` $\rightarrow$ `Reasoning Step (Pydantic)` $\rightarrow$ `Manager Agent (Pydantic)` $\rightarrow$ `Supabase` $\rightarrow$ `Telegram/Web`

### 3. Storage Schema (Supabase)
- `daily_summaries`: Stores the final manager report, date, overall sentiment, and telegram status.
- `agent_reports`: Stores raw analysis, chain-of-thought reasoning, and impact scores (-5 to 5) from each agent.

### 4. Execution Environment
- GitHub Actions for orchestration (cron schedule).
- Secrets managed via GitHub Repository Secrets.
- Local development using `.env` (ignored by git).
