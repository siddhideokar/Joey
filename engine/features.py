import subprocess
import webbrowser
import eel
from engine.command import speak
from playsound import playsound
from engine.config import ASSISTANT_NAME, LLM_KEY
import pywhatkit as kit
import re
from engine.helper import extract_yt_term, markdown_to_text
import pvporcupine
import pyaudio
import struct
import time
import markdown2



@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\audio\\start_sound.mp3"
    playsound(music_dir)

import os
import subprocess
import webbrowser
import sqlite3

import os
import subprocess
import webbrowser
import sqlite3

import os
import subprocess
import webbrowser
import sqlite3

def openCommand(query):
    try:
        query = query.replace(ASSISTANT_NAME.lower(), "").replace("open", "").strip().lower()
        app_name = query

        # ✅ Connect to database
        conn = sqlite3.connect('commands.db')
        cursor = conn.cursor()

        # ✅ Ensure required tables exist
        cursor.execute('''CREATE TABLE IF NOT EXISTS sys_command (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE,
                            path TEXT)''')

        cursor.execute('''CREATE TABLE IF NOT EXISTS web_command (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT UNIQUE,
                            url TEXT)''')

        conn.commit()

        # Check in sys_command table
        cursor.execute("SELECT path FROM sys_command WHERE name = ?", (app_name,))
        results = cursor.fetchall()

        if len(results) > 0:
            speak("Opening " + query)
            os.startfile(results[0][0])
            conn.close()
            return

        #  Check in web_command table
        cursor.execute("SELECT url FROM web_command WHERE name = ?", (app_name,))
        results = cursor.fetchall()

        if len(results) > 0:
            speak("Opening " + query)
            webbrowser.open(results[0][0])
            conn.close()
            return

        #  Built-in apps
        apps = {
            "chrome": "chrome",
            "google chrome": "chrome",
            "notepad": "notepad",
            "calculator": "calc",
            "paint": "mspaint",
            "word": "winword",
            "excel": "excel",
            "vs code": "code",
            "command prompt": "cmd"
        }

        for app in apps:
            if app in query:
                speak(f"Opening {app}")
                subprocess.Popen(f"start {apps[app]}", shell=True)
                conn.close()
                return

        #  Known websites
        websites = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "facebook": "https://www.facebook.com",
            "instagram": "https://www.instagram.com",
            "twitter": "https://twitter.com",
            "github": "https://github.com",
            "chatgpt": "https://chat.openai.com"
        }

        for site in websites:
            if site in query:
                speak(f"Opening {site}")
                webbrowser.open(websites[site])
                conn.close()
                return

        #  Try system open
        speak("Opening " + query)
        try:
            os.system('start ' + query)
        except:
            speak("Not found")

        # Final fallback: Google search
        speak(f"Searching for {query}")
        webbrowser.open(f"https://www.google.com/search?q={query}")

        conn.close()

    except Exception as e:
        print("Error:", e)
        speak("Something went wrong")




import pywhatkit
import re
from engine.command import speak

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    
    if not search_term:  # if extraction failed
        # Try a simpler fallback — just use the whole query
        search_term = query.replace("play", "").replace("on youtube", "").strip()
        
        if not search_term:
            speak("Please tell me what to play on YouTube.")
            return
    
    speak("Playing " + search_term + " on YouTube")
    
    try:
        pywhatkit.playonyt(search_term)
    except Exception as e:
        print("Error while playing YouTube:", e)
        speak("Something went wrong while trying to play on YouTube.")

def extract_yt_term(command):
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    match = re.search(pattern, command, re.IGNORECASE)
    return match.group(1).strip() if match else None

import pvporcupine
import pyaudio
import struct
import time
import pyautogui

def hotword():
    porcupine = None
    paud = None
    audio_stream = None

    try:
        # Initialize Porcupine with the built-in keyword "porcupine"
        porcupine = pvporcupine.create(
            keywords=["porcupine"]
        )

        paud = pyaudio.PyAudio()
        audio_stream = paud.open(
            rate=porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=porcupine.frame_length
        )

        print(" Listening for hotword: 'Porcupine'...")

        while True:
            pcm = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )

            pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)

            result = porcupine.process(pcm)

            if result >= 0:
                print(" Hotword 'Porcupine' detected!")

                # Trigger Win+J
                pyautogui.keyDown("win")
                pyautogui.press("j")
                time.sleep(0.2)
                pyautogui.keyUp("win")

                # Prevent multiple rapid triggers
                time.sleep(1)

    except KeyboardInterrupt:
        print("\nStopped by user.")

    except Exception as e:
        print("Error:", e)

    finally:
        if porcupine:
            porcupine.delete()
        if audio_stream:
            audio_stream.close()
        if paud:
            paud.terminate()

        print("Audio resources released.")


import google.generativeai as genai
def geminiai(query):
    try:
        query = query.replace(ASSISTANT_NAME, "")
        query= query.replace("search", "")
        #Set your API key
        genai.configure(api_key=LLM_KEY)


        #Select a model
        model = genai.GenerativeModel("gemini-2.0-flash")

        #Generate a response
        response = model.generate_content(query)
        filter_text = markdown_to_text(response.text)
        speak(filter_text)
    except Exception as e:
        print("Error:", e)