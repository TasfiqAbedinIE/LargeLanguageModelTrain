import re

with open("the-verdict.txt", 'r', encoding='utf-8') as f:
    raw_text = f.read()

print(f"Total number of charecter: {len(raw_text)}")
print(raw_text[:60])


text_to_split = raw_text[:60]
# result = re.split(r'(\s)', text_to_split)
result = re.split(r'([,.]\s)', text_to_split)
print(result)