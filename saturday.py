import os
import pyttsx3
import datetime
import playsound
import speech_recognition as sr
import wikipedia
import webbrowser
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
import random

client_id = '54d961da3d844b7fab9714c3b358b251'
client_secret = 'd082b452a51f4adfaaac2f53b4331a4d'
redirect_uri = 'https://developer.spotify.com/dashboard/create'
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope="user-library-read user-modify-playback-state"))

#weather api
api_key = '1f0d13975c7576a5c90d1037dfccd97c'
#jokes
jokes=[ "Why did the scarecrow win an award? Because he was outstanding!",
"What do you call a fish with no eyes? Fsh!",
"Why don't scientists trust atoms? Because they make up everything!",
"Parallel lines have so much in common. It's a shame they'll never meet.",
"Why don't skeletons fight each other? They don't have the guts.",
"I told my wife she was drawing her eyebrows too high. She looked surprised.",
"What do you get when you cross a snowman and a dog? Frostbite!",
"Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them.",
"What did one plate say to the other plate? Lunch is on me!",
"How do you make holy water? You boil the hell out of it.",
"Why did the bicycle fall over? Because it was two-tired.",
"I'm reading a book on anti-gravity. It's impossible to put down.",
"Did you hear about the cheese factory that exploded? There was nothing left but de-brie.",
"I used to play piano by ear, but now I use my hands.",
"How do you catch a squirrel? Climb a tree and act like a nut!",
"Why can't you give Elsa a balloon? Because she will let it go.",
"I told my wife she was drawing her eyebrows too high. She looked surprised." ]

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def get_weather(city):
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    params = {'q': city, 'appid': api_key, 'units': 'metric'}  # Adjust units as needed

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        return f"The current temperature in {city} is {temperature}°C with {description}."
    else:
        return "Sorry, I couldn't fetch the weather information at the moment."

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
    else :
        speak("Good evening")
    speak("I am nova .please tell me how can i help you")

def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        
        
        audio=r.listen(source)
    try:
        print("recognizing.....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user said :{query}\n")
    except Exception as e:
        print("say that again..............")
        return "None"
    return query


    
     

if __name__ =="__main__":
    wishMe()
    if 1:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedia..................")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play song' in query:
            speak("which song you want to play")
            song=takecommand()
            webbrowser.open(f'https://open.spotify.com//search//{song}')
            results = sp.search(q=song, type='track')
            song_uri = results['tracks']['items'][0]['uri']
            sp.start_playback(uris=[song_uri])

        elif 'the time' in query:
            current_time=datetime.datetime.now(datetime.timezone.utc) +datetime.timedelta(hours=5, minutes=30) 
            strTime = current_time.strftime("%I:%M %p")
            speak(f"the time is  {strTime}")

        elif 'open code' in query:
            codepath="C:\\Users\\Kanika\\OneDrive\\Desktop\\saturday.py"
            os.startfile(codepath)

        elif  'tell me weather' in query:
            speak("Sure, please specify the city.")
            city = takecommand().lower()
            weather_info = get_weather(city)
            speak(weather_info)
        elif "joke" in query:
            speak(random.choice(jokes))
            

        


        

        


    












    
