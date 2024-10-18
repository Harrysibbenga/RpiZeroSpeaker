from pynput import keyboard

class Controls:
    def __init__(self, media_player, lcd_screen):
        """Initializes the keypress controls."""
        self.media_player = media_player
        self.lcd_screen = lcd_screen
        self.listener = None

    def start(self):
        """Starts the keyboard listener."""

        def on_press(key):
            try:
                if key.char == 's':  # Play/Pause
                    self.lcd_screen.display_message("Play/Pause pressed")
                    self.media_player.play_pause()
                elif key.char == 'n':  # Next
                    self.lcd_screen.display_message("Next pressed")
                    self.media_player.next_track()
                elif key.char == 'p':  # Previous
                    self.lcd_screen.display_message("Previous pressed")
                    self.media_player.previous_track()
                elif key.char == 'q':  # Quit
                    self.lcd_screen.display_message("Quit pressed")
                    print("Exiting...")
                    self.media_player.stop_playback()
                    # Add any cleanup or exit logic here
                    self.stop()  # Stop the listener

            except AttributeError:
                pass  # Ignore special keys like Shift, Ctrl, etc.

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()

    def stop(self):
        """Stops the keyboard listener."""
        if self.listener:
            self.listener.stop()