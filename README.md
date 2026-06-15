# 🤖 Customer Support AI Pipeline

A 3-in-1 AI pipeline that processes customer messages using the **Cohere API**
and produces — in a single API call per message:

| Output | Options |
|---|---|
| **Category** | Complaint · Refund/Return · Sales Inquiry · Delivery Question · Account/Technical Issue · General Query · Spam |
| **Sentiment** | Positive · Neutral · Negative |
| **Auto-Reply** | Short, professional, context-aware response |

---

## 📁 Project Structure

```
customer_support_ai/
├── config.py               ← 🔑 PUT YOUR API KEY HERE
├── processor.py            ← Core pipeline (Cohere API calls + JSON parsing)
├── demo_messages.py        ← 7 sample messages covering all categories
├── display_utils.py        ← Styled HTML cards for Jupyter rendering
├── generate_notebook.py    ← Script that produced the .ipynb (already run)
├── requirements.txt        ← Python dependencies
├── Customer_Support_AI.ipynb  ← Main notebook — open and run this
└── README.md
```

---

## ⚡ Quick Start

### 1. Get a free Cohere API key
Sign up at https://dashboard.cohere.com/api-keys (no credit card needed).

### 2. Set your API key
Open `config.py` and replace the placeholder:
```python
COHERE_API_KEY = "your-actual-key-here"
```

### 3. Open the notebook
```bash
jupyter notebook Customer_Support_AI.ipynb
```

### 4. Run all cells top to bottom (`Kernel → Restart & Run All`)

That's it — results appear as styled cards directly in the notebook.

---

## 🔧 How it works

```
Customer Message
      │
      ▼
  config.py        ← categories, sentiments, model name
      │
      ▼
 processor.py      ← builds structured prompt → calls Cohere chat API
                      → parses JSON response
      │
      ▼
 display_utils.py  ← renders HTML cards in Jupyter
      │
      ▼
 Three outputs: Category · Sentiment · Auto-Reply
```

**One API call per message** returns all three outputs as a JSON object:
```json
{
  "category":   "Delivery Question",
  "sentiment":  "Negative",
  "auto_reply": "We sincerely apologize for the delay …"
}
```

---

## 📦 Dependencies

```
cohere >= 5.0.0   (Cohere Python SDK — free tier supports command-r-plus)
jupyter           (notebook environment)
```

Install with:
```bash
pip install cohere>=5.0.0
```

---

## 🗒️ Notes

- The free Cohere tier has a rate limit (~20 API calls/minute). A small `time.sleep(0.3)` 
  is included in the batch processing cell to stay well within limits.
- If the model returns malformed JSON, the processor falls back to safe defaults 
  and reports the error in the `status` field.
- All 7 categories and 3 sentiments are covered by the 7 demo messages.
