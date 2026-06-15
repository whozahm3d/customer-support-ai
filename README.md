# 🤖 Customer Support AI Pipeline

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Cohere](https://img.shields.io/badge/Cohere-API-39594C?style=for-the-badge&logo=cohere&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

**An AI-powered customer message processing pipeline that classifies messages, detects sentiment, and generates professional auto-replies — all in a single API call.**

[Features](#-features) • [Demo](#-demo) • [Project Structure](#-project-structure) • [Setup](#-setup) • [Usage](#-usage) • [Output](#-output) • [Contributing](#-contributing)

</div>

---

## 📌 Overview

Customer Support AI Pipeline is a lightweight NLP system built for automating the first layer of customer support. Given any incoming customer message, the system produces three structured outputs:

| Output | Description |
|---|---|
| **Category** | Classifies the message into one of 7 predefined support categories |
| **Sentiment** | Detects the emotional tone of the message |
| **Auto-Reply** | Generates a short, professional response tailored to the message |

All three outputs are produced in a **single API call per message**, making the pipeline fast and token-efficient.

---

## ✨ Features

- ⚡ **Single API call** per message returns all three outputs as structured JSON
- 🎯 **7 classification categories** covering the full range of customer support scenarios
- 💬 **Context-aware auto-replies** that match the tone and urgency of each message
- 🎨 **Styled Jupyter output** with color-coded category and sentiment badges
- 📊 **CSV export** of all processed results for reporting and analysis
- 🛡️ **Robust error handling** with safe fallback values if parsing fails
- 🆓 **Fully free** — runs on Cohere's free trial API tier

---

## 🗂 Classification Categories

```
Complaint  •  Refund/Return  •  Sales Inquiry  •  Delivery Question
Account/Technical Issue  •  General Query  •  Spam
```

## 💭 Sentiment Labels

```
Positive  •  Neutral  •  Negative
```

---

## 🎥 Demo

The pipeline processes each message and renders a styled card in the Jupyter notebook:

```
Input Message:
"I ordered a laptop two weeks ago and it still hasn't arrived! This is absolutely unacceptable."

Output:
┌─────────────────────────────────────────────────────┐
│  CATEGORY     Complaint                             │
│  SENTIMENT    ❌ Negative                           │
│  AUTO-REPLY   We sincerely apologize for the delay  │
│               in your order. Our team is urgently   │
│               looking into this and will update you  │
│               within 24 hours.                      │
└─────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
customer-support-ai-pipeline/
│
├── 📓 Customer_Support_AI.ipynb   # Main notebook — run this
│
├── 🐍 config.py                   # API key, model name, category & sentiment labels
├── 🐍 processor.py                # Core pipeline: prompt builder, Cohere API call, JSON parser
├── 🐍 demo_messages.py            # 7 sample messages covering all categories
├── 🐍 display_utils.py            # Styled HTML card renderer for Jupyter output
├── 🐍 generate_notebook.py        # Script used to generate the .ipynb (already run)
│
├── 📄 requirements.txt            # Python dependencies
├── 📄 README.md                   # Project documentation
├── 📄 CONTRIBUTORS.md             # Contributor guidelines
└── 📄 LICENSE                     # MIT License
```

---

## ⚙️ How It Works

```
Customer Message
      │
      ▼
┌─────────────────────────────────────────┐
│           processor.py                  │
│                                         │
│  1. Build structured prompt             │
│     (category list + sentiment list)    │
│                                         │
│  2. Call Cohere Chat API                │
│     model: command-a-03-2025            │
│                                         │
│  3. Parse JSON response                 │
│     { category, sentiment, auto_reply } │
└─────────────────────────────────────────┘
      │
      ▼
┌─────────────────────────────────────────┐
│          display_utils.py               │
│  Render styled HTML card in Jupyter     │
└─────────────────────────────────────────┘
      │
      ▼
  CSV Export  →  customer_support_results.csv
```

The prompt instructs the model to return a **strict JSON object** with exactly three keys. A regex-based parser handles edge cases where the model wraps output in markdown fences.

---

## 🚀 Setup

### 1. Clone the Repository

```bash
git clone https://github.com/whozahm3d/customer-support-ai.git
cd customer-support-ai
```

### 2. Install Dependencies

```bash
pip install cohere>=5.0.0
```

### 3. Get a Free Cohere API Key

Sign up at [dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys) — no credit card required.

### 4. Set Your API Key

Open `config.py` and replace the placeholder:

```python
COHERE_API_KEY = "your-actual-api-key-here"
```

### 5. Launch the Notebook

```bash
jupyter notebook Customer_Support_AI.ipynb
```

Then run **Kernel → Restart & Run All**.

---

## 📖 Usage

### Process a Single Message

```python
from processor import CustomerMessageProcessor

processor = CustomerMessageProcessor()

result = processor.process("I still haven't received my refund after 10 days!")

print(result["category"])    # Refund/Return
print(result["sentiment"])   # Negative
print(result["auto_reply"])  # We apologize for the delay in processing...
```

### Process Multiple Messages in Batch

```python
messages = [
    "Where is my order? It's been 2 weeks!",
    "Do you offer student discounts?",
    "Thank you, the product is amazing!",
]

results = processor.process_batch(messages)

for r in results:
    print(r["category"], "|", r["sentiment"])
```

### Export Results to CSV

```python
import csv

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "original_message", "category", "sentiment", "auto_reply"])
    writer.writeheader()
    for i, r in enumerate(results, 1):
        writer.writerow({"id": i, **{k: r[k] for k in ["original_message", "category", "sentiment", "auto_reply"]}})
```

---

## 📊 Output

### Notebook Cards

Each message renders as a color-coded card with:
- 🏷️ **Category badge** — unique color per category
- 💭 **Sentiment badge** — green / yellow / red
- 💬 **Auto-reply box** — blue-accented professional response

### CSV Export

| id | original_message | category | sentiment | auto_reply | status |
|---|---|---|---|---|---|
| 1 | I ordered a laptop... | Complaint | Negative | We sincerely apologize... | success |
| 2 | I'd like to return... | Refund/Return | Neutral | Thank you for reaching... | success |
| 3 | Do you have discounts... | Sales Inquiry | Positive | We'd love to help you... | success |

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| **Python 3.8+** | Core language |
| **Cohere API** (`command-a-03-2025`) | LLM for classification, sentiment & reply generation |
| **Jupyter Notebook** | Interactive execution environment |
| **IPython Display** | HTML card rendering inside notebook |
| **CSV module** | Results export |

---

## 📦 Dependencies

```txt
cohere>=5.0.0
```

No heavy ML frameworks required. The entire pipeline runs on a single lightweight API dependency.

---

## 🔮 Future Improvements

- [ ] Streamlit web interface for non-technical users
- [ ] Support for multilingual customer messages
- [ ] Confidence scores for category predictions
- [ ] Integration with email/helpdesk platforms (Zendesk, Freshdesk)
- [ ] Fine-tuned model on domain-specific support data
- [ ] Real-time processing via webhook

---

## 🤝 Contributing

We welcome contributions from the community! Whether you're fixing bugs, adding features, or improving documentation, your help is valued.

### Quick Start for Contributors

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/YOUR-USERNAME/customer-support-ai.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Make your changes** and test thoroughly
5. **Commit** with clear messages: `git commit -m "feat: Add your feature"`
6. **Push** to your fork: `git push origin feature/your-feature-name`
7. **Open a Pull Request** with a description of your changes

For detailed guidelines, please see [CONTRIBUTORS.md](CONTRIBUTORS.md).

### 🎯 Areas for Contribution

- 🐛 **Bug fixes** — Found an issue? Help fix it!
- ✨ **Features** — Have a great idea? Implement it!
- 📚 **Documentation** — Improve README or add examples
- 🧪 **Tests** — Add test cases
- ⚡ **Optimization** — Improve performance
- 🎨 **UI/UX** — Enhance styling and display

---

## 🙌 Acknowledgments

This project was developed with invaluable support from:

- **Claude AI** (Anthropic) — Code generation, architecture design, documentation, testing & debugging
- **Cohere** — Powerful language model API and free tier access

---

## 👤 Author

**Ali** — BS Data Science, FAST NUCES Lahore
- GitHub: [@whozahm3d](https://github.com/whozahm3d)

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <sub>Built with ❤️ using Cohere API · Python · Jupyter</sub>
</div>
