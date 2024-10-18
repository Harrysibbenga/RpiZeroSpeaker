from pynput import keyboard

class Controls:
    def __init__(self, media_player):
        """Initializes the keypress controls."""
        self.media_player = media_player
        self.listener = None

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