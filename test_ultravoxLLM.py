# pip install transformers librosa

import transformers
import numpy as np
import librosa
import time

# Initialize the pipeline with the multimodal model
pipe = transformers.pipeline(model='fixie-ai/ultravox-v0_2', trust_remote_code=True)

# Load the audio file
path = "webserver.wav"
audio, sr = librosa.load(path, sr=16000)

# Define the multimodal input with both text and speech
turns = [
    {
        "role": "system",
        "content": "You are a friendly and helpful character. You love to answer questions for people."
    },
]

# Prepare input data
input_data = {'audio': audio, 'turns': turns, 'sampling_rate': sr}

# Testing performance
start_time = time.time()
response = pipe(input_data, max_new_tokens=30)
end_time = time.time()

# Calculate and print execution time
execution_time = end_time - start_time
print("Execution time (in seconds):", execution_time)

# Print the output to review model's response for fluency
print("Model response:", response)
