import json
import re
from typing import List, Tuple

# Placeholder for Amharic LLM (e.g., Amharic LLaVA-13B)
def call_amharic_llm(tokens: List[str], message_text: str) -> List[Tuple[str, str]]:
    """
    Placeholder for calling an Amharic LLM (e.g., Amharic LLaVA-13B).
    Replace with actual Hugging Face or API call.
    Returns list of (token, label) tuples.
    """
    # Example prompt for few-shot learning
    prompt = f"""
    Label the following tokens in CoNLL format for NER (entities: Product, Price, Location, Contact Info).
    Use B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, B-CONTACT_INFO, I-CONTACT_INFO, O.
    Example 1:
    Input: ["Hair", "Dye", "200", "ብር", "ገርጂ"]
    Output:
    Hair B-Product
    Dye I-Product
    200 B-PRICE
    ብር I-PRICE
    ገርጂ B-LOC

    Example 2:
    Input: ["Silicone", "Baby", "150", "ml", "2200", "birr"]
    Output:
    Silicone B-Product
    Baby I-Product
    150 B-PRICE
    ml I-PRICE
    2200 I-PRICE
    birr I-PRICE

    Tokens: {tokens}
    Full text: {message_text}
    Output in CoNLL format:
    """

    # TODO: Replace with actual LLM call (e.g., Hugging Face transformers)
    # from transformers import pipeline
    # nlp = pipeline("text-generation", model="path/to/amharic-llava-13b")
    # response = nlp(prompt, max_length=1000)
    # Parse response to extract token-label pairs
    # For now, return rule-based labels as fallback
    return rule_based_labeling(tokens)

def rule_based_labeling(tokens: List[str]) -> List[Tuple[str, str]]:
    """Rule-based fallback for labeling tokens."""
    price_indicators = {'ብር', 'birr', 'ዋጋ', 'ml'}
    location_indicators = {'ገርጂ', 'አዲስ', 'አበባ', '4ኪሎ', 'ቅድስት', 'ስላሴ', 'መገናኛ', 'ዘፍመሽ', 
                          'ጀሞ', 'ኢምፔሪያል', 'አልፎዝ', 'ፕላዛ', 'ህንፃ', 'ፎቅ', 'Mall', 'Building', 'Floor'}
    product_indicators = {'Bottle', 'ልብስ', 'ቦትል', 'Silicone', 'Baby', 'Water', 'Dye', 'Brush', 
                         'Nano', 'Liquid', 'Breast', 'Milk', 'Wide', 'Mouth', 'Outdoor', 'Handle', 'Straw'}
    contact_indicators = {'@', 'httpstme', '090', '094', '099'}

    labels = []
    for i, token in enumerate(tokens):
        prev_token = tokens[i-1] if i > 0 else None
        if token.isdigit():
            label = 'B-PRICE'
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
    return labels

# Load selected messages
try:
    with open('data/selected_messages.json', 'r', encoding='utf-8') as f:
        messages = json.load(f)
except FileNotFoundError:
    print("Error: data/selected_messages.json not found. Run scripts/select_messages.py first.")
    exit(1)

# Generate CoNLL output
conll_lines = []
for msg in messages:
    tokens = msg['tokens']
    text = msg['text']
    labeled_tokens = call_amharic_llm(tokens, text)  # Replace with actual LLM call if available
    for token, label in labeled_tokens:
        conll_lines.append(f"{token} {label}")
    conll_lines.append("")  # Blank line between messages

# Save to CoNLL file
with open('data/labeled_data.conll', 'w', encoding='utf-8') as f:
    f.write('\n'.join(conll_lines))

print("Initial labels saved to data/labeled_data.conll")
print("Please review and edit the file manually to correct errors.")
print("To use an Amharic LLM, replace call_amharic_llm with an API call (e.g., Amharic LLaVA-13B).")