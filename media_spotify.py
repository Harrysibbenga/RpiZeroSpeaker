import subprocess

def initialize_media():
    """Starts the Raspotify service."""
    subprocess.run(["systemctl", "start", "playerctl"])

def get_current_song_info():
    """Gets information about the currently playing song using playerctl."""
    # Use playerctl or Raspotify's API to get song info
    # ... (Implementation to get song info from Spotify API)
    return song_info

def play_pause():
    """Plays or pauses Spotify playback."""
    subprocess.run(["playerctl", "play-pause"])

def next_track():
    """Skips to the next track."""
    subprocess.run(["playerctl", "next"])

def previous_track():
    """Skips to the previous track."""
    subprocess.run(["playerctl", "previous"])

def stop_playback():
    """Stops Spotify playback."""
    subprocess.run(["playerctl", "stop"])