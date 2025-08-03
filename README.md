# 🎙️ Text Translator & Speech Generator using Python

This Python project allows you to **translate any English text into another language** and then **convert the translated text into speech (audio)** — all in one go!

Whether you're working with Urdu, Hindi, Telugu, or any other supported language, this tool gives you both the translated version and the spoken audio file.

---

## 🔧 What This Project Does

✅ Translates text from **English** into another language (you choose the language code)  
✅ Converts the translated text into **speech (MP3 audio)** using Google Text-to-Speech (gTTS)  
✅ Saves the audio to a file (e.g., `translated_audio.mp3`) that you can listen to

---

## 🧠 How It Works (Step-by-Step)

1. ✍️ You enter some English text  
2. 🌐 The script uses **GoogleTranslator** to convert it into your desired language  
3. 🔊 Then, it uses **gTTS (Google Text-to-Speech)** to speak out the translated text  
4. 💾 The speech is saved as an `.mp3` file that you can play on any media player

---

## 🗂️ Project Files

| File                         | Description                                      |
|------------------------------|--------------------------------------------------|
| `translator_speech.py`       | The main Python script                          |
| `translated_audio.mp3`       | Output file containing translated speech audio  |

---

## 🧾 Example Code (with Comments)

```python
from deep_translator import GoogleTranslator  # To translate text
from gtts import gTTS                        # To convert text to speech
from io import BytesIO                       # To store audio in memory before saving

# Function to translate text to the target language
def translate_text(text, dest_lang):
    translated_text = GoogleTranslator(source='en', target=dest_lang).translate(text)
    return translated_text

# Function to convert text to speech
def text_to_speech(text, dest_lang):
    tts = gTTS(text=text, lang=dest_lang)
    with BytesIO() as buffer:
        tts.write_to_fp(buffer)
        buffer.seek(0)
        audio_data = buffer.read()
    return audio_data

# Sample input
text = "Robotics combines science, engineering, and technology to build useful machines."
dest_lang = 'ur'  # You can change this to 'hi', 'te', 'fr', 'es', etc.

# Translate and generate speech
translated_text = translate_text(text, dest_lang)
tts_audio = text_to_speech(translated_text, dest_lang)

# Save the audio as an MP3 file
with open("translated_audio.mp3", "wb") as audio_file:
    audio_file.write(tts_audio)

---

## 🌍 Supported Languages (Quick Reference)

You can translate to many popular languages just by changing the `dest_lang` code.

| 🌐 Language      | 💬 Code  |
|------------------|----------|
| Urdu             | `ur`     |
| Hindi            | `hi`     |
| Telugu           | `te`     |
| Tamil            | `ta`     |
| French           | `fr`     |
| Spanish          | `es`     |
| Arabic           | `ar`     |
| Bengali          | `bn`     |
| German           | `de`     |
| Russian          | `ru`     |
| Chinese          | `zh-cn`  |

> 🔗 **Full list of supported languages** → [gTTS Documentation](https://gtts.readthedocs.io/en/latest/module.html#available-languages)

---

## 📁 Optional Enhancements

Looking to build more features? Here are some ideas:

- 🎛️ Add a simple **Graphical User Interface (GUI)** using `Tkinter`
- 📤 Auto-play the generated audio after saving
- 🌐 Allow **input from different source languages**, not just English
- 🔁 Batch process multiple sentences or files

---

## 📌 Notes

- 🌐 Internet connection is **required** (both translation and speech generation use online services)
- 🎯 Best for **small to medium** length text (ideal: 1–3 sentences)
- 🧪 Tested in **VS Code** and **PyCharm** (run normally, audio file will be saved)
