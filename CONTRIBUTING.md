# Contributing to Smart Research Agent

We welcome contributions from developers, researchers, and students who want to build intelligent tools that combine **search, summarization, and chat reasoning**.

## 🧠 Overview
This project provides a modular AI research assistant with:
- **Frontend:** React + Tailwind for user interaction
- **Backend:** Python + FastAPI for orchestration
- **LLM API:** OpenAI GPT‑4.1 via OpenAI API
- **Pathways:** hooks for continuous model improvement (training)
- **Pricing Model:** prompt-token based billing engine

---

## 🚀 How to Contribute
1. **Fork** the repository and clone your fork.
2. **Create a branch** for your feature or fix:
   ```bash
   git checkout -b feature/add-<your-feature>
   ````

3. **Install dependencies:**

   ```bash
   cd backend && pip install -r requirements.txt
   ```

   For frontend:

   ```bash
   cd frontend && npm install && npm run dev
   ```
4. **Set up environment variables:**

   ```bash
   export OPENAI_API_KEY=<your_api_key>
   export OPENAI_MODEL=gpt-4.1
   ```
5. **Run locally:**

   ```bash
   uvicorn app:app --reload
   ```
6. **Submit a pull request (PR):**
   Include a clear description of your change, the motivation, and relevant screenshots/logs if applicable.

---

## 📁 Repository Structure

```
frontend/
  ├── src/App.jsx
  ├── src/components/SearchChat.jsx
backend/
  ├── app.py
  ├── agent.py
  ├── billing.py
  ├── utils/logger.py
requirements.txt
CONTRIBUTING.md
docker-compose.yml
```

---

## 🧩 Types of Contributions

* **Feature Additions:** New tools (e.g., document summarizer, citation extraction).
* **Integrations:** Web search APIs, vector DB, or analytics.
* **Bug Fixes:** Backend errors, API misconfigurations, token cost calculations.
* **Documentation:** README updates, tutorials, or architecture diagrams.

---

## 🧪 Code Guidelines

* **Python:** Follow [PEP8](https://peps.python.org/pep-0008/), include docstrings.
* **React:** Use functional components + hooks.
* **Testing:** Add tests for new modules; mock external API calls.
* **Commits:** Use conventional commit style (e.g., `feat:`, `fix:`, `docs:`).

---

## 💬 Communication

* Discuss in **Issues** before large design changes.
* PRs must pass all CI checks and include a clear commit message.

---

## 💡 Good First Issues

* Add logging middleware in FastAPI.
* Integrate citation formatting from search results.
* Build a token usage chart on the frontend.

We appreciate your time and creativity. Together, we can make the Smart Research Agent a powerful open-source AI researcher assistant.
