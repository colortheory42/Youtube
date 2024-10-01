from moviepy.editor import *
import numpy as np

# Define video parameters
duration = 60  # duration of the video in seconds
fps = 60  # frames per second
resolution = (1920, 1080)  # resolution of the video (width, height)

# Define colors
blue = [0, 0, 255]  # specific blue in RGB
yellow = [255, 255, 0]  # specific yellow in RGB

# Function to generate the correct color frame
def make_frame(t):
    # Switch between blue and yellow every second
    if int(t) % 2 == 0:
        return np.full((resolution[1], resolution[0], 3), blue, dtype=np.uint8)
    else:
        return np.full((resolution[1], resolution[0], 3), yellow, dtype=np.uint8)

# Create video clip
video = VideoClip(make_frame, duration=duration)

# Set FPS and export to mp4
video.write_videofile("blue_yellow_video.mp4", fps=fps)
