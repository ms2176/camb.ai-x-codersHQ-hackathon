# CAMBAI-Hackathon
This repo contains the project made for the CAMB AI x CodersHQ hackathon. 
Segments of the project:
* GPEC
* Story Telling 

## GPEC
  
The main objective of the the GPEC was to allow the user to record a video of them speaking in a language and using the CAMB AI the video could be dubbed to any language of their desire.

`AVrecordeR.py` : This file contains the code for recording video and audio combining it into one. This was branched from https://github.com/bunkahle/AVrecordeR 

`run.py` : This file is used to run the AVrecoderR file.

`uploading.py` : Script to upload videos to catbox and get a link for it.

`dub.py` : Script used to access the api key and dub the video.

`sending_mail.py` : Script to send email to the user using SMTP.

`frontend.py` : Script to pipeline all the process (GUI still in development).


## Narrative Nexus

Narrative Nexus is a Streamlit application that generates a story based on user input and converts the story into speech.

### Installation

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages.

### Usage

1. Run the Streamlit app.
2. Open the provided URL in your web browser.
3. Enter your text in the text area and click the "Generate Story" button.
4. The application will generate a story based on your input and display it on the page.
5. The application will also convert the story into speech and play the audio.

### Features

- Text-to-speech conversion: The application uses the Camb.ai Text-to-Speech API to convert the generated story into speech.
- Story generation: The application uses the Langchain Groq API to generate a story based on user input.

### Dependencies

- Streamlit
- Requests
- Time
- Langchain Core
- Langchain Groq
- PyDub

#### Note: Replicating this code would require you to purchase CAMB AI api for TTS, Dubbing etc.


