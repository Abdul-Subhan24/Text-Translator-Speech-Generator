# Text-Translator-Speech-Generator
Translate English text into any language and convert it to speech using Python.

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Text Translator & Speech Generator</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #f5f7fa;
      color: #333;
      margin: 0;
      padding: 0;
    }

    header {
      background-color: #4c8bf5;
      color: white;
      padding: 20px;
      text-align: center;
    }

    .container {
      max-width: 800px;
      margin: 30px auto;
      padding: 20px;
      background-color: white;
      box-shadow: 0 0 10px rgba(0,0,0,0.1);
      border-radius: 10px;
    }

    h1, h2 {
      color: #4c8bf5;
    }

    code {
      background-color: #eee;
      padding: 2px 4px;
      border-radius: 4px;
      font-size: 0.95em;
    }

    ul {
      padding-left: 20px;
    }

    footer {
      text-align: center;
      padding: 15px;
      color: #888;
      font-size: 0.9em;
    }
  </style>
</head>
<body>
  <header>
    <h1>Text Translator & Speech Generator</h1>
    <p>Translate English text into any language and convert it to speech using Python</p>
  </header>

  <div class="container">
    <h2>🔧 About This Project</h2>
    <p>This Python project helps you do two things:</p>
    <ol>
      <li>Translate English text into a language of your choice</li>
      <li>Convert the translated text into an audio file</li>
    </ol>

    <p><strong>Technologies Used:</strong></p>
    <ul>
      <li><code>deep_translator</code> – to translate text</li>
      <li><code>gTTS (Google Text-to-Speech)</code> – to generate speech</li>
    </ul>

    <h2>📌 Example</h2>
    <p><strong>Original Text (in English):</strong><br>
      <em>"Robotics is the science of building smart machines to help humans."</em>
    </p>

    <p><strong>Translated into Urdu:</strong><br>
      <em>"روبوٹکس سمارٹ مشینیں بنانے کا علم ہے جو انسانوں کی مدد کرتی ہیں۔"</em>
    </p>

    <p><strong>Generated Audio File:</strong><br>
      <code>translated_audio.mp3</code>
    </p>

    <p>Just run the code, and you'll get an audio file that reads the translated sentence aloud in the selected language.</p>
  </div>

  <footer>
    © 2025 Md Abdul Subhan | Internship Project – Fullstack Academy
  </footer>
</body>
</html>
