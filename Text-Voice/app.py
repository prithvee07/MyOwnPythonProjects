import requests
from TTS.api import TTS
import os

# Step 1: Query Ollama
def get_ollama_response("prompt"):
    response = requests.post("http://localhost:11434/api/generate", json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    })
    return response.json()["response"]

# Step 2: Convert text to speech
def text_to_speech(text, filename="response.wav"):
    tts = TTS(model_name="tts_models/en/ljspeech/glow-tts", gpu=False)
    tts.tts_to_file(text=text, file_path=filename)
    print(f"✅ Audio saved to {filename}")

# Step 3: Combine it all
def main():
    prompt = input("🧠 Enter a prompt for Ollama: ")
    response = get_ollama_response(prompt)
    print("📝 LLM says:", response)
    
    os.makedirs("outputs", exist_ok=True)
    output_file = f"outputs/ollama_response.wav"
    text_to_speech(response, output_file)

if __name__ == "__main__":
    main()
