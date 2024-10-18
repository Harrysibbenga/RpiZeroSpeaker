import time
from LCD import LCDClass
from SpotifyMedia import SpotifyPlayer
from VLCMedia import VLCPlayer
from Controller import Controls

media_player_inst = {}
lcd_inst = {}

def main():
    """Main loop of the music player."""
    # initialize the LCD Class
    lcd_inst = LCDClass()

    if lcd_inst.image is None:  # Check if initialization failed
        print("Error initializing LCD. Exiting...")
        return  # Exit the script
    
    media_choice = input("Choose media player (vlc or spotify): ").lower()

    if media_choice == "vlc":
        lcd_inst.display_message("You have picked VLC")
        media_player_inst = VLCPlayer()
        media_player_inst.load_music("/home/rpi_speaker/Music")
        time.sleep(5)
    elif media_choice == "spotify":
        lcd_inst.display_message("You have picked SPOTIFY")
        media_player_inst = SpotifyPlayer()
        time.sleep(5)
    else:
        print("Invalid choice. Please enter 'vlc' or 'spotify'.")

    try:
        while True:
            lcd_inst.display_message("Your device is ready !!")
            controls = Controls(media_player_inst)  # Create a Controls instance
            controls.start()

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