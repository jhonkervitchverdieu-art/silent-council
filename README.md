# 🏛️ Silent Council (`silent-council`)

> **7 adversarial AI minds debate behind closed doors. None of them are allowed to talk to you—except the Chief Arbiter who delivers one ruthless, unified verdict.**

[![Agent Skill Standard](https://img.shields.io/badge/Standard-SKILL.md-black)](#installation)
[![Compatible with Claude](https://img.shields.io/badge/Claude-Web%20%7C%20Desktop%20%7C%20Code-D97757)](#installation)
[![Compatible with ChatGPT](https://img.shields.io/badge/ChatGPT-Projects%20%7C%20GPTs%20%7C%20Codex-10A37F)](#installation)
[![Zero Dependencies](https://img.shields.io/badge/Dependencies-Zero-blue)](#architecture)

## Why Silent Council?

Standard LLMs suffer from **terminal sycophancy**—tell Claude or ChatGPT a flawed startup idea or a fragile software architecture, and they will enthusiastically cheer you off a cliff.

On the other hand, traditional "multi-agent debate" prompts drown you in **2,000 words of noisy roleplay monologues**.

**Silent Council solves both problems:**
1. **Closed-Door Debate:** 6 specialized critics tear your proposal apart internally while a 7th member (**The Chief Arbiter**) polices the debate, blocks empty praise, and runs a deterministic Python scoring engine with strict veto rules.
2. **Zero Noise Output:** The 6 critics are strictly forbidden from addressing you. You receive **one single, unified, <350-word executive ruling** with the exact fatal flaws and a 3-step action plan.

---

## The 7-Member Chamber

| Member | Role | Obsession |
| :--- | :--- | :--- |
| **1. The Chief Arbiter** | Supreme Moderator & Sole Spokesperson | Enforces anti-sycophancy, catches blind spots, settles trade-offs, issues final verdict. |
| **2. The Skeptic** | Devil's Advocate | Exposes unverified assumptions and week-one failure modes. |
| **3. The Architect** | First-Principles Engineer | Finds technical debt, over-engineering, and 100x bottlenecks. |
| **4. The Risk Auditor** | Security, Legal & Cost Paranoiac | Spots data leaks, compliance traps, and runaway API costs. |
| **5. The Pragmatist** | Lean Ship-It Operator | Cuts feature bloat and forces the shortest path to ROI. |
| **6. The End-User** | Impatient Customer | Attacks UX friction, jargon, and weak value propositions. |
| **7. The Futurist** | Post-Mortem Strategist | Looks 2 years ahead to diagnose why the project died. |

---

## Domain Presets

Invoke specialized council lenses by appending a preset flag to your prompt:
- `--preset code-review` — Pull requests, system architecture, refactoring plans.
- `--preset startup-pitch` — SaaS ideas, pricing models, GTM strategies.
- `--preset security-audit` — Pre-deployment production checks, auth flows, API exposure.

---

## Installation

### Option A: Claude Code / Codex CLI (Recommended)
Clone directly into your global or project skills folder:

```bash
# For Claude Code
git clone https://github.com/YOUR_USERNAME/silent-council.git ~/.claude/skills/silent-council

# For OpenAI Codex / Universal Agents
git clone https://github.com/YOUR_USERNAME/silent-council.git ~/.agents/skills/silent-council
```

### Option B: Claude.ai (Web / Desktop) & ChatGPT Projects
1. Download this repository as a `.zip` file (or upload `SKILL.md`, `scripts/arbiter_score.py`, and `presets/`).
2. **In Claude.ai:** Upload the `.zip` in **Settings → Capabilities → Skills** (or add the files to a **Claude Project**).
3. **In ChatGPT:** Upload the files into a **ChatGPT Project** or **Custom GPT** knowledge base.

---

## Usage

Simply ask Claude or ChatGPT to stress-test anything:

```text
Run the silent council on my SaaS idea: an AI wrapper that summarizes PDFs for lawyers at $49/month. --preset startup-pitch
```

```text
Challenge this database schema and API architecture before I push to production. --preset security-audit
```

*Need to see what happened behind closed doors? Append `--transcript` to unlock the anonymized minutes of the debate.*

---

## License

MIT
