#Subclasses imported
from artists.drake import Drake
from artists.travis import Travis
from artists.gunna import Gunna
from artists.future import Future
from artists.carti import Carti
from artists.youngthug import YoungThug
# difflib is part of python's standard library for identifying close matches : drak -> drake
from difflib import get_close_matches

# User input taken as strings entered into a dictionary to instantiate new classes without constructors
artists = {
    "drake": Drake,
    "travis": Travis,
    "gunna": Gunna,
    "future": Future,
    "playboi carti": Carti,
    "young thug": YoungThug
}

#Synonyms of commands to improve versatility/robustness
commands = {
    "exit": ["exit", "quit", "bye", "close", "end", "goodbye"],
    "list": ["list", "artists", "show all"],
    "help": ["help", "commands", "options", "instructions"],
    "info": ["info","information","introduction", "intro", "who", "about"],
    "bio": ["bio", "summary", "details"],
    "songs": ["songs", "tracks", "music", "hits","most streamed songs","top","most streamed","top streamed"],
    "genre": ["genre", "style", "type", "category","influence"]
}

# Reverse map each synonym to its main command
synonym_map = {syn: main for main, synonyms in commands.items() for syn in synonyms}

# Creating chatbot() execution method to be called in main.py
def chatbot():
    print("🎵 Hey there! Welcome to the Artist ChatBot!")  #Friendly greeting
    print("Commands:")
    print("  info <artist>  - Show artist brief introduction")
    print("  bio  <artist>  - Display summary of artist")
    print("  songs <artist> - List top streamed songs")
    print("  genre <artist> - Show artist genre")
    print("  list           - Show all available artists")
    print("  help           - Show all commands")
    print("  exit           - Quit")

    while True:
        user_input = input("\nWhat would you like to know? ").strip().lower()  # Friendly prompt

        if not user_input:
            print("🤔 I didn’t catch that. Can you type something?")
            continue

        # Try to detect command from input
        command = None
        for key, main_command in synonym_map.items():
            if key in user_input:
                command = main_command
                break

        if not command:
            print("⚠ Hmm… I didn’t get that. Type 'help' to see what I can do.")  #Humanized unknown command
            continue

        # Handle single-word commands
        if command == "exit":
            print("👋 Catch you later! Keep enjoying good music!")  #Friendly exit message
            break
        elif command == "list":
            print("Here’s who I know about:", ", ".join(artists.keys()))
            continue
        elif command == "help":
            print("\nI can help you with these commands:")  #Added friendly comment
            print("  info <artist>  - Quick intro")
            print("  bio  <artist>  - Artist summary")
            print("  songs <artist> - Top streamed tracks")
            print("  genre <artist> - Artist genre")
            print("  list           - Show all available artists")
            print("  help           - Show this list")
            print("  exit           - Say goodbye")
            continue

        # Try to detect artist from input using fuzzy matching
        artist_name = None
        matches = get_close_matches(user_input, artists.keys(), n=1, cutoff=0.5)
        if matches:
            artist_name = matches[0]

        if not artist_name:
            print("⚠ I couldn’t figure out which artist you mean. Type 'list' to see available artists.")
            continue

        artist_obj = artists[artist_name]()  # instantiate

        #Execute conditional loop responses to predefined inputs and their synonyms
        if command == "info":
            print("\n🎤 " + artist_obj.get_info())
        elif command == "bio":
            print("\n📖 " + artist_obj.get_bio())
        elif command == "songs":
            songs = artist_obj.get_top_songs()
            if isinstance(songs, str):
                songs = [s.strip() for s in songs.split(",")]
            print("\n🎶 Most streamed songs:\n" + "\n".join(f"- {s}" for s in songs))
        elif command == "genre":
            print("\n🎧 Genre/style: " + artist_obj.get_genre())
