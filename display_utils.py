"""
display_utils.py — Jupyter HTML rendering for Customer Support AI results.
Provides styled cards showing: original message · category · sentiment · auto-reply.
"""

from IPython.display import display, HTML


# ------------------------------------------------------------------
# Color palettes
# ------------------------------------------------------------------
CATEGORY_COLORS = {
    "Complaint":               ("#dc3545", "#ffffff"),
    "Refund/Return":           ("#fd7e14", "#ffffff"),
    "Sales Inquiry":           ("#0d6efd", "#ffffff"),
    "Delivery Question":       ("#6f42c1", "#ffffff"),
    "Account/Technical Issue": ("#0dcaf0", "#000000"),
    "General Query":           ("#6c757d", "#ffffff"),
    "Spam":                    ("#212529", "#ffffff"),
}

SENTIMENT_CONFIG = {
    "Positive": {"bg": "#d1e7dd", "text": "#0a3622", "border": "#28a745", "icon": "✅"},
    "Neutral":  {"bg": "#fff3cd", "text": "#664d03", "border": "#ffc107", "icon": "➖"},
    "Negative": {"bg": "#f8d7da", "text": "#58151c", "border": "#dc3545", "icon": "❌"},
}


# ------------------------------------------------------------------
# Badge builders
# ------------------------------------------------------------------
def _category_badge(category: str) -> str:
    bg, fg = CATEGORY_COLORS.get(category, ("#6c757d", "#ffffff"))
    return (
        f'<span style="background:{bg};color:{fg};padding:5px 13px;'
        f'border-radius:20px;font-size:12px;font-weight:700;'
        f'letter-spacing:.4px;white-space:nowrap;">'
        f'{category}</span>'
    )


def _sentiment_badge(sentiment: str) -> str:
    cfg = SENTIMENT_CONFIG.get(sentiment, SENTIMENT_CONFIG["Neutral"])
    return (
        f'<span style="background:{cfg["bg"]};color:{cfg["text"]};'
        f'border:1.5px solid {cfg["border"]};padding:5px 13px;'
        f'border-radius:20px;font-size:12px;font-weight:700;">'
        f'{cfg["icon"]}&nbsp;{sentiment}</span>'
    )


def _status_badge(status: str) -> str:
    if status == "success":
        return ""
    return (
        f'<span style="background:#fff3cd;color:#664d03;border:1px solid #ffc107;'
        f'padding:3px 8px;border-radius:8px;font-size:11px;margin-left:8px;">'
        f'⚠️ {status[:60]}</span>'
    )


# ------------------------------------------------------------------
# Main render functions
# ------------------------------------------------------------------
def render_banner() -> None:
    """Display the pipeline startup banner."""
    html = """
    <div style="background:linear-gradient(135deg,#1a1a2e 0%,#16213e 60%,#0f3460 100%);
                padding:32px 28px;border-radius:14px;margin:8px 0 20px 0;
                font-family:'Segoe UI',Arial,sans-serif;text-align:center;
                box-shadow:0 4px 20px rgba(0,0,0,.25);">
      <div style="font-size:42px;margin-bottom:10px;">🤖</div>
      <h1 style="color:#ffffff;margin:0 0 8px 0;font-size:26px;font-weight:700;
                 letter-spacing:.5px;">
        Customer Support AI Pipeline
      </h1>
      <p style="color:#a0b4c8;margin:0 0 18px 0;font-size:14px;">
        Powered by&nbsp;<strong style="color:#56cfaf;">Cohere API</strong>
        &nbsp;·&nbsp; Classification &nbsp;·&nbsp; Sentiment Analysis &nbsp;·&nbsp; Auto-Reply Generation
      </p>
      <div style="display:inline-flex;gap:10px;flex-wrap:wrap;justify-content:center;">
        <span style="background:rgba(255,255,255,.1);color:#cfe2ff;padding:4px 14px;
                     border-radius:20px;font-size:12px;font-weight:600;">📂 7 Categories</span>
        <span style="background:rgba(255,255,255,.1);color:#cfe2ff;padding:4px 14px;
                     border-radius:20px;font-size:12px;font-weight:600;">💭 3 Sentiments</span>
        <span style="background:rgba(255,255,255,.1);color:#cfe2ff;padding:4px 14px;
                     border-radius:20px;font-size:12px;font-weight:600;">⚡ 1 API Call / Message</span>
      </div>
    </div>
    """
    display(HTML(html))


def render_result(result: dict, index: int = None) -> None:
    """Render a single processed message as a styled HTML card."""
    label    = f"Message #{index}" if index is not None else "Custom Message"
    cat_b    = _category_badge(result.get("category", "General Query"))
    sent_b   = _sentiment_badge(result.get("sentiment", "Neutral"))
    status_b = _status_badge(result.get("status", "success"))
    message  = result.get("original_message", "")
    reply    = result.get("auto_reply", "")

    # Truncate long messages for display
    display_msg = message if len(message) <= 220 else message[:217] + "…"

    html = f"""
    <div style="border:1px solid #dee2e6;border-radius:12px;padding:22px 24px;
                margin:14px 0;background:#ffffff;
                box-shadow:0 2px 8px rgba(0,0,0,.07);
                font-family:'Segoe UI',Arial,sans-serif;">

      <!-- Header row -->
      <div style="display:flex;align-items:center;justify-content:space-between;
                  margin-bottom:12px;flex-wrap:wrap;gap:6px;">
        <span style="font-size:12px;color:#6c757d;font-weight:600;letter-spacing:.6px;
                     text-transform:uppercase;">{label}</span>
        {status_b}
      </div>

      <!-- Original message -->
      <div style="background:#f8f9fa;border-left:4px solid #adb5bd;
                  padding:10px 16px;border-radius:0 8px 8px 0;
                  margin-bottom:16px;color:#495057;font-style:italic;
                  font-size:14px;line-height:1.65;">
        &ldquo;{display_msg}&rdquo;
      </div>

      <!-- Badges row -->
      <div style="display:flex;gap:16px;flex-wrap:wrap;margin-bottom:16px;
                  align-items:flex-start;">
        <div>
          <div style="font-size:10px;color:#6c757d;font-weight:700;letter-spacing:.8px;
                      text-transform:uppercase;margin-bottom:5px;">Category</div>
          {cat_b}
        </div>
        <div>
          <div style="font-size:10px;color:#6c757d;font-weight:700;letter-spacing:.8px;
                      text-transform:uppercase;margin-bottom:5px;">Sentiment</div>
          {sent_b}
        </div>
      </div>

      <!-- Auto-reply -->
      <div>
        <div style="font-size:10px;color:#6c757d;font-weight:700;letter-spacing:.8px;
                    text-transform:uppercase;margin-bottom:6px;">Auto-Reply</div>
        <div style="background:#e8f4fd;border-left:4px solid #0d6efd;
                    padding:12px 16px;border-radius:0 8px 8px 0;
                    color:#1a1a2e;font-size:14px;line-height:1.7;">
          💬 &nbsp;{reply}
        </div>
      </div>

    </div>
    """
    display(HTML(html))


def render_batch(results: list) -> None:
    """Render all results with a summary header."""
    success  = sum(1 for r in results if r.get("status") == "success")
    total    = len(results)

    header = f"""
    <div style="font-family:'Segoe UI',Arial,sans-serif;padding:8px 0 4px 0;">
      <h2 style="color:#1a1a2e;margin:0 0 4px 0;font-size:20px;">
        📊 Pipeline Results
      </h2>
      <p style="color:#6c757d;margin:0;font-size:13px;">
        {success}/{total} messages processed successfully via Cohere API
      </p>
      <hr style="border:none;border-top:2px solid #e9ecef;margin:12px 0 4px 0;">
    </div>
    """
    display(HTML(header))

    for i, result in enumerate(results, start=1):
        render_result(result, index=i)


def render_summary_table(results: list) -> None:
    """Render a compact summary table of all results."""
    rows = ""
    for i, r in enumerate(results, start=1):
        cat  = r.get("category", "—")
        sent = r.get("sentiment", "—")
        bg, fg = CATEGORY_COLORS.get(cat, ("#6c757d", "#fff"))
        s_cfg  = SENTIMENT_CONFIG.get(sent, SENTIMENT_CONFIG["Neutral"])
        msg_short = r["original_message"][:60] + ("…" if len(r["original_message"]) > 60 else "")
        rows += f"""
        <tr>
          <td style="padding:8px 12px;font-size:13px;color:#495057;">#{i}</td>
          <td style="padding:8px 12px;font-size:13px;color:#212529;font-style:italic;">"{msg_short}"</td>
          <td style="padding:8px 12px;">
            <span style="background:{bg};color:{fg};padding:3px 10px;border-radius:12px;font-size:11px;font-weight:700;">{cat}</span>
          </td>
          <td style="padding:8px 12px;">
            <span style="background:{s_cfg['bg']};color:{s_cfg['text']};border:1px solid {s_cfg['border']};
                         padding:3px 10px;border-radius:12px;font-size:11px;font-weight:700;">
              {s_cfg['icon']} {sent}
            </span>
          </td>
        </tr>"""

    html = f"""
    <div style="font-family:'Segoe UI',Arial,sans-serif;margin:16px 0;">
      <h3 style="color:#1a1a2e;margin:0 0 10px 0;">📋 Quick Summary</h3>
      <table style="width:100%;border-collapse:collapse;background:#fff;
                    border:1px solid #dee2e6;border-radius:10px;overflow:hidden;
                    box-shadow:0 2px 6px rgba(0,0,0,.06);">
        <thead>
          <tr style="background:#f8f9fa;">
            <th style="padding:10px 12px;text-align:left;font-size:11px;color:#6c757d;
                       font-weight:700;letter-spacing:.6px;text-transform:uppercase;">#</th>
            <th style="padding:10px 12px;text-align:left;font-size:11px;color:#6c757d;
                       font-weight:700;letter-spacing:.6px;text-transform:uppercase;">Message</th>
            <th style="padding:10px 12px;text-align:left;font-size:11px;color:#6c757d;
                       font-weight:700;letter-spacing:.6px;text-transform:uppercase;">Category</th>
            <th style="padding:10px 12px;text-align:left;font-size:11px;color:#6c757d;
                       font-weight:700;letter-spacing:.6px;text-transform:uppercase;">Sentiment</th>
          </tr>
        </thead>
        <tbody>{rows}</tbody>
      </table>
    </div>
    """
    display(HTML(html))
