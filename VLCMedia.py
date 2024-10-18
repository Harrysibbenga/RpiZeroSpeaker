import subprocess

class VLCPlayer:
    def __init__(self):
        """Initializes the VLC media player."""
        print("Initializing VLC...")
        # No specific initialization needed for cvlc

    def load_music(self, music_dir):
        """Loads music from the given directory."""
        print(f"Loading music from {music_dir}...")
        try:
            # Get a list of supported audio files in the directory
            process = subprocess.run(['find', music_dir, '-type', 'f', '-name', '*.mp3', '-o', '-name', '*.wav', '-o', '-name', '*.flac'], 
                                   capture_output=True, text=True)
            files = process.stdout.splitlines()

            if files:
                self.playlist = files  # Store the files in the playlist
                for file in files:
                    print(file)  # Print each file path
            else:
                print("No supported audio files found in the directory.")

        except FileNotFoundError:
            print("Error: Music directory not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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