import json

# Load selected messages
try:
    with open('data/selected_messages.json', 'r', encoding='utf-8') as f:
        messages = json.load(f)
except FileNotFoundError:
    print("Error: data/selected_messages.json not found. Run scripts/select_messages.py first.")
    exit(1)

# Ensure exactly 30 messages
messages = messages[:30]
print(f"Selected {len(messages)} messages for labeling")

# Print messages for sharing
for i, msg in enumerate(messages, 1):
    print(f"\nMessage {i}:")
    print(f"Text: {msg['text']}")
    print(f"Tokens: {msg['tokens']}")
    print("-" * 50)

print("\nShare the above messages (text and tokens) to get label suggestions.")
print("After receiving labels, manually add them to data/labeled_data.conll.")