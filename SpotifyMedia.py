import subprocess

class SpotifyPlayer:
    def __init__(self):
        """Initializes the Spotify player."""
        print("Initializing Spotify...")
        # You'll implement the actual Spotify initialization here later
        pass

    def get_current_song_info(self, time_constant):
        """Gets information about the currently playing song using Raspotify."""
        print("Getting song information (Spotify)...")
        # You'll implement the Spotify metadata extraction here later
        song_info = {
            "title": "Song Title (Spotify)",
            "artist": "Song Artist (Spotify)",
            "duration": "3:33"
        }
        return song_info

    def play_pause(self):
        """Plays or pauses Spotify playback."""
        print("Play/Pause (Spotify)")
        # Implement Spotify play/pause command here
        pass

    def next_track(self):
        """Skips to the next track."""
        print("Next Track (Spotify)")
        # Implement Spotify next track command here
        pass

    def previous_track(self):
        """Skips to the previous track."""
        print("Previous Track (Spotify)")
        # Implement Spotify previous track command here
        pass

    def stop_playback(self):
        """Stops Spotify playback."""
        print("Stop Playback (Spotify)")
        # Implement Spotify stop command here
        pass