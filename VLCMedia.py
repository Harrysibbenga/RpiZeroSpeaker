import subprocess
import vlc
import time

class VLCPlayer:
    def __init__(self, time_constant):
        """Initializes the VLC media player."""
        print("Initializing VLC...")
        self.instance = vlc.Instance('--no-xlib')
        self.player = self.instance.media_player_new()
        self.playlist = []
        self.current_song_index = 0
        self.time_const = time_constant

    def load_music(self, music_dir):
        """Loads music from the given directory."""
        print(f"Loading music from {music_dir}...")
        try:
            # Get a list of supported audio files in the directory
            process = subprocess.run(['find', music_dir, '-type', 'f', '-name', '*.mp3', '-o', '-name', '*.wav', '-o', '-name', '*.flac'],
                                   capture_output=True, text=True)
            files = process.stdout.splitlines()

            if files:
                self.playlist = files
                for file in files:
                    print(file)
                # Start playing the first song
                self.play_song(0)

            else:
                print("No supported audio files found in the directory.")

        except FileNotFoundError:
            print("Error: Music directory not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def get_current_song_info(self):
        """Gets information about the currently playing song."""
        print("Getting song information (VLC)...")
        media = self.player.get_media()
        if media:
            # Extract metadata
            title = media.get_meta(vlc.Meta.Title) or "Unknown Title"
            artist = media.get_meta(vlc.Meta.Artist) or "Unknown Artist"
            duration = self.format_time(media.get_duration())

            song_info = {
                "title": title,
                "artist": artist,
                "duration": duration
            }
            return song_info
        else:
            return {"title": "No song playing", "artist": "", "duration": ""}

    def play_pause(self):
        """Plays or pauses the music."""
        print("Play/Pause (VLC)")
        if self.player.is_playing():
            self.player.pause()
        elif self.playlist:  # Check if the playlist is not empty
            self.play_song(self.current_song_index)

    def play_song(self, index):
        """Plays the song at the given index in the playlist."""
        if 0 <= index < len(self.playlist):
            self.current_song_index = index
            media = self.instance.media_new(self.playlist[index])
            self.player.set_media(media)
            self.player.play()

    def next_track(self):
        """Skips to the next track."""
        print("Next Track (VLC)")
        self.play_song(self.current_song_index + 1)

    def previous_track(self):
        """Skips to the previous track."""
        print("Previous Track (VLC)")
        self.play_song(self.current_song_index - 1)

    def stop_playback(self):
        """Stops the music playback."""
        print("Stop Playback (VLC)")
        self.player.stop()

    def format_time(self, milliseconds):
        """Formats milliseconds to mm:ss format."""
        seconds = int(milliseconds / 1000)
        minutes = seconds // 60
        seconds %= 60
        return f"{minutes:02d}:{seconds:02d}"