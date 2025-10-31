import json

def restructure_for_openai(input_path, output_path):
    new_data = []

    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            entry = json.loads(line)
            if "messages" in entry and "response" in entry:
                entry["messages"].append({
                    "role": "assistant",
                    "content": entry["response"]
                })
                new_data.append({ "messages": entry["messages"] })

    with open(output_path, 'w', encoding='utf-8') as f:
        for item in new_data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')

    print(f"✅ Restructured data saved to: {output_path}")

restructure_for_openai('valid_split.jsonl', 'valid_split_formatted.jsonl')