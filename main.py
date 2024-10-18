import time
from LCD import LCDClass
from Controller import Controls

def main():
    """Main loop of the music player."""
    # Initialize the LCD Class
    lcd_inst = LCDClass()
    time_constant = 5

    if lcd_inst.image is None:  # Check if initialization failed
        print("Error initializing LCD. Exiting...")
        return  # Exit the script

    try:
        while True:
            media_choice = input("Choose media player (vlc or spotify): ").lower()
            if media_choice == "vlc":
                from VLCMedia import VLCPlayer
                media_player_inst = VLCPlayer()
                media_player_inst.load_music("/home/rpi_speaker/Music")
                lcd_inst.display_message("You have picked VLC")
                time.sleep(time_constant)
                break
            elif media_choice == "spotify":
                from SpotifyMedia import SpotifyPlayer
                media_player_inst = SpotifyPlayer()
                lcd_inst.display_message("You have picked SPOTIFY")
                time.sleep(time_constant)
                break
            else:
                lcd_inst.display_message("Invalid choice.")
                time.sleep(time_constant)
                lcd_inst.display_message("Choose your src")
                time.sleep(time_constant)
                lcd_inst.display_message("vlc or spotify ?")
                time.sleep(time_constant)

        lcd_inst.display_message("Your device is ready !!")
        time.sleep(5)

        controls = Controls(media_player_inst, lcd_inst)  # Create a Controls instance
        controls.start()  # Start the keyboard listener

        while controls.running:  # Main loop
            song_info = media_player_inst.get_current_song_info()
            title = song_info['title']
            artist = song_info['artist']
            duration = song_info['duration']
            lcd_inst.display_message(f"{artist} - {duration}")
            time.sleep(time_constant)
            lcd_inst.display_message(f"{title} - {duration}")
            time.sleep(time_constant)

    except KeyboardInterrupt:
        print("Exiting due to KeyboardInterrupt...")
    finally:
        print("Resetting display and ending program")
        lcd_inst.display_message("Goodbye. Untill next time :)")
        time.sleep(5)
        lcd_inst.disp.fill(0)  # Clear the display
        lcd_inst.disp.show()

if __name__ == "__main__":
    main()