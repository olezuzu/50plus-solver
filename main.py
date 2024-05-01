import pyautogui
import time
import math

start_time = time.time()

# Function to find pixels with a specific color in a screenshot
def find_pixels_with_color(screenshot, target_color):
    matching_pixels = []
    width, height = screenshot.size
    for x in range(width):
        for y in range(height):
            pixel_color = screenshot.getpixel((x, y))
            if pixel_color == target_color:
                matching_pixels.append((x, y))
    return matching_pixels

# Function to calculate distance between two points
def calculate_distance(point1, point2):
    return ((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2) ** 0.5

# Take a screenshot of the entire screen
screenshot = pyautogui.screenshot()

# Define the color to search for
target_color = (171, 216, 238)
target_color_2 = (136, 0, 0)

# Find pixels with the first target color
matching_pixels = find_pixels_with_color(screenshot, target_color)

# Find the minimum and maximum x and y coordinates of the pixels with the target color
min_x = min(coord[0] for coord in matching_pixels)
max_x = max(coord[0] for coord in matching_pixels)
min_y = min(coord[1] for coord in matching_pixels)
max_y = max(coord[1] for coord in matching_pixels)

# Calculate the corners of the bounding square
top_left = (min_x, min_y)
top_right = (max_x, min_y)
bottom_left = (min_x, max_y)
bottom_right = (max_x, max_y)

# Calculate the length of one of the sides of the square
offset = (max_x - min_x) / 12  # Assuming the square is aligned with the x-axis

# Output corners coordinates and side length
print("Corners:")
print(f"Top Left: {top_left}")
print(f"Top Right: {top_right}")
print(f"Bottom Left: {bottom_left}")
print(f"Bottom Right: {bottom_right}")
print(f"Side Length: {offset}")

# Move mouse cursor to the top left corner with an offset
pyautogui.moveTo(top_left[0] + offset / 2, top_left[1] + offset / 2)

# Move to 11 positions to the right
visited_pixels = set()  # Set to keep track of visited pixels
for a in range(12):
    pyautogui.moveTo(top_left[0] + offset / 2, top_left[1] + offset / 2 + a * offset)
    for _ in range(11):
        pyautogui.click()  # Click after each movement
        pyautogui.press('e')  # Press the 'A' key
        current_position = pyautogui.position()
        visited_pixels.add((current_position[0], current_position[1]))
        pyautogui.move(offset, 0)
        time.sleep(0.1)  # Add a small delay for smooth movement
    pyautogui.click()  # Click after each row movement
    pyautogui.press('e')  # Press the 'A' key
    time.sleep(0.1)  # Add a small delay for smooth movement



# Loop through the alphabet except 'e'
for letter in 'nisratdhulcgmobwfkzpvßjyxq':
    # Take another screenshot
    screenshot = pyautogui.screenshot()

    # Find pixels with the second target color
    matching_pixels_2 = find_pixels_with_color(screenshot, target_color_2)

    # Keep track of visited coordinates
    visited_coordinates = set()

    # Function to move to a new pixel with target color, further than a given distance
    def move_to_new_pixel(further_than_distance):
        for pixel in matching_pixels_2:
            if pixel not in visited_coordinates:
                # Check distance from previously visited pixels
                distances = [calculate_distance(pixel, visited_pixel) for visited_pixel in visited_coordinates]
                if all(distance > further_than_distance for distance in distances):
                    # Move to the pixel
                    pyautogui.moveTo(pixel[0], pixel[1])
                    pyautogui.click()
                    pyautogui.press(letter)  # Press the 'N' key
                    time.sleep(0.1)
                    visited_coordinates.add(pixel)
                    return True
        return False

    # Define the distance threshold
    distance_threshold = 65

    # Move to new pixels until none are further than the threshold
    while move_to_new_pixel(distance_threshold):
        pass
    time.sleep(1)

# Print finish when there are no more available pixels
print("Finish")
print("--- %s seconds ---" % (time.time() - start_time))