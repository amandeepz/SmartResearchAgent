```python
# FastAPI server: routes for /api/agent, /api/billing and simple health checks
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from agent import ResearchAgent
from billing import BillingEngine

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=['*'], allow_methods=['*'], allow_headers=['*'])

agent = ResearchAgent()
billing = BillingEngine(rate_per_token_input=0.000002, rate_per_token_output=0.00001)

class AgentRequest(BaseModel):
    messages: list
    query: str

@app.post('/api/agent')
async def run_agent(req: AgentRequest):
    try:
        # run the research pipeline
        reply, usage = await agent.run(req.query, req.messages)
        # compute billing for this interaction
        cost = billing.compute_cost(usage)
        return { 'reply': reply, 'summary': agent.last_summary, 'usage': usage, 'cost_usd': cost }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get('/api/health')
async def health():
    return {'status': 'ok'}
```

---
