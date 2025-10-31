import openai
import json

# 🔑 Replace with your actual API key
openai.api_key = ""

def test_api_key():
    try:
        models = openai.models.list()
        print("✅ API key is valid. Available models:")
        for model in models.data:
            print("-", model.id)
    except Exception as e:
        print("❌ API key test failed:", e)

def test_file_upload():
    try:
        file = openai.files.create(file=open("train_split.jsonl", "rb"), purpose="fine-tune")
        print("✅ File uploaded successfully. File ID:", file.id)
        return file.id
    except Exception as e:
        print("❌ File upload failed:", e)
        return None

def test_finetune_launch(file_id):
    try:
        job = openai.fine_tuning.jobs.create(
            training_file=file_id,
            model="gpt-3.5-turbo"
        )
        print("✅ Fine-tune launched. Job ID:", job.id)
    except Exception as e:
        print("❌ Fine-tune launch failed:", e)

if __name__ == "__main__":
    print("🔍 Testing OpenAI fine-tuning setup...\n")
    test_api_key()
    print("\n📁 Uploading training file...\n")
    file_id = test_file_upload()
    if file_id:
        print("\n🚀 Attempting to launch fine-tune...\n")

        test_finetune_launch(file_id)
