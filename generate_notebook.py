"""
generate_notebook.py
Run this once to produce Customer_Support_AI.ipynb
"""

import json, os

# ── helpers ────────────────────────────────────────────────────────────────────
def md(source: str) -> dict:
    return {"cell_type": "markdown", "id": f"md-{abs(hash(source))%99999:05d}",
            "metadata": {}, "source": source}

def code(source: str) -> dict:
    return {"cell_type": "code", "execution_count": None,
            "id": f"co-{abs(hash(source))%99999:05d}",
            "metadata": {}, "outputs": [], "source": source}

# ── cells ──────────────────────────────────────────────────────────────────────
cells = [

    # ── TITLE ──────────────────────────────────────────────────────────────────
    md("""\
# 🤖 Customer Support AI Pipeline
### Powered by [Cohere API](https://cohere.com) — Free Tier

This notebook runs a 3-in-1 AI pipeline on customer messages:

| Output | Detail |
|---|---|
| **Category** | Complaint · Refund/Return · Sales Inquiry · Delivery Question · Account/Technical Issue · General Query · Spam |
| **Sentiment** | Positive · Neutral · Negative |
| **Auto-Reply** | Short, professional, context-aware response |

> ⚡ All three outputs are produced in **a single Cohere API call** per message.

---"""),

    # ── STEP 0: install ────────────────────────────────────────────────────────
    md("## ⚙️  Step 0 — Install Dependencies"),

    code("""\
# Run this cell once to install the Cohere SDK
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "cohere>=5.0.0", "-q"])
print("✅  Dependencies installed")"""),

    # ── STEP 1: API key ────────────────────────────────────────────────────────
    md("""\
## 🔑  Step 1 — Set Your Cohere API Key

1. Open **`config.py`** in the same folder as this notebook.
2. Replace `"your-cohere-api-key-here"` with your actual key.
3. Get a **free** key at 👉 https://dashboard.cohere.com/api-keys"""),

    code("""\
from config import COHERE_API_KEY, COHERE_MODEL, CATEGORIES, SENTIMENTS

if COHERE_API_KEY == "your-cohere-api-key-here":
    raise ValueError("⚠️  Please set your Cohere API key in config.py before continuing!")

print(f"✅  API key loaded  (ends with: …{COHERE_API_KEY[-4:]})")
print(f"📦  Model          : {COHERE_MODEL}")
print(f"📂  Categories     : {', '.join(CATEGORIES)}")
print(f"💭  Sentiments     : {', '.join(SENTIMENTS)}")"""),

    # ── STEP 2: initialise ────────────────────────────────────────────────────
    md("## 🚀  Step 2 — Initialise the AI Processor"),

    code("""\
from display_utils import render_banner
from processor import CustomerMessageProcessor

render_banner()
processor = CustomerMessageProcessor()
print("\\n✅  Processor ready — pipeline initialised!")"""),

    # ── STEP 3: demo batch ────────────────────────────────────────────────────
    md("""\
## 📨  Step 3 — Process the Demo Messages

Running the pipeline on **7 diverse customer messages** that cover every category.  
Each message costs exactly one Cohere API call."""),

    code("""\
import time
from demo_messages import DEMO_MESSAGES
from display_utils import render_batch, render_summary_table

print(f"🔄  Processing {len(DEMO_MESSAGES)} messages …\\n")

messages = [item["message"] for item in DEMO_MESSAGES]
results  = []

for i, msg in enumerate(messages, 1):
    print(f"  [{i}/{len(messages)}] {DEMO_MESSAGES[i-1]['tag']} …", end=" ")
    result = processor.process(msg)
    results.append(result)
    status = "✅" if result["status"] == "success" else "⚠️"
    print(status)
    time.sleep(0.3)   # gentle on the free-tier rate limit

print(f"\\n✅  All {len(messages)} messages processed!\\n")
render_summary_table(results)"""),

    code("""\
# Full detailed cards for each message
render_batch(results)"""),

    # ── STEP 4: custom message ─────────────────────────────────────────────────
    md("""\
## ✏️  Step 4 — Try Your Own Message

Edit `custom_message` below and run the cell to test any text you like."""),

    code("""\
from display_utils import render_result

# ✏️  Change this to any customer message you want to test
custom_message = "I still haven't received my refund after 10 business days. This is really frustrating and I need this resolved immediately!"

print("🔄  Processing …")
result = processor.process(custom_message)
render_result(result)"""),

    # ── STEP 5: export ────────────────────────────────────────────────────────
    md("""\
## 💾  Step 5 — Export Results to JSON  *(optional)*

Run this cell to save all processed results to `results.json`."""),

    code("""\
import json

export_data = [
    {
        "id":               i + 1,
        "original_message": r["original_message"],
        "category":         r["category"],
        "sentiment":        r["sentiment"],
        "auto_reply":       r["auto_reply"],
        "status":           r["status"],
    }
    for i, r in enumerate(results)
]

with open("results.json", "w", encoding="utf-8") as f:
    json.dump(export_data, f, indent=2, ensure_ascii=False)

print(f"✅  Saved {len(export_data)} results to results.json")"""),

]

# ── write notebook ─────────────────────────────────────────────────────────────
notebook = {
    "nbformat": 4,
    "nbformat_minor": 5,
    "metadata": {
        "kernelspec": {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3",
        },
        "language_info": {
            "codemirror_mode": {"name": "ipython", "version": 3},
            "file_extension": ".py",
            "mimetype": "text/x-python",
            "name": "python",
            "pygments_lexer": "ipython3",
            "version": "3.8.0",
        },
    },
    "cells": cells,
}

out_path = os.path.join(os.path.dirname(__file__), "Customer_Support_AI.ipynb")
with open(out_path, "w", encoding="utf-8") as fh:
    json.dump(notebook, fh, indent=1, ensure_ascii=False)

print(f"✅  Notebook written → {out_path}")
