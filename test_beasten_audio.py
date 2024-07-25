import requests
import base64
import time

# Assuming you have the BASETEN_API_KEY environment variable set
baseten_api_key = "l1ovI2c6.fxn1Mr8VphKnscRM5FSVYGdsFu8WrT5Q"
model_id = "jwd76pnw"  # You should replace this with your actual model ID

# Path to your audio file
audio_file_path = 'C:\\Users\\susha\\Desktop\\test-ultra\\Question.wav'

# Read and encode the audio file
with open(audio_file_path, "rb") as audio_file:
    base64_wav = base64.b64encode(audio_file.read()).decode('utf-8')

# Form the request
start_time = time.time()
resp = requests.post(
    f"https://model-{model_id}.api.baseten.co/production/predict",
    headers={"Authorization": f"Api-Key {baseten_api_key}"},
    json={"messages": 
      [{
          "role": "user",
          "content": [
              {"type": "text", "text": "Summarize the following: "},
              {"type": "image_url", "image_url": {"url": f"data:audio/wav;base64,{base64_wav}"}}
          ]
      }], 
    "stream": False
  },
)

# Handle the response
resp = resp.json()
end_time = time.time()

# Calculate and print execution time
execution_time = end_time - start_time
print("Execution time (in seconds):", execution_time)

print(resp['choices'][0]['message']['content'])
