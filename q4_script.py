
#   Question 4


import cv2
import numpy as np
import os

# Load the original image
image_path = 'input.jpg'
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Image input.jpg not found.")

# Define block sizes
block_sizes = [3, 5, 7]

# Create results directory
results_dir = "results"
os.makedirs(results_dir, exist_ok=True)

# Save original image
original_save_path = os.path.join(results_dir, '00_original.jpg')
cv2.imwrite(original_save_path, image)
print(f"Saved: {original_save_path}")

# Function to process the image with a given block size
def process_image(image, block_size):
    processed_image = np.copy(image)

    # Iterate over each block
    for y in range(0, image.shape[0], block_size):
        for x in range(0, image.shape[1], block_size):
            # Define the region of interest (ROI)
            roi = image[y:y+block_size, x:x+block_size]
            # Calculate the mean of the ROI (per channel)
            mean_color = np.mean(roi, axis=(0, 1))
            # Replace the ROI with the mean color (cast to uint8)
            processed_image[y:y+block_size, x:x+block_size] = mean_color.astype(np.uint8)

    return processed_image

# Process and save images for each block size
for size in block_sizes:
    processed_img = process_image(image, size)
    save_path = os.path.join(results_dir, f'processed_block_{size}x{size}.jpg')
    cv2.imwrite(save_path, processed_img)
    print(f"Saved: {save_path}")

print(f"\nImage block processing completed. Outputs saved in '{results_dir}' folder.")
