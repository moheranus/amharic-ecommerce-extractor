import json
import random

# Load all messages
with open('data/all_messages.json', 'r', encoding='utf-8') as f:
    all_messages = json.load(f)

# Filter valid messages (non-empty text and tokens)
valid_messages = [
    msg for msg in all_messages
    if msg.get('text', '').strip() and msg.get('tokens', [])
]

# Select exactly 30 valid messages
selected_messages = random.sample(valid_messages, min(30, len(valid_messages)))

# Save to file
with open('data/selected_messages.json', 'w', encoding='utf-8') as f:
    json.dump(selected_messages, f, ensure_ascii=False, indent=2)

print(f"Selected {len(selected_messages)} valid messages")