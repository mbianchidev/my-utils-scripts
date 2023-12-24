from PIL import Image

# A4 paper size in pixels at 300 DPI (8.27 x 11.69 inches)
width, height = int(8.27 * 300), int(11.69 * 300)
background_color = (255, 255, 255)  # White color (RGB)

# Create a new blank image
blank_image = Image.new('RGB', (width, height), background_color)

# Save the blank A4 image
blank_image.save('blank_A4.png')
