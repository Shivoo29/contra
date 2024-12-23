import os

# Get the base directory of the project
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define paths for images
IMAGES_DIR = os.path.join(BASE_DIR, '..', 'images')

PLAYER_IMAGE_PATH = os.path.join(IMAGES_DIR, 'player.png')
