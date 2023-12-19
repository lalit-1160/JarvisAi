from flask import Flask, jsonify, request
from flask_cors import CORS
import speech_recognition as sr
import os
import datetime
import webbrowser
import random
import openai
from openai import OpenAI
import pyttsx3
import json

# app = Flask(__name__)
app = Flask(__name__)
CORS(app)





chat_str = ""
engine = pyttsx3.init()

# Server 1
@app.route('/data', methods=['POST'])
def data():
    try:
        beta = request.json
        print(beta)
        que = beta['query']
        query_type = beta['type']
        global_variable = []


        if query_type=='0':
            temp = chat(que, global_variable)
            print(f'Temp = {temp}')
            # Access the value from the global_variable list
            result = global_variable[0] if global_variable else None
            return jsonify({'result': result})
        elif query_type=='1':
            q = process_browser(que,global_variable);
            result = global_variable[0] if global_variable else None
            return jsonify({'result': result})
        elif query_type=='2':
            b = process_application(que,global_variable)
            result = global_variable[0] if global_variable else None
            return jsonify({'result': result})
        elif query_type=='3':
            t = process_time(global_variable)
            result = global_variable[0] if global_variable else None
            return jsonify({'result': result})

        else:
            # Handle the case when type is not 0, 1, 2, or 3
            return jsonify({'error': 'Invalid type value'})

    except Exception as e:
        # Handle exceptions (e.g., JSON decoding error)
        return jsonify({'error': str(e)})

# Server 2

@app.route('/microphone',methods=['Get'])
def microphone():
    mic_value = take_command();
    return jsonify({'result':mic_value})


# Mic
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Jarvis"

# Speech
def say(text):
    engine.say(text)
    spoken_text = f"Speaking: {text}"
    # engine.runAndWait()  # Uncomment this line if you need to run and wait for the speech synthesis to finish
    return spoken_text

def process_browser(query,global_variable):
    sites = [["youtube", "https://www.youtube.com"], ["wikipedia", "https://www.wikipedia.com"],
             ["google", "https://www.google.com"]]
    for site in sites:
        if f"Open {site[0]}".lower() in query.lower():
            say(f"Opening {site[0]} sir...")
            webbrowser.open(site[1])
            global_variable.append("Command processed successfully")
            return "Command processed successfully"

    return "Sorry can not process request...."


def process_time(global_variable):
    hour = datetime.datetime.now().strftime("%H")
    minute = datetime.datetime.now().strftime("%M")
    global_variable.append(f"Sir, the time is {hour} o'clock {minute} minutes")
    spoken_text = say(f"Sir, the time is {hour} o'clock {minute} minutes")
    print(spoken_text)
    return f"The time is {hour}:{minute}"


def process_application(query,global_varaible):
    if "open music".lower() in query.lower():
        musicPath = r"C:\Users\lalit\PycharmProjects\JarvisAI\pythonProject\music.mp3"
        os.system(f"start {musicPath}")
        global_varaible.append("Command processed successfully")
        return "Command processed successfully"
    elif "open jetbrains".lower() in query.lower():
        os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\JetBrains Toolbox\JetBrains Toolbox.lnk")
        global_varaible.append("Command processed successfully")
        return "Command processed successfully"
    elif "open visual studio".lower() in query.lower():
        os.system(r"start explorer.exe C:\Users\lalit\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code\Visual Studio Code.lnk")
        global_varaible.append("Command processed successfully")
        return "Command processed successfully"
    else:
        global_varaible.append("Sorry can not find path.....")
        return "Sorry can not find path....."



# OpenAi Key
api_key = "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"
client = openai.OpenAI(api_key=api_key)

# ChatGPT Fun
def chat(query, global_variable):
    # Convert chatStr to a list to make it JSON serializable
    chat_messages = [{"role": "system", "content": "You are a helpful assistant."},
                     {"role": "user", "content": query}]

    try:
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
        choices = response.choices
        content = choices[0].message.content

        # Append content to the global_variable list
        global_variable.append(content)

        print(content)
        say(content)

        return content
    except Exception as e:
        # Handle the exception here
        print(f"An error occurred: {e}")
        # You might want to log the error or take other appropriate actions
        return "An error occurred. Please try again."



# main function
if __name__ == '__main__':
    print('Welcome to Jarvis A.I')
    # say("Jarvis A.I")
    app.run(debug=True,port=2000)
