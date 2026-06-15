"""
processor.py — Customer Support AI Pipeline
Handles: Classification · Sentiment Analysis · Auto-Reply Generation
All three outputs are produced in a single Cohere API call per message.
"""

import cohere
import json
import re

from config import COHERE_API_KEY, COHERE_MODEL, CATEGORIES, SENTIMENTS


class CustomerMessageProcessor:
    """
    Processes a customer message and returns:
      - category  : one of CATEGORIES
      - sentiment : one of SENTIMENTS
      - auto_reply: a short, professional response
    """

    def __init__(self):
        self.co = cohere.ClientV2(COHERE_API_KEY)
        print(f"[Processor] Connected to Cohere — model: {COHERE_MODEL}")

    # ------------------------------------------------------------------
    # Prompt builder
    # ------------------------------------------------------------------
    def _build_prompt(self, message: str) -> str:
        cats  = ", ".join(f'"{c}"' for c in CATEGORIES)
        sents = ", ".join(f'"{s}"' for s in SENTIMENTS)

        return f"""You are a professional customer support AI. Analyze the customer message below.

Return ONLY a single valid JSON object with exactly these three keys:

  "category"   — choose exactly one from: [{cats}]
  "sentiment"  — choose exactly one from: [{sents}]
  "auto_reply" — write a short, professional 2-3 sentence response suited to this message

Customer Message:
\"\"\"{message}\"\"\"

Rules:
- Output ONLY the JSON object — no markdown, no code fences, no commentary.
- The auto_reply must be polite, empathetic, and brand-appropriate.
- For spam messages, the auto_reply should be a brief, polite non-engagement response.

JSON output:"""

    # ------------------------------------------------------------------
    # JSON parser (robust against markdown fences / extra whitespace)
    # ------------------------------------------------------------------
    @staticmethod
    def _parse_json(raw: str) -> dict:
        text = raw.strip()
        # Strip markdown code blocks if model adds them
        text = re.sub(r"```(?:json)?\s*", "", text)
        text = re.sub(r"```\s*$", "", text, flags=re.MULTILINE)
        text = text.strip()

        # Extract the first {...} block
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            text = match.group(0)

        return json.loads(text)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def process(self, message: str) -> dict:
        """Process a single customer message. Returns a result dict."""
        try:
            response = self.co.chat(
                model=COHERE_MODEL,
                messages=[{"role": "user", "content": self._build_prompt(message)}],
            )

            raw_text = response.message.content[0].text
            parsed = self._parse_json(raw_text)

            return {
                "original_message": message,
                "category":   parsed.get("category",   "General Query"),
                "sentiment":  parsed.get("sentiment",  "Neutral"),
                "auto_reply": parsed.get("auto_reply", "Thank you for reaching out. We will get back to you shortly."),
                "status": "success",
            }

        except json.JSONDecodeError as exc:
            return self._fallback(message, f"JSON parse error: {exc}")
        except Exception as exc:
            return self._fallback(message, f"API error: {exc}")

    @staticmethod
    def _fallback(message: str, reason: str) -> dict:
        return {
            "original_message": message,
            "category":   "General Query",
            "sentiment":  "Neutral",
            "auto_reply": (
                "Thank you for contacting us. A member of our support team "
                "will review your message and respond as soon as possible."
            ),
            "status": reason,
        }

    def process_batch(self, messages: list) -> list:
        """Process a list of messages and return a list of result dicts."""
        results = []
        for msg in messages:
            results.append(self.process(msg))
        return results
