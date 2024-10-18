import subprocess

class SpotifyPlayer:
    def __init__(self, time_constant):
        """Initializes the Spotify player (using Raspotify)."""
        print("Initializing Spotify...")
        try:
            # Check if Raspotify is installed and running
            subprocess.run(["systemctl", "status", "raspotify"], check=True)
            print("Raspotify is running.")
        except subprocess.CalledProcessError:
            print("Error: Raspotify is not installed or not running.")
            print("Please install and start Raspotify.")
            # You might want to exit or handle the error differently here

    def get_current_song_info(self):
        """Gets information about the currently playing song using Raspotify."""
        print("Getting song information (Spotify)...")
        try:
            # Use playerctl to get song information
            process = subprocess.run(["playerctl", "metadata", "-p", "raspotify", 
                                      "title", "artist", "duration"], capture_output=True, text=True)
            output = process.stdout.splitlines()

            if len(output) == 3:
                title, artist, duration = output
                return {
                    "title": title,
                    "artist": artist,
                    "duration": duration
                }
            else:
                print("Error: Could not get song information from playerctl.")
                return {"title": "Unknown", "artist": "Unknown", "duration": "Unknown"}

        except FileNotFoundError:
            print("Error: playerctl not found. Please install playerctl.")
            return {"title": "Unknown", "artist": "Unknown", "duration": "Unknown"}
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return {"title": "Unknown", "artist": "Unknown", "duration": "Unknown"}

    def play_pause(self):
        """Plays or pauses Spotify playback."""
        print("Play/Pause (Spotify)")
        subprocess.run(["playerctl", "play-pause", "-p", "raspotify"])

    def next_track(self):
        """Skips to the next track."""
        print("Next Track (Spotify)")
        subprocess.run(["playerctl", "next", "-p", "raspotify"])

    def previous_track(self):
        """Skips to the previous track."""
        print("Previous Track (Spotify)")
        subprocess.run(["playerctl", "previous", "-p", "raspotify"])

    def stop_playback(self):
        """Stops Spotify playback."""
        print("Stop Playback (Spotify)")
        subprocess.run(["playerctl", "stop", "-p", "raspotify"])