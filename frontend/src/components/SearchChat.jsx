```jsx
import React, {useState} from 'react'

export default function SearchChat(){
  const [query, setQuery] = useState('')
  const [messages, setMessages] = useState([])
  const [loading, setLoading] = useState(false)

  async function send(){
    if(!query.trim()) return
    const userMsg = {role:'user', content: query}
    setMessages(msgs => [...msgs, userMsg])
    setLoading(true)
    try{
      const res = await fetch('/api/agent', {
        method: 'POST', headers: {'Content-Type':'application/json'},
        body: JSON.stringify({messages:[...messages, userMsg], query})
      })
      const data = await res.json()
      setMessages(msgs => [...msgs, {role:'assistant', content: data.reply}, {role:'system', content: `Summary:\n${data.summary}`}])
    }catch(e){
      setMessages(msgs => [...msgs, {role:'assistant', content:'Error: '+String(e)}])
    }finally{ setLoading(false) }
    setQuery('')
  }

  return (
    <div className="space-y-4">
      <div className="bg-white rounded-lg shadow p-4 max-h-96 overflow-auto">
        {messages.map((m,i)=> (
          <div key={i} className={`mb-3 ${m.role==='user'? 'text-right': 'text-left'}`}>
            <div className={`inline-block px-3 py-2 rounded ${m.role==='user'? 'bg-indigo-100':'bg-gray-100'}`}>
              <pre className="whitespace-pre-wrap">{m.content}</pre>
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input value={query} onChange={e=>setQuery(e.target.value)} className="flex-1 p-2 rounded border" placeholder="Ask a research question or paste docs..." />
        <button onClick={send} disabled={loading} className="px-4 py-2 bg-indigo-600 text-white rounded">{loading? 'Sending...':'Send'}</button>
      </div>

      <div className="text-sm text-gray-500">Pricing: billed per prompt tokens. See backend for details.</div>
    </div>
  )
}
```

---
