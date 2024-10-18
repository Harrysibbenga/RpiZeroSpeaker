import requests

class SpotifyPlayer:
    def __init__(self, time_constant):
        """Initializes the Spotify player and gets the amplifier's IP address."""
        self.time_constant = time_constant
        print("Initializing Spotify...")

        # Get amplifier's IP address from user input (with default)
        amp_ip = input("Enter the amplifier's IP address (default: 192.168.1.146): ")
        if not amp_ip:
            amp_ip = "192.168.1.146"  # Use default if no input

        self.amp_ip = amp_ip
        self.url = f"http://{self.amp_ip}/httpapi.asp?command=getPlayerStatus"
        self.current_track_id = None

    def get_current_song_info(self):
        """Gets information about the currently playing song from the amplifier."""
        print("Getting song information (Spotify)...")
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            data = response.json()

            # Check if a track is playing and if it's a new track
            track_id = data["Title"]["Artist"]["totlen"]

            if data['status'] == 'play':
                if track_id != self.current_track_id:
                    self.current_track_id = track_id
                    return {
                        "title": data["Title"],
                        "artist": data["Artist"],
                    }
                else:
                    # Track hasn't changed, return None to avoid unnecessary updates
                    return None
            else:
                print("No track playing.")
                return {"title": "No track playing", "artist": ""}

        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return {"title": "Error", "artist": "Error", "duration": "Error"}

    def format_time(self, seconds):
        """Formats seconds to mm:ss format."""
        minutes = int(seconds // 60)
        seconds = int(seconds % 60)
        return f"{minutes:02d}:{seconds:02d}"