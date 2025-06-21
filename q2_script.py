
#   Question 2


import cv2
import numpy as np
import os

# Load the image
image = cv2.imread('input.jpg')
if image is None:
    raise FileNotFoundError("Image 'input.jpg' not found.")

# Create results directory
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

# Save original image
cv2.imwrite(os.path.join(results_dir, '00_original.jpg'), image)
print("Saved: 00_original.jpg")

# Define spatial averaging function
def apply_average_filter(image, kernel_size):
    return cv2.blur(image, (kernel_size, kernel_size))

# Apply and save filtered images
for size in [3, 10, 20]:
    blurred = apply_average_filter(image, size)
    filename = f'02_average_{size}x{size}.jpg'
    filepath = os.path.join(results_dir, filename)
    cv2.imwrite(filepath, blurred)
    print(f"Saved: {filename}")

print(f"\nAll spatial averaging outputs saved in '{results_dir}' folder.")
