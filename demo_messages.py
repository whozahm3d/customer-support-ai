"""
demo_messages.py — Sample customer messages for pipeline demonstration.
Covers all 7 categories and a range of sentiments.
"""

DEMO_MESSAGES = [
    {
        "id": 1,
        "tag": "Complaint",
        "message": (
            "I ordered a laptop from your website two weeks ago and it still hasn't arrived! "
            "The tracking page hasn't updated in 5 days and no one from support has responded "
            "to my emails. This is absolutely unacceptable — I need answers NOW!"
        ),
    },
    {
        "id": 2,
        "tag": "Refund/Return",
        "message": (
            "Hi, I'd like to return a jacket I purchased last week. Unfortunately it doesn't "
            "fit correctly and the colour looks different from the photos online. Could you "
            "please guide me through the return process and confirm I'll receive a full refund?"
        ),
    },
    {
        "id": 3,
        "tag": "Sales Inquiry",
        "message": (
            "Hello! I'm interested in your premium annual subscription. Do you offer any "
            "student discounts or bundle deals? Also, can I try it free before committing "
            "to a paid plan?"
        ),
    },
    {
        "id": 4,
        "tag": "Delivery Question",
        "message": (
            "My tracking number shows my order is still 'In Transit' after 6 days. "
            "The estimated delivery was last Tuesday. Can you check what's going on "
            "and give me an updated delivery estimate?"
        ),
    },
    {
        "id": 5,
        "tag": "Account/Technical Issue",
        "message": (
            "I'm completely locked out of my account. I tried resetting my password "
            "three times but the reset email never arrives — not even in spam. "
            "I have an important meeting tomorrow and urgently need access to my files."
        ),
    },
    {
        "id": 6,
        "tag": "General Query (Positive)",
        "message": (
            "Just wanted to drop a note to say how impressed I am with your service! "
            "The product arrived two days early, packaging was perfect, and the quality "
            "exceeded my expectations. I'll definitely be recommending you to friends!"
        ),
    },
    {
        "id": 7,
        "tag": "Spam",
        "message": (
            "CONGRATULATIONS!!! You have WON a FREE iPhone 15!!! "
            "CLICK HERE NOW >>> www.claimprize.xyz <<< "
            "LIMITED TIME ONLY!!! ACT FAST!!! 🎁🎁🎁"
        ),
    },
]
