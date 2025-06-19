import json

# Load selected messages
with open('data/selected_messages.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)

# Initialize CoNLL output
conll_lines = []

for i, msg in enumerate(messages, 1):
    print(f"\nMessage {i}: {msg['text']}")
    print("Tokens:", msg['tokens'])
    print("Label each token (e.g., B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, O):")
    
    # Example: Manually add labels (replace with your labels)
    # You can modify this to accept input or hardcode labels
    labels = []
    for token in msg['tokens']:
        # Placeholder: Replace with actual labeling logic
        label = input(f"Label for '{token}': ") if token.strip() else 'O'
        labels.append(label)
    
    # Add to CoNLL lines
    for token, label in zip(msg['tokens'], labels):
        conll_lines.append(f"{token} {label}")
    conll_lines.append("")  # Blank line between messages

# Save to CoNLL file
with open('data/labeled_data.conll', 'w', encoding='utf-8') as f:
    f.write('\n'.join(conll_lines))

print("Labeled data saved to data/labeled_data.conll")