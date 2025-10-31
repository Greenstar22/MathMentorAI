import json
import random

# Load all lines from train.jsonl
with open("train.jsonl", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Shuffle the lines to randomize the split
random.shuffle(lines)

# Split 90% train, 10% validation
split_index = int(len(lines) * 0.9)
train_lines = lines[:split_index]
valid_lines = lines[split_index:]

# Save the split files
with open("train_split.jsonl", "w", encoding="utf-8") as f:
    f.writelines(train_lines)

with open("valid_split.jsonl", "w", encoding="utf-8") as f:
    f.writelines(valid_lines)

print(f"Split complete: {len(train_lines)} training examples, {len(valid_lines)} validation examples.")