from PIL import Image, ImageDraw

# Define A4 dimensions in pixels (assuming 300 DPI for print quality)
width, height = 2480, 3508  # A4 dimensions in pixels

# Create a new blank image with a white background
image = Image.new('RGB', (width, height), 'white')
draw = ImageDraw.Draw(image)

# Calculate the width for the white side (66% of the total width)
white_width = width * 0.57

# Define the coordinates for the white area
white_box = [(0, 0), (white_width, height)]

# Fill the white area with the desired color (e.g., white)
draw.rectangle(white_box, fill='white')

# Calculate the width for the blue side (33% of the total width)
blue_width = width * 0.43

# Define the coordinates for the blue area
blue_box = [(white_width, 0), (width, height)]

# Fill the blue area with a darker blue color (adjust the color as needed)
draw.rectangle(blue_box, fill='#00008b')  # Dark blue color (hex code)

# Save the image as a PNG file
image.save('split_image.png', 'PNG')
