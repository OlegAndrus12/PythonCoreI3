import re

chat = (
    "Hi, my card is 4111 1111 1111 1111 and I can't complete payment. "
    "I also tried 5500-0000-0000-0004 but same issue."
)

# \b        — word boundary (no digits before/after the card number)
# (\d{4})   — capture group: exactly 4 digits  (repeated 4 times)
# [\s-]     — separator between groups: space or dash
# \4        — backreference to group 4 (last 4 digits kept visible)

masked = re.sub(r"\b(\d{4})[\s-](\d{4})[\s-](\d{4})[\s-](\d{4})\b", r"**** **** **** \4", chat)
print(masked)
