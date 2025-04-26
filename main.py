import speech_recognition as sr
import os
import win32com.client
# from wikipedia import languages
import webbrowser
import google.generativeai as genai
# import openai
import datetime
# import subprocess
import sys
from config import apiKey
# import random

chatStr = ""

speaker = win32com.client.Dispatch("SAPI.SpVoice")

def chat(query,chatStr):
    genai.configure(api_key=apiKey)
    chatStr+= f"Pragya : {query} \nJarvis : "
    print(chatStr)
    # prompt = chatStr

    model = genai.GenerativeModel('gemini-2.0-flash')
    try:
        response = model.generate_content(query)
        # print(response.text[0:1000])
        say(response.text)
        chatStr = f"{response.text}"
        print(chatStr)
        return chatStr
    except Exception as e:
        print(f"Error generating content: {e}")
        chatStr += f"Error: {e}"  # Add the error to the text to be saved

    dirD = "gemini"
    if not os.path.exists(dirD):
        try:
            os.makedirs(dirD)
        except OSError as e:
            print(f"Error creating directory {dirD}: {e}")
            return

    filename = f" {''.join(query.split("intelligence")[1:]).strip()}.txt"
    filepath = os.path.join(dirD, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:  # Specify encoding
            f.write(chatStr)
        print(f"Response saved to: {filepath}")  # added print
    except OSError as e:
        print(f"Error writing to file {filepath}: {e}")

def ai(prompt):
    genai.configure(api_key=apiKey)
    text = f"Jarvis Response for prompt: {prompt} \n********************\n\n"

    model = genai.GenerativeModel('gemini-2.0-flash')
    try:
        response = model.generate_content(prompt)
        print(response.text[0:1000])
        text+= response.text
    except Exception as e:
        print(f"Error generating content: {e}")
        text += f"Error: {e}"  # Add the error to the text to be saved

    dirD = "gemini"
    if not os.path.exists(dirD):
        try:
            os.makedirs(dirD)
        except OSError as e:
            print(f"Error creating directory {dirD}: {e}")
            return

    filename = f" {''.join(prompt.split("intelligence")[1:]).strip()}.txt"
    filepath = os.path.join(dirD, filename)
    try:
        with open(filepath, "w", encoding="utf-8") as f:  # Specify encoding
            f.write(text)
        print(f"Response saved to: {filepath}")  # added print
    except OSError as e:
        print(f"Error writing to file {filepath}: {e}")


def say(text):
    # os.system(f"say {text}")
    speaker.Speak(text)

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-IN")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "An error occurred. Sorry from Jarvis"
    
if __name__ == '__main__':
    say("Hello I am Jarvis AI")
    while True:
        print("Listening....")
        query = takeCommand()
        sites = [["youtube", "https://youtube.com"],["google","https://google.com"],["wikipedia", "https://wikipedia.com"],["instagram", "https://instagram.com"],["github",    "https://github.com"],["twitter",   "https://twitter.com"],["facebook",  "https://facebook.com"],["reddit",    "https://reddit.com"],["linkedin",  "https://linkedin.com"],["stackoverflow", "https://stackoverflow.com"],["amazon", "https://amazon.com"],["twitter",       "https://twitter.com"],["medium",        "https://medium.com"],["duckduckgo",    "https://duckduckgo.com"],["pinterest",     "https://pinterest.com"]]
        musics = [["hope", r"C:\Users\pragy\Downloads\hope.mp3"],["slow life", r"C:\Users\pragy\Downloads\slowlife.mp3"],["heart", r"C:\Users\pragy\Downloads\hearty.mp3"],["by my side", r"C:\Users\pragy\Downloads\bymyside.mp3"], ["long night", r"C:\Users\pragy\Downloads\longnight.mp3"]]

        for site in sites:
            if f"Open {site[0]}".lower() in query.lower():
                say(f"Opening {site[0]}...")
                webbrowser.open(site[1])

        for music in musics:
            if f"play {music[0]}".lower() in query.lower():
                musicPath = music[1]
                try:
                    if sys.platform == "darwin": #mac OS
                        os.system(f"open '{musicPath}'")
                    elif sys.platform == "win32":
                        os.system(f"start \"\" \"{musicPath}\"")
                except FileNotFoundError:
                    say(f"Error: The file '{musicPath}' was not found.")
                except Exception as e:
                    say(f"An error occurred: {e}")

        if "the time".lower() in query.lower():
            strfTime = datetime.datetime.now().strftime("%H:%M:%S")
            say(f"The time is {strfTime}")

        elif "open ML folder".lower() in query.lower():
            mlFolderPath = r"C:\Users\pragy\Documents\Codessss of all kindsssss\ML"
            if sys.platform == "darwin": #mac OS
                os.system(f"open '{mlFolderPath}'")
            elif sys.platform == "win32":
                os.system(f"start \"\" \"{mlFolderPath}\"")
            else:
                say("Unsupported operating system for opening folders via command line.")

        elif "open Vs Code".lower() in query.lower():
            mlFolderPath = r"C:\Users\pragy\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            if sys.platform == "darwin": #mac OS
                os.system(f"open '{mlFolderPath}'")
            elif sys.platform == "win32":
                os.system(f"start \"\" \"{mlFolderPath}\"")
            else:
                say("Unsupported operating system for opening folders via command line.")

        elif "Using your intelligence".lower() in query.lower():
            ai(query)


        elif "Jarvis quit".lower() in query.lower():
            exit()

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        else:
            print("Chatting....")
            chat(query,chatStr)


