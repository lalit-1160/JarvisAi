import speech_recognition as sr
import os
import webbrowser
import datetime
import random
import openai  # Assuming you have OpenAI installed on your Windows environment
from openai import OpenAI
# Flask Package
from flask import Flask, jsonify, request
from flask_cors import CORS
import json
import pyttsx3

app = Flask(__name__)
CORS(app)

api_key = "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"
client = OpenAI(api_key=api_key)



chatStr = ""
engine = pyttsx3.init()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

def say(text):
    engine.say(text)
    engine.runAndWait()


def chat(query):
    global chatStr
    print(chatStr)
    chatStr += f"Lalit: {query}\n Jarvis: "

    # Convert chatStr to a list to make it JSON serializable
    chat_messages = [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": chatStr}]

    # The rest of your chat function remains the same
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=chat_messages,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        choices = response.choices
        content = choices[0].message.content
        say(content)
        chatStr += f"{content}\n"
        print(f"Resopnse: {content}")
        return content
    except Exception as e:
        # Handle the exception here
        print(f"An error occurred: {e}")






# Query Process
def process_command_logic(query):
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"]]

    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            return "Command processed successfully"

    if "open music" in query:
        musicPath = r"C:\Users\lalit\PycharmProjects\JarvisAI\pythonProject\music.mp3"
        os.system(f"start {musicPath}")
        return "Command processed successfully"
    elif "the time" in query:
        hour = datetime.datetime.now().strftime("%H")
        minute = datetime.datetime.now().strftime("%M")
        say(f"Sir, the time is {hour} o'clock {minute} minutes")
        return f"The time is {hour}:{minute}"
    elif "open jetbrains".lower() in query.lower():
        os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox\JetBrains Toolbox.lnk")
        return "Command processed successfully"
    elif "open visual studio".lower() in query.lower():
        os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
        return "Command processed successfully"
    else:
        return chat(query)

# # Server 1
# @app.route('/commands')
# def command():
#     print("hello")
#     data = {'message': 'Hello from the backend!'}
#     json_string = json.dumps(data)
#     return json_string

# Server 2
@app.route('/data', methods=['POST'])
def data():
    try:
        # Get JSON data from the request
        beta = request.json
        print(beta)
        print(beta['query'])

        temp = process_command_logic(beta['query'])
        return temp;

    except Exception as e:
        # Handle exceptions (e.g., JSON decoding error)
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    say("Jarvis A.I")
    app.run(debug=True, port=2000)

    # while True:
    #     print("Listening...")
    #     query = takeCommand()
    #
    #     # Update the sites list with Windows-compatible URLs or commands
    #     sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
    #              ["google", "https://www.google.com"]]
    #
    #     for site in sites:
    #         if f"Open {site[0]}".lower() in query.lower():
    #             say(f"Opening {site[0]} sir...")
    #             webbrowser.open(site[1])
    #
    #     # Update the musicPath with a valid path to a music file on your Windows machine
    #     if "open music" in query:
    #         musicPath = r"C:\Users\lalit\PycharmProjects\JarvisAI\pythonProject\music.mp3"
    #         os.system(f"start {musicPath}")
    #
    #     elif "the time" in query:
    #         hour = datetime.datetime.now().strftime("%H")
    #         minute = datetime.datetime.now().strftime("%M")
    #         say(f"Sir, the time is {hour} o'clock {minute} minutes")
    #
    #     # Update the path to open FaceTime and Passky on Windows
    #     elif "open jetbrains".lower() in query.lower():
    #         # Provide the path to the executable or command to open FaceTime on Windows
    #         os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox\JetBrains Toolbox.lnk")
    #
    #     elif "open visual studio".lower() in query.lower():
    #         # Provide the path to the executable or command to open Passky on Windows
    #         os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
    #
    #     # The rest of your code remains unchanged
    #
    #     else:
    #         print("Chatting...")
    #         chat(query)