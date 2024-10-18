from pynput import keyboard

def initialize_controls(media_player):
    """Sets up keypress controls."""

    def on_press(key):
        try:
            if key.char == 'p':
                play_pause(media_player)
            # ... (map other keys to actions) ...
        except AttributeError:
            pass

    # ... (set up keyboard listener) ...