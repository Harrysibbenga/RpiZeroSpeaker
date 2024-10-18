from pynput import keyboard
import time
class Controls:
    def __init__(self, media_player, lcd_inst):
        """Initializes the keypress controls."""
        self.media_player = media_player
        self.lcd_inst = lcd_inst  # Store the LCD instance
        self.listener = None
        self.running = True  # Flag to indicate if the listener is running

    def start(self):
        """Starts the keyboard listener."""

        def on_press(key):
            try:
                if key.char == 's':  # Play/Pause
                    self.media_player.play_pause()
                elif key.char == 'n':  # Next
                    self.media_player.next_track()
                elif key.char == 'p':  # Previous
                    self.media_player.previous_track()
                elif key.char == 'q':  # Quit
                    self.lcd_inst.display_message("Exiting the Control listener ....")  # Display on LCD
                    time.sleep(2)
                    self.running = False  # Set the flag to False
                    self.stop()  # Stop the listener

            except AttributeError:
                pass  # Ignore special keys like Shift, Ctrl, etc.

        self.listener = keyboard.Listener(on_press=on_press)
        self.listener.start()
        self.running = True  # Set the flag to True

    def stop(self):
        """Stops the keyboard listener."""
        if self.listener:
            self.listener.stop()