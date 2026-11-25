#!/usr/bin/env python3
"""
Silent Council — Chief Arbiter Deterministic Scoring Engine
Zero external dependencies. Enforces strict veto rules against LLM sycophancy.
"""

import sys
import json

WEIGHTS = {
    "viability": 0.20,      # The Skeptic
    "architecture": 0.15,   # The Architect
    "security_risk": 0.20,  # The Risk & Security Auditor
    "execution_roi": 0.20,  # The Pragmatist
    "user_value": 0.15,     # The Impatient End-User
    "longevity": 0.10,      # The Post-Mortem Futurist
}

def evaluate_council(scores: dict) -> dict:
    for key, val in scores.items():
        if not (0 <= val <= 10):
            raise ValueError(f"Score for {key} must be between 0 and 10.")

    weighted_sum = sum(scores[k] * WEIGHTS[k] for k in WEIGHTS)
    raw_score = round(weighted_sum * 10)

    fatal_flaws = [k for k, v in scores.items() if v <= 3]
    weak_spots = [k for k, v in scores.items() if 4 <= v <= 5]

    # Anti-sycophancy penalty for unresolved fatal flaws
    penalty = len(fatal_flaws) * 12
    final_score = max(0, raw_score - penalty)

    if final_score < 50 or len(fatal_flaws) >= 2:
        verdict = "🔴 VETO / STOP"
    elif fatal_flaws or final_score < 75:
        verdict = "🟡 CONDITIONAL GO"
    else:
        verdict = "🟢 GO"

    return {
        "verdict": verdict,
        "survival_score": final_score,
        "raw_score": raw_score,
        "veto_triggers": fatal_flaws,
        "warnings": weak_spots,
    }

def main():
    if len(sys.argv) != 7:
        print(
            "Usage: python3 arbiter_score.py <viability> <architecture> <security_risk> <execution_roi> <user_value> <longevity>",
            file=sys.stderr,
        )
        sys.exit(1)

    try:
        vals = [float(x) for x in sys.argv[1:7]]
    except ValueError:
        print("Error: All 6 scores must be numeric values between 0 and 10.", file=sys.stderr)
        sys.exit(1)

    keys = list(WEIGHTS.keys())
    scores = dict(zip(keys, vals))
    result = evaluate_council(scores)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
