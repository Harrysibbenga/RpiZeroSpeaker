import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

def initialize_lcd():
    """Initializes the PiOLED display."""
    try:
        print("Initializing I2C...")
        i2c = busio.I2C(board.SCL, board.SDA)
        print("Initializing PiOLED...")
        disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

        print("Clearing display...")
        disp.fill(0)
        disp.show()

        print("Creating image...")
        width = disp.width
        height = disp.height
        image = Image.new("1", (width, height))

        print("Getting drawing object...")
        draw = ImageDraw.Draw(image)

        print("Loading font...")
        font = ImageFont.load_default()

        print("Displaying welcome message...")
        draw.text((0, 0), "Welcome!", font=font, fill=255)
        draw.text((0, 16), "Choose media:", font=font, fill=255)
        disp.image(image)
        disp.show()
        time.sleep(2)

        print("LCD initialized successfully!")
        return image, draw, font, disp

    except ValueError as e:
        print(f"Error initializing PiOLED: {e}")
        return None, None, None, None  # Return None for all objects on error

def display_song_info(image, draw, font, song_info):
    """Displays song information on the LCD (mocked on PC)."""
    # Clear the image
    draw.rectangle((0, 0, image.width, image.height), outline=0, fill=0)
    # Draw the song info on the image (adjust layout as needed)
    draw.text((0, 0), song_info["title"], font=font, fill=255)
    draw.text((0, 16), f"{song_info['artist']} - {song_info['duration']}", font=font, fill=255)
    # Show the image (mocked on PC - this won't display anything)
    image.show()