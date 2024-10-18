import subprocess

class VLCPlayer:
    def __init__(self):
        """Initializes the VLC media player."""
        print("Initializing VLC...")
        # No specific initialization needed for cvlc

    def load_music(self, music_dir):
        """Loads music from the given directory."""
        print(f"Loading music from {music_dir}...")
        # You'll implement the actual VLC loading logic here later
        pass

    def get_current_song_info(self):
        """Gets information about the currently playing song."""
        print("Getting song information (VLC)...")
        # You'll implement the VLC metadata extraction here later
        song_info = {
            "title": "Song Title (VLC)",
            "artist": "Song Artist (VLC)",
            "duration": "3:33"
        }
        return song_info

    def play_pause(self):
        """Plays or pauses the music."""
        print("Play/Pause (VLC)")
        # Implement VLC play/pause command here
        pass

    def next_track(self):
        """Skips to the next track."""
        print("Next Track (VLC)")
        # Implement VLC next track command here
        pass

    def previous_track(self):
        """Skips to the previous track."""
        print("Previous Track (VLC)")
        # Implement VLC previous track command here
        pass

    def stop_playback(self):
        """Stops the music playback."""
        print("Stop Playback (VLC)")
        # Implement VLC stop command here
        pass