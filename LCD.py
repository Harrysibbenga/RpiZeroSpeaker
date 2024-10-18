import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

class LCDClass:
    def __init__(self):
        """Initializes the PiOLED display."""
        try:
            print("Initializing I2C...")
            self.i2c = busio.I2C(board.SCL, board.SDA)
            print("Initializing PiOLED...")
            self.disp = adafruit_ssd1306.SSD1306_I2C(128, 32, self.i2c)

            print("Clearing display...")
            self.disp.fill(0)
            self.disp.show()

            print("Creating image...")
            width = self.disp.width
            height = self.disp.height
            self.image = Image.new("1", (width, height))

            print("Getting drawing object...")
            self.draw = ImageDraw.Draw(self.image)

            print("Loading font...")
            self.font = ImageFont.load_default()

            print("Displaying welcome message...")
            self.draw.text((0, 0), "Welcome!", font=self.font, fill=255)
            self.draw.text((0, 16), "Choose media:", font=self.font, fill=255)
            self.disp.image(self.image)
            self.disp.show()
            time.sleep(2)

            print("LCD initialized successfully!")

        except ValueError as e:
            print(f"Error initializing PiOLED: {e}")
            self.disp = None  # Set disp to None on error

    def display_song_info(self, song_info):
        """Displays song information on the LCD."""
        if self.disp is None:
            print("Error: LCD not initialized.")
            return

        # Clear the image
        self.draw.rectangle((0, 0, self.image.width, self.image.height), outline=0, fill=0)
        # Draw the song info on the image (adjust layout as needed)
        self.draw.text((0, 0), song_info["title"], font=self.font, fill=255)
        self.draw.text((0, 16), f"{song_info['artist']} - {song_info['duration']}", font=self.font, fill=255)
        # Display on the PiOLED
        self.disp.image(self.image)
        self.disp.show()