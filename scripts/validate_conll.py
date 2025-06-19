valid_labels = {'B-Product', 'I-Product', 'B-LOC', 'I-LOC', 'B-PRICE', 'I-PRICE', 'O', 
                'B-CONTACT_INFO', 'I-CONTACT_INFO', 'B-DELIVERY_FEE', 'I-DELIVERY_FEE'}
message_count = 0
with open('data/labeled_data.conll', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines, 1):
    line = line.strip()
    if not line:
        message_count += 1
        continue
    parts = line.split()
    if len(parts) != 2:
        print(f"Error at line {i}: {line} (Expected 'token label')")
        continue
    token, label = parts
    if label not in valid_labels:
        print(f"Invalid label at line {i}: {label}")

print(f"Found {message_count} messages in CoNLL file.")
if message_count < 30:
    print("Warning: Fewer than 30 messages labeled. Task requires 30–50.")