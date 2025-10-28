# core agent: handles search, call to OpenAI, summarization, and training hook
await asyncio.sleep(0.05)
return f"SearchResults(top: 3) for: {query}\n- Result A excerpt...\n- Result B excerpt...\n"


async def _call_openai(self, messages: List[Dict[str,str]]) -> Dict[str,Any]:
# Use Chat Completions API (chat.create) via httpx
headers = {
'Authorization': f'Bearer {OPENAI_API_KEY}',
'Content-Type': 'application/json'
}
payload = {
'model': MODEL_NAME,
'messages': messages,
'temperature': 0.2,
'max_tokens': 1024
}
async with httpx.AsyncClient(timeout=60.0) as client:
r = await client.post(f"{OPENAI_API_BASE}/chat/completions", json=payload, headers=headers)
r.raise_for_status()
return r.json()


async def _summarize(self, text: str) -> str:
prompt = [
{'role':'system', 'content':'You are a concise summarizer.'},
{'role':'user', 'content': 'Summarize the following text in 4 bullet points:\n\n' + text}
]
resp = await self._call_openai(prompt)
return resp['choices'][0]['message']['content']


async def run(self, query: str, conversation: List[Dict[str,str]]):
# 1. search
search_text = await self._search_web(query)


# 2. compose messages for model: system + search + conversation + user query
system_msg = {'role':'system', 'content': 'You are a research assistant that cites search results and produces summaries.'}
combined = [system_msg, {'role':'system', 'content': search_text}] + conversation + [{'role':'user', 'content': query}]


# 3. call model
resp = await self._call_openai(combined)
assistant_reply = resp['choices'][0]['message']['content']
usage = resp.get('usage', {})


# 4. summarization
self.last_summary = (await self._summarize(assistant_reply))[:1000]


# 5. training/pathway hook (non-blocking)
asyncio.create_task(self._training_pathway(query, assistant_reply, usage))


return assistant_reply, usage


async def _training_pathway(self, query, reply, usage):
# Placeholder: store a record to a training queue or external store.
# This function is intentionally non-blocking and returns quickly.
# In production, securely store pair with metadata, follow user opt-in.
await asyncio.sleep(0.01)
# e.g., write to a DB or call a retriever service
print('training_hook:', query[:80], '...')
