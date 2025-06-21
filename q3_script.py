
#   Question 3


import cv2
import os

# Load the image
image = cv2.imread('input.jpg')
if image is None:
    raise FileNotFoundError("Image 'input.jpg' not found.")

# Get image dimensions
rows, cols = image.shape[:2]
center = (cols / 2, rows / 2)

# Create results directory
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

# Save original image
cv2.imwrite(os.path.join(results_dir, '00_original.jpg'), image)
print("Saved: 00_original.jpg")

# Rotate by 45 degrees
rotation_matrix_45 = cv2.getRotationMatrix2D(center, 45, 1)
rotated_45 = cv2.warpAffine(image, rotation_matrix_45, (cols, rows))
cv2.imwrite(os.path.join(results_dir, '03_rotated_45deg.jpg'), rotated_45)
print("Saved: 03_rotated_45deg.jpg")

# Rotate by 90 degrees
rotation_matrix_90 = cv2.getRotationMatrix2D(center, 90, 1)
rotated_90 = cv2.warpAffine(image, rotation_matrix_90, (cols, rows))
cv2.imwrite(os.path.join(results_dir, '03_rotated_90deg.jpg'), rotated_90)
print("Saved: 03_rotated_90deg.jpg")

print(f"\nImage rotation completed. Outputs saved in '{results_dir}' folder.")
