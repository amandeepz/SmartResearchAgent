```jsx
import React from 'react'
import ReactDOM from 'react-dom/client'
import './index.css'
import SearchChat from './components/SearchChat'

export default function App(){
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-3xl font-bold mb-4">Smart Research Agent</h1>
        <SearchChat />
      </div>
    </div>
  )
}

const root = ReactDOM.createRoot(document.getElementById('root'))
root.render(<App />)
```
