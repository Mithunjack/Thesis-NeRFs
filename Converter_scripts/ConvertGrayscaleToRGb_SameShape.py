
## For same size
import os
import cv2
import numpy as np

# Folder path containing grayscale BMP images
folder_path = '/data/stu225039/Datasets/JPG/Dataset_1'

# Output folder path to save enhanced RGB images
output_folder_path = '/data/stu225039/Datasets/RGB/Dataset_1'

# Get a list of grayscale BMP image files in the folder
grayscale_files = [f for f in os.listdir(folder_path) if f.endswith('.jpg')]

# Initialize a list to store the resized and enhanced RGB images
enhanced_images = []

# Initialize variables to store the dimensions of the first enhanced image
first_image_height = None
first_image_width = None

# Iterate through each grayscale BMP image
for idx, file_name in enumerate(grayscale_files):
    # Load grayscale BMP image
    grayscale_img = cv2.imread(os.path.join(folder_path, file_name), cv2.IMREAD_GRAYSCALE)

    # Apply denoising
    denoised_img = cv2.fastNlMeansDenoising(grayscale_img, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # Convert denoised grayscale image to RGB
    denoised_rgb = cv2.cvtColor(denoised_img, cv2.COLOR_GRAY2RGB)

    # Enhance sharpness
    enhanced_img = cv2.detailEnhance(denoised_rgb, sigma_s=10, sigma_r=0.15)

    # If it's the first image, store its dimensions
    if idx == 0:
        first_image_height, first_image_width, _ = enhanced_img.shape

    # Resize the enhanced RGB image to match the dimensions of the first image
    enhanced_img = cv2.resize(enhanced_img, (first_image_width, first_image_height))

    # Append the resized enhanced image to the list
    enhanced_images.append(enhanced_img)

    # Save the enhanced RGB image as JPG to the output folder
    output_file_name = os.path.splitext(file_name)[0] + '.jpg'
    output_file_path = os.path.join(output_folder_path, output_file_name)
    cv2.imwrite(output_file_path, enhanced_img)

    print(f"Converted {file_name} to enhanced RGB JPG.")

# Convert the list of enhanced images to a NumPy array
enhanced_images = np.array(enhanced_images)

# Check the shape of the resulting array
print("Shape of enhanced images array:", enhanced_images.shape)

print("Conversion and enhancement completed.")
