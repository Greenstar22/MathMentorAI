import json

# Define the system instruction that will be included in every training example
system_prompt = (
    "You are MathMentor-Grader. Given a math question, a student's answer, "
    "and the correct answer, determine if the student is correct. "
    "If incorrect, identify the misconception. Always output JSON with fields: "
    "is_correct, misconception, topic."
)

# Load your original JSON file (an array of objects)
with open("data_asciimath.json", "r", encoding="utf-8") as f:
    items = json.load(f)

# Open the output file in JSONL format
with open("train.jsonl", "w", encoding="utf-8") as out:
    for ex in items:
        # Build the user payload with only the fields you want
        user_payload = {
            "Question": ex["Question"],
            "Incorrect_answer": ex["Incorrect Answer"],
            "Correct_answer": ex["Correct Answer"]
        }

        # Build the gold response (what the model should learn to output)
        gold_response = {
            "is_correct": ex["Incorrect Answer"] == ex["Correct Answer"],
            "misconception": ex["Misconception"] if ex["Incorrect Answer"] != ex["Correct Answer"] else "",
            "Topic": ex["Topic"]
        }
    
        # Wrap into the fine-tuning format
        record = {
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": json.dumps(user_payload, ensure_ascii=False)}
            ],
            "response": json.dumps(gold_response, ensure_ascii=False)
        }

        # Write one JSON object per line
        out.write(json.dumps(record, ensure_ascii=False) + "\n")

print("Conversion complete. File saved as train.jsonl")