# Voice_Assistant
Nova - Voice-Activated Assistant
Nova is a Python-based voice-activated assistant that leverages various libraries to perform tasks such as fetching information from Wikipedia, opening web pages, playing songs on Spotify, checking the time, and more. The assistant utilizes text-to-speech and speech recognition to interact with the user.

Features:
Wikipedia Search: Nova can fetch information from Wikipedia based on user queries.

Web Browsing: Open YouTube, Google, and Stack Overflow using voice commands.

Spotify Integration: Play songs on Spotify by specifying the song name.

Time Information: Ask Nova for the current time.

Code Editor: Open a specified code editor using a voice command.

Weather Information: Get current weather information by providing the city name.

Jokes: Nova can tell you a random joke for a touch of humor.

Dependencies:
pyttsx3: Text-to-speech engine for voice output.

speech_recognition: Library for recognizing speech.

wikipedia: Fetch information from Wikipedia.

spotipy: Spotify API integration for playing songs.

requests: Make API calls to fetch weather information.

Usage:
Install the required dependencies: pip install pyttsx3 speech_recognition wikipedia spotipy requests.

Obtain Spotify API credentials (client ID, client secret, and redirect URI) and update them in the script.

Run the script, and Nova will greet you and await your voice commands.

Example Commands:
"Open YouTube"
"Play song"
"Tell me about Wikipedia"
"What's the time?"
"Open code editor"
"Tell me the weather"
Feel free to explore Nova's capabilities and customize it according to your needs!
