import pyautogui
import time



# Take another screenshot
screenshot = pyautogui.screenshot()


width, height = screenshot.size
# Define the color to search for
target_color = (136, 0, 0)

# List to store coordinates of pixels with the target color
matching_pixels = []

# Loop through each pixel of the screenshot
for x in range(width):
    for y in range(height):
        # Get the RGB values of the current pixel
        pixel_color = screenshot.getpixel((x, y))
        # Check if the current pixel matches the target color
        if pixel_color == target_color:
            # Check if there's no nearby pixel within the specified radius
            nearby_pixels = [(xx, yy) for xx in range(x - 65, x + 66) for yy in range(y - 65, y + 66)
                             if 0 <= xx < width and 0 <= yy < height]
            nearby_pixels.remove((x, y))  # Remove the pixel itself from nearby pixels
            nearby_pixels_colors = [screenshot.getpixel(coord) for coord in nearby_pixels]
            if target_color not in nearby_pixels_colors:
                matching_pixels.append((x, y))

# Click on the pixels found
for pixel in matching_pixels:
    pyautogui.click(pixel[0], pixel[1])