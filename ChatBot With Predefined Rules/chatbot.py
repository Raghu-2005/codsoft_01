import pyttsx3 
import wikipedia
import speech_recognition as sr
from geopy.geocoders import Nominatim
import json
import strmath

name = 'IPS Chat Bot'

engine = pyttsx3.init('sapi5')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 20)

def jsonInit():
    with open('question.json', 'r') as file:
        data = file.read().replace('\n', '')   
        questions = json.loads(data)
    return questions

def getAnswer(query : str, questions):
    try:
        answer = questions[query]
    except:
        if 'add' in query or 'plus' in query or '+' in query:
            answer = 'the answer is ' + strmath.add(query)

        elif 'subtract' in query or 'minus' in query or '-' in query:
            answer = 'the answer is ' + strmath.subtract(query)

        elif 'divide' in query or 'divided' in query:
            answer = 'the answer is ' + strmath.divide(query)

        elif 'multiply' in query or 'multiplied' in query or 'times' in query or 'into' in query:
            answer = 'the answer is ' + strmath.multiply(query)

        elif 'what is ' in query:
            query = query.replace('what is ', '')
            answer = searchWiki(query)
    
        elif 'who is ' in query:
            query = query.replace('who is ', '')
            answer = searchWiki(query)

        elif 'where is ' in query:
            query = query.replace('where is ', '')
            answer = query + ' is located at ' + str(locate(query))

        else:
            answer = 'i do not know about that'

    return answer

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:       
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print('listening')
        audio = r.listen(source)

    try:
        print('recognizing')
        query = (r.recognize_google(audio, language ='en-in'))      
    except:
        query = 'Please repeat it'
        return query

    query.lower()
    print(query)
    return query

def searchWiki(query : str):
    try:
        search = wikipedia.search(query)
        result = wikipedia.summary(search[0], 2)
    except:       
        result = 'sorry, i can not find any results realating to ' + query + ' on wikipedia'

    print(result)
    return result

def locate(place):
    geolocator = Nominatim(user_agent = 'IPS Chat Bot')
    return geolocator.geocode('Taj Mahal', language = 'en')

def Greet(engine, name):
    engine.say('My name is ' + name)
    engine.say('How may I help you')
    engine.runAndWait()

Greet(engine, name)
questions = jsonInit()

while 1:    
    query = takeCommand()
   
    answer = getAnswer(query, questions)      

    engine.say(answer)
    engine.runAndWait()