import board
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306
import time

def initialize_lcd():
    """Initializes the PiOLED display."""
    # Create I2C interface
    i2c = busio.I2C(board.SCL, board.SDA)
    # Create PiOLED display object
    disp = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)
    # Clear display
    disp.fill(0)
    disp.show()
    # Create blank image for drawing
    width = disp.width
    height = disp.height
    image = Image.new("1", (width, height))
    # Get drawing object to draw on image
    draw = ImageDraw.Draw(image)
    # Load default font
    font = ImageFont.load_default()

    # Display welcome message
    draw.text((0, 0), "Welcome!", font=font, fill=255)
    draw.text((0, 16), "Choose media:", font=font, fill=255)
    disp.image(image)  # Display the image on the PiOLED
    disp.show()
    time.sleep(2)  # Show the message for 2 seconds

    return image, draw, font, disp

def display_song_info(image, draw, font, song_info):
    """Displays song information on the LCD (mocked on PC)."""
    # Clear the image
    draw.rectangle((0, 0, image.width, image.height), outline=0, fill=0)
    # Draw the song info on the image (adjust layout as needed)
    draw.text((0, 0), song_info["title"], font=font, fill=255)
    draw.text((0, 16), f"{song_info['artist']} - {song_info['duration']}", font=font, fill=255)
    # Show the image (mocked on PC - this won't display anything)
    image.show()