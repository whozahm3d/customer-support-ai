# ============================================================
#  config.py  —  Customer Support AI Pipeline
#  Set your Cohere API key here before running the notebook.
#  Get a free key at: https://dashboard.cohere.com/api-keys
# ============================================================

COHERE_API_KEY = "YOUR_API_KEY_HERE"  # replace with your actual API key 

COHERE_MODEL = "command-a-03-2025"   # free-tier model

CATEGORIES = [
    "Complaint",
    "Refund/Return",
    "Sales Inquiry",
    "Delivery Question",
    "Account/Technical Issue",
    "General Query",
    "Spam",
]

SENTIMENTS = ["Positive", "Neutral", "Negative"]
