from openai import OpenAI
import os


model_id = ""
baseten_api_key = os.environ["BASETEN_API_KEY"]

client = OpenAI(
    api_key=baseten_api_key,
    base_url=f"https://bridge.baseten.co/{model_id}/direct/v1"
)

response = client.chat.completions.create(
    model="fixie-ai/ultravox-v0.2",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Tell me about the Ultravox model."}
    ],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta)