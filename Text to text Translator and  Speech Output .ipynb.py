# Code for text to text to speech (This will use in Py-Charm! or VS Code)

from deep_translator import GoogleTranslator  # Importing GoogleTranslator for translating text
from gtts import gTTS                        # Importing gTTS (Google Text-to-Speech) to convert text to audio
from io import BytesIO                       # Importing BytesIO to handle audio in memory (like a virtual file)

# Function to translate the given text into the destination language
def translate_text(text, dest_lang):
    translated_text = GoogleTranslator(source='en', target=dest_lang).translate(text)  # Translate text from English to destination language
    return translated_text  # Return the translated text

# Function to convert translated text to speech (audio)
def text_to_speech(text, dest_lang):
    tts = gTTS(text=text, lang=dest_lang)  # Create a text-to-speech object with the translated text and language
    with BytesIO() as buffer:              # Create a virtual file (buffer) to store the audio temporarily
        tts.write_to_fp(buffer)            # Write the audio data into the buffer
        buffer.seek(0)                     # Move to the beginning of the buffer
        audio_data = buffer.read()         # Read the audio data from the buffer
    return audio_data  # Return the audio data

# Original English text to be translated and converted to speech
text = "In simple terms, robotics combines science, engineering, and technology to design, construct, operate, and use machines programmed to replicate, substitute, or assist humans in completing tasks of varying complexity. These machines are known as robots."

dest_lang = 'ur'  # Destination language code (e.g., 'ur' for Urdu, 'te' for Telugu, 'hi' for Hindi, etc.)

translated_text = translate_text(text, dest_lang)  # Call function to translate the English text

tts_audio = text_to_speech(translated_text, dest_lang)  # Call function to convert translated text to audio

# Save the audio data to a file named "translated_audio.mp3"
with open("translated_audio.mp3", "wb") as audio_file:
    audio_file.write(tts_audio)  # Write the audio content to the MP3 file
