"""Single place where the language model is called.

Every agent goes through complete_json(), so the model provider can be swapped
in one file. Output is constrained to a JSON schema (structured outputs), so each
agent's answer is machine-checkable and lands in the audit trace as-is.
"""
import json
import os
import time
from pathlib import Path

import anthropic
from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parent.parent
load_dotenv(ROOT / ".env")

MODEL = os.environ.get("SG_MODEL", "claude-opus-5-5")
EFFORT = os.environ.get("SG_EFFORT", "medium")  # low | medium | high | xhigh | max

_client = None


class LLMRefusal(Exception):
    """Raised when the model declines the request (stop_reason == 'refusal')."""


def _get_client():
    global _client
    if _client is None:
        _client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env / .env
    return _client


def complete_json(system: str, user: str, schema: dict, max_tokens: int = 16000):
    """Call the model once and return (parsed_json, call_metadata)."""
    t0 = time.time()
    resp = _get_client().beta.messages.create(
        model=MODEL,
        max_tokens=max_tokens,
        system=system,
        messages=[{"role": "user", "content": user}],
        output_config={
            "effort": EFFORT,
            "format": {"type": "json_schema", "schema": schema},
        },
        # Server-side fallback on a safety decline (routes by refusal category).
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if resp.stop_reason == "refusal":
        detail = getattr(resp, "stop_details", None)
        raise LLMRefusal(f"model declined: {detail}")
    if resp.stop_reason == "max_tokens":
        raise RuntimeError("model output hit max_tokens before finishing")
    text = next(b.text for b in resp.content if b.type == "text")
    data = json.loads(text)
    meta = {
        "model": resp.model,
        "effort": EFFORT,
        "stop_reason": resp.stop_reason,
        "input_tokens": resp.usage.input_tokens,
        "output_tokens": resp.usage.output_tokens,
        "latency_s": round(time.time() - t0, 2),
    }
    return data, meta
