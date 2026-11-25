---
name: open-deep-research
description: Run the "Open Deep Research" Node.js agent (iterative web search via Firecrawl + LLM via OpenAI/Fireworks/OpenAI-compatible endpoint) to produce a sourced markdown research report or a short answer. Use when the user asks to run open-deep-research / deep-research-main, or wants an autonomous breadth/depth web research run with this tool.
---

# Open Deep Research

Source: github.com/dzhng/deep-research (MIT). The code lives in this skill folder
(`.claude/skills/open-deep-research/`).

## Requirements

- Node.js 22, then `npm ci` in this folder (once per fresh container).
- A `.env.local` file in this folder (never commit it) with:
  - `FIRECRAWL_KEY` (or `FIRECRAWL_BASE_URL` for self-hosted Firecrawl)
  - one LLM: `OPENAI_KEY` (uses o3-mini), or `FIREWORKS_KEY` (DeepSeek R1),
    or `OPENAI_ENDPOINT` + `CUSTOM_MODEL` for an OpenAI-compatible server.
  - optional: `CONTEXT_SIZE` (default 128000), `FIRECRAWL_CONCURRENCY` (default 2).
- Network access to api.firecrawl.dev and the LLM host. In a cloud session, ask for
  keys with the credential tool rather than having the user paste them in chat.

## Running

The CLI (`npm start`) is interactive: it asks, in order, the query, breadth
(2-10, default 4), depth (1-5, default 2), `report` or `answer`, then (report mode
only) 3 or so follow-up questions. To run it non-interactively, pipe the answers:

```bash
cd .claude/skills/open-deep-research
printf '%s\n' "<query>" 4 2 answer | npm start
```

Report mode writes `report.md`, answer mode writes `answer.md`, in this folder.
For report mode, run once to see the follow-up questions, or prefer the HTTP API:

```bash
npm run api   # listens on PORT (default 3051)
curl -s localhost:3051/api/research -H 'content-type: application/json' \
  -d '{"query":"<query>","breadth":3,"depth":2}'
```

Cost and time grow roughly as breadth^depth: start small (breadth 2-3, depth 1-2)
and confirm with the user before large runs.
