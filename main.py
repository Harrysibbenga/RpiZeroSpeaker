import time
from lcd import initialize_lcd, display_song_info
#from controls import initialize_controls

def main():
    """Main loop of the music player."""
    try:
        # Get LCD objects
        lcd_image, lcd_draw, lcd_font, disp = initialize_lcd() 

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

        # media_player = initialize_media()
        # initialize_controls(media_player)

        # if media_choice == "vlc":
        #     load_music(media_player, "/home/rpi_speaker/Music")

        # while True:
        #     song_info = get_current_song_info(media_player)
        #     display_song_info(lcd_image, lcd_draw, lcd_font, song_info)  # Pass LCD objects
        #     time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
    finally:
        disp.fill(0)
        disp.show()