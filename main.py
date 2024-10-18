import time
from LCD import LCDClass
from Controller import Controls

def main():
    """Main loop of the music player."""
    # Initialize the LCD Class
    lcd_inst = LCDClass()

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
                time.sleep(2)
                break
            elif media_choice == "spotify":
                from SpotifyMedia import SpotifyPlayer
                media_player_inst = SpotifyPlayer()
                lcd_inst.display_message("You have picked SPOTIFY")
                time.sleep(2)
                break
            else:
                lcd_inst.display_message("Invalid choice.")
                time.sleep(2)
                lcd_inst.display_message("Choose your src")
                time.sleep(1)
                lcd_inst.display_message("vlc or spotify ?")
                time.sleep(1)

        lcd_inst.display_message("Your device is ready !!")
        time.sleep(2)

        controls = Controls(media_player_inst, lcd_inst)  # Create a Controls instance
        controls.start()  # Start the keyboard listener

        while True:  # Main loop
            song_info = media_player_inst.get_current_song_info()
            lcd_inst.display_song_info(song_info)
            time.sleep(1)

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