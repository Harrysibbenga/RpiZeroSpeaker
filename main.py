import time
from lcd import initialize_lcd

def main():
    """Main loop of the music player."""
    try:
        """Main loop of the music player."""
        # Get LCD objects
        lcd_image, lcd_draw, lcd_font, disp = initialize_lcd()
        
        if lcd_image is None:  # Check if initialization failed
            print("Error initializing LCD. Exiting...")
            return  # Exit the script

        while True:
            media_choice = input("Choose media player (vlc or spotify): ").lower()
            if media_choice == "vlc":
                from media_vlc import initialize_media, load_music, get_current_song_info, play_pause, next_track, previous_track, stop_playback
                break
            elif media_choice == "spotify":
                from media_spotify import initialize_media, get_current_song_info, play_pause, next_track, previous_track, stop_playback
                break
            else:
                print("Invalid choice. Please enter 'vlc' or 'spotify'.")

    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        disp.fill(0)
        disp.show()