import cv2
import numpy as np

# Load the video
video = cv2.VideoCapture("downloaded_video.mp4")

# Set to store unique colors
unique_colors = set()

# Read the frames of the video
success, frame = video.read()

while success:
    # Reshape the frame to a list of pixels (each pixel is a list of [B, G, R])
    reshaped_frame = frame.reshape(-1, 3)

    # Convert to tuples to make the pixel colors hashable
    for pixel in reshaped_frame:
        unique_colors.add(tuple(pixel))  # Add the color as a tuple (B, G, R)

    # Read the next frame
    success, frame = video.read()

video.release()

# Print all unique colors found in the video
print("Unique colors in the video:")
for color in unique_colors:
    print(f"RGB: ({int(color[0])}, {int(color[1])}, {int(color[2])})")
