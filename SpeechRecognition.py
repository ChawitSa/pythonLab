import speech_recognition as sr
import pyttsx3
import openai

openai.api_key = "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"

def greeting():
    speak("Hello!!")
    print("Hello!!")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        recognizerObject.adjust_for_ambient_noise(source)
        print("Listening...")
        voice = recognizerObject.listen(source, timeout=5)
        try:
            statement = ChatGPT_explain(voice)
            print("Got it")
            print("GPT:", statement)
        except Exception as e:
            print("Sorry, Please try again")
            speak("Sorry, Please try again")
            return ""
        return statement


def ChatGPT_explain(query:str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=query,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response['choices'][0]['text']


engine = pyttsx3.init()
recognizerObject = sr.Recognizer()
greeting()

while True:
    statement = take_command().lower()
    if statement == 0:
        continue
    if "goodbye" in statement or "stop" in statement or "bye" in statement:
        print("ChatGPT interface is shutting down, good bye")
        speak("ChatGPT interface is shutting down, good bye")
        break
