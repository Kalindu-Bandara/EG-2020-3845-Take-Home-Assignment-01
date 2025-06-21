
#   Question 1

import cv2
import numpy as np
import os

# Load the grayscale image
image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
if image is None:
    raise FileNotFoundError("Image 'input.jpg' not found.")

# Create the results directory
results_dir = 'results'
os.makedirs(results_dir, exist_ok=True)

# Save the original grayscale image
cv2.imwrite(os.path.join(results_dir, '00_original_gray.jpg'), image)
print("Saved original grayscale image.")

# Function to reduce intensity levels
def reduce_intensity_levels(image, levels):
    factor = 256 // levels
    reduced = (image // factor) * factor
    return reduced

# Reduce and save for powers of 2: 2, 4, 8, ..., 256
for power in range(1, 9):  # 2^1 to 2^8
    levels = 2 ** power
    reduced_img = reduce_intensity_levels(image, levels)
    filename = f'01_reduced_levels_{levels}.jpg'
    filepath = os.path.join(results_dir, filename)
    cv2.imwrite(filepath, reduced_img)
    print(f"Saved: {filename}")

print(f"\nAll reduced intensity images saved in '{results_dir}' folder.")
