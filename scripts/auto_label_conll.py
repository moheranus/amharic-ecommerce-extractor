import json
import re
from typing import List, Tuple

def rule_based_labeling(tokens: List[str], text: str) -> List[Tuple[str, str]]:
    """Apply rule-based labeling for NER based on observed patterns."""
    price_indicators = {'ብር', 'birr', 'PRICE', 'price'}
    location_indicators = {'ሜክሲኮ', 'ድሬዳዋ', 'አሸዋ', 'ሚና', 'ህንፃ', 'ፎቅ', 'መገናኛ', 'ማራቶን', 'ገበያ', 'ማእከል', 
                         'መግቢያ', 'መሬት', 'ላይ', 'ግራውንድ', 'በስተቀኝ', 'በመጀመሪያው', 'ሱቅቁ', 'ቁጥር', 'አዲስ', 'አበባ'}
    product_indicators = {'PUMA', 'SPIREX', 'SKECHERS', 'QUANTUM', 'FLEX', 'COTTON', 'TISHERTS', 'HP', 'ELITEBOOK', 'ቦርሳ', 'የሴቶች', 
                         'Under', 'armour', 'Curry', '11ORIGINAL', 'Silicone', 'Baby', 'Water', 'Bottle', 'Hair', 'Dye', 'Brush'}
    contact_indicators = {'@', 'httpstme', '094', '098', '097', 'www'}

    labels = []
    prev_token = None
    for i, token in enumerate(tokens):
        if token.isdigit() or re.match(r'^\d+$', token):
            label = 'B-PRICE' if prev_token not in price_indicators else 'I-LOC' if prev_token in location_indicators else 'O'
        elif token in price_indicators:
            label = 'I-PRICE'
        elif token in location_indicators:
            label = 'B-LOC' if prev_token not in location_indicators else 'I-LOC'
        elif token in product_indicators:
            label = 'B-Product' if prev_token not in product_indicators else 'I-Product'
        elif any(token.startswith(prefix) for prefix in contact_indicators) or re.match(r'^\d{10}$', token):
            label = 'B-CONTACT_INFO'
        else:
            label = 'O'
        labels.append((token, label))
        prev_token = token
    return labels

# Load selected messages
try:
    with open('data/selected_messages.json', 'r', encoding='utf-8') as f:
        messages = json.load(f)
except FileNotFoundError:
    print("Error: data/selected_messages.json not found. Run scripts/select_messages.py first.")
    exit(1)

# Ensure exactly 30 messages
messages = messages[:30]
print(f"Processing {len(messages)} messages")

# Generate CoNLL output
conll_lines = []
for msg in messages:
    tokens = msg['tokens']
    text = msg['text']
    labeled_tokens = rule_based_labeling(tokens, text)
    for token, label in labeled_tokens:
        conll_lines.append(f"{token} {label}")
    conll_lines.append("")  # Blank line between messages

# Save to CoNLL file
with open('data/labeled_data.conll', 'w', encoding='utf-8') as f:
    f.write('\n'.join(conll_lines))

print("Initial labels saved to data/labeled_data.conll")
print("Please review and edit the file manually to correct errors.")