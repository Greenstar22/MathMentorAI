import openai
import time

# 🔑 Set your API key
openai.api_key = ""

# 📁 Upload training and validation files
train_file = openai.files.create(file=open("train_split.jsonl", "rb"), purpose="fine-tune")
valid_file = openai.files.create(file=open("valid_split.jsonl", "rb"), purpose="fine-tune")

print("Training file ID:", train_file.id)
print("Validation file ID:", valid_file.id)

# 🚀 Launch fine-tune
job = openai.fine_tuning.jobs.create(
    training_file=train_file.id,
    validation_file=valid_file.id,
    model="gpt-4.1-mini",
    hyperparameters={
        "n_epochs": 5,
        "learning_rate_multiplier": 0.1
    }
)

print("Fine-tune job started:", job.id)

# 📊 Monitor progress
print("\nMonitoring training progress...\n")
while True:
    events = openai.fine_tuning.jobs.list_events(id=job.id)
    for event in events.data[-5:]:
        print(f"[{event.created_at}] {event.message}")
    job_status = openai.fine_tuning.jobs.retrieve(id=job.id).status
    if job_status in ["succeeded", "failed", "cancelled"]:
        print(f"\nTraining finished with status: {job_status}")
        break
    time.sleep(10)

# 🧪 Test the fine-tuned model
fine_tuned_model = openai.fine_tuning.jobs.retrieve(id=job.id).fine_tuned_model
response = openai.chat.completions.create(
    model=fine_tuned_model,
    messages=[{"role": "user", "content": "What is 7 × 8?"}]
)


print("\nModel response:", response.choices[0].message.content)
