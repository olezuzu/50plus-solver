from PIL import Image
import pyautogui
import math

def is_color_within_radius(image, x, y, target_color, radius):
    width, height = image.size
    for i in range(max(0, x - radius), min(width, x + radius + 1)):
        for j in range(max(0, y - radius), min(height, y + radius + 1)):
            pixel_color = image.getpixel((i, j))
            if pixel_color == target_color:
                return True
    return False

# Example usage:
image_path = "screenshot.png"
target_color = (136, 0, 0)
radius = 65

image = Image.open(image_path)

for a in range(12):
    for b in range(12):
        x_coord = math.floor(336 + 66 / 2 + b * 66)
        y_coord = math.floor(262 + 66 / 2 + a * 66)
        if is_color_within_radius(image, x_coord, y_coord, target_color, radius):
            print("yes")
        else:
            print("no")