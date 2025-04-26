
# Jarvis - Your Personal AI Assistant

## Description
A Python based AI assistant that performs small tasks and converse.

This is a Python-based personal AI assistant, "Jarvis," that can perform various tasks, including:

* Opening websites (YouTube, Google, Wikipedia, etc.)
* Playing music files
* Telling the current time
* Opening specific folders (ML folder, VS Code)
* Chatting with a large language model (using Gemini)
* Saving chat logs
* Voice commands using speech recognition
* Text-to-speech output

## Features Implemented
The following features are implemented:
* Opening websites by voice command.
* Playing music files from a specified directory.
* Telling the time.
* Opening specific folders.
* Chatting with a large language model.
* Saving chat logs to files.

## Code Description
The core code consists of the following python script:
* `config.py`: Holds the API key for the Gemini.
* `main.py`: Main script to run the Jarvis AI.

## Dependencies
* `speech_recognition`: For voice recognition.
* `pywin32`: For text-to-speech on Windows.
* `webbrowser`: For opening websites.
* `google.generativeai`: For interacting with the Gemini API.
* `datetime`: For getting current time.
* `os`: For interacting with the operating system.
* `sys`: For system-specific parameters and functions.

## Setup Instructions
1.  **Install Dependencies:**
    ```bash
    pip install SpeechRecognition pypiwin32 google-generativeai
    ```
2.  **Configure API Key:**
    * Create a file named `config.py` in the same directory as `main.py`.
    * Add your Google Gemini API key to `config.py` as follows:
        ```python
        apiKey = "YOUR_API_KEY"  # Replace with your actual API key
        ```
3.  **Set Music Paths (Optional):**
    * Modify the `musics` list in `main.py` to point to the correct paths of your music files.
4.  **Run Jarvis:**
    ```bash
    python main.py
    ```

## Video Demos
Here are the video demos:

### Jarvis 1

[Demo Video of Jarvis 1](https://github.com/Jarvis AI assistant/blob/master/Jarvis 1.mp4)


### Jarvis 2

[Demo Video of Jarvis 2](https://github.com/Jarvis AI assistant/blob/master/Jarvis 2.mp4)

