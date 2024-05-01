from PIL import Image

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
given_pixel_x = 360
given_pixel_y = 460

image = Image.open(image_path)
result = is_color_within_radius(image, given_pixel_x, given_pixel_y, target_color, radius)

if result:
    print("The color is within the radius of the given pixel.")
else:
    print("The color is not within the radius of the given pixel.")
