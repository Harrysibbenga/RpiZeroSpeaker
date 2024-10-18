import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

def initialize_lcd():
    """Initializes the PiOLED display (mocked on PC)."""
    # Mock the display size (adjust if needed)
    width = 128
    height = 32
    image = Image.new("1", (width, height))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    
    # Display welcome message
    draw.text((0, 0), "Welcome!", font=font, fill=255)
    draw.text((0, 16), "Choose media:", font=font, fill=255)
    image.show()  # Mocked on PC - won't display anything
    time.sleep(2)  # Show the message for 2 seconds

    return image, draw, font  # Return the image, drawing object, and font

def display_song_info(image, draw, font, song_info):
    """Displays song information on the LCD (mocked on PC)."""
    # Clear the image
    draw.rectangle((0, 0, image.width, image.height), outline=0, fill=0)
    # Draw the song info on the image (adjust layout as needed)
    draw.text((0, 0), song_info["title"], font=font, fill=255)
    draw.text((0, 16), f"{song_info['artist']} - {song_info['duration']}", font=font, fill=255)
    # Show the image (mocked on PC - this won't display anything)
    image.show()