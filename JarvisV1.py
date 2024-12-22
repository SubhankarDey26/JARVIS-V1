from Engine.STT import STT
from Engine.TTS import TTS
from Brain.Brain import get_answer
import webbrowser
try:
    import pywhatkit as kt
except ModuleNotFoundError:
    import subprocess
    subprocess.run('pip install pywhatkit')
    import pywhatkit as kt

print("Please press the key 1 or 2 to start Jarvis input")
x = int(input())

if x == 1:
    while True:
        text = input()
        if "jarvis" in text.lower():
            text = text.replace("jarvis", "")
            text = text.replace("Who is """)
            text.replace("What is ", "")
            answer = get_answer(text)
            TTS(answer)
            if "search in youtube" in text:
                text = text.replace("search in youtube", "")
                webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            if "search in google" in text:  # Fixed typo
                text = text.replace("search in google", "")
                TTS("Searching about your request sir.")
                webbrowser.open(f'https://www.google.com/search?q={text}')
                TTS(f"You can see the search result about {text} on your screen.")

            if "music on youtube" in text:
                text = text.replace("music on youtube", "")
                text = text.replace("play", "")
                TTS(f"Playing your music: {text}. Enjoy, sir.")
                kt.playonyt(text)

elif x == 2:
    while True:
        text = STT().lower()
        if "jarvis" in text:
            text = text.replace("jarvis", "")
            text = text.replace("Who is ", "").replace("What is ", "")
            answer = get_answer(text)
            TTS(answer)
            if "search in youtube" in text:
                text = text.replace("search in youtube", "")
                webbrowser.open(f"https://www.youtube.com/results?search_query={text}")
            if "search in google" in text:  # Fixed typo
                text = text.replace("search in google", "")
                TTS("Searching about your request sir.")
                webbrowser.open(f'https://www.google.com/search?q={text}')
                TTS(f"You can see the search result about {text} on your screen.")

            if "music on youtube" in text:
                text = text.replace("music on youtube", "")
                text = text.replace("play", "")
                TTS(f"Playing your music: {text}. Enjoy, sir.")
                kt.playonyt(text)
