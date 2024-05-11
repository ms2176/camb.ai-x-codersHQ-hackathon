##API key: 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
import streamlit as st
import requests
import time

from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq

from pydub import AudioSegment
from pydub.playback import play

def main():
    st.title("Narrative Nexus")

    # Text input
    system = "You are a helpful assistant."
    human = st.text_area("Enter your text here:", "")

    chat = ChatGroq(temperature=0, groq_api_key="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", model_name="llama3-8b-8192")

    if st.button("Generate Story"):
        if human.strip() == "":
            st.error("Please enter some text.")
        else:
            prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])
            chain = prompt | chat
            chain.invoke({"text": "write a cinderella story from once upon a time"})
            
            Story = ""
            for chunk in chain.stream({"topic": "once upon a time"}):
                Story += chunk.content

            # Text output
            st.markdown("## Story:")
            st.write(Story)

            # Generate audio
            API_KEY = "d346f052-a0d2-451b-a3d4-b2e4e50ffb7f"
            url = "https://client.camb.ai/apis/tts"
            selected_language_voices = {"id": 8899, "gender": 1, "age": 30}  # Default voice
            payload = {
                "text": Story,
                "voice_id": selected_language_voices["id"],
                "language": 1,
                "gender": selected_language_voices["gender"],
                "age": selected_language_voices["age"]
            }

            headers = {
                "x-api-key": API_KEY,
                "Content-Type": "application/json"
            }
            response = requests.post(url, json=payload, headers=headers)
            response.raise_for_status()
            task_id = response.json().get('task_id')

            # Polling for run_id
            url = f"https://client.camb.ai/apis/tts/{task_id}"
            while True:
                response1 = requests.get(url, headers={"x-api-key": API_KEY})
                if response1.status_code == 200:
                    run_id = response1.json().get('run_id')
                    if run_id:
                        break
                time.sleep(5)

            # Polling for TTS result
            url2 = f"https://client.camb.ai/apis/tts_result/{run_id}"
            while True:
                response2 = requests.get(url2, headers={"x-api-key": API_KEY})
                if response2.status_code == 200:
                    break
                elif response2.status_code == 404:
                    time.sleep(5)

            # Download and play audio
            tts_result = requests.get(url2, headers={"x-api-key": API_KEY}, stream=True)
            with open("saved_stream.wav", "wb") as f:
                f.write(tts_result.content)

            st.markdown("## Audio Output:")
            st.audio("saved_stream.wav", format='audio/wav')

if __name__ == "__main__":
    main()
