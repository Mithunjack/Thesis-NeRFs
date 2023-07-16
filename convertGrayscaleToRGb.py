import os
import cv2
import numpy as np

# Folder path containing grayscale BMP images
folder_path = 'Thesis-Dataset/TEM Tomography_Ex2/Janustomo2_thumb'

# Output folder path to save enhanced RGB images
output_folder_path = 'Thesis-Dataset/TEM Tomography_Ex2/output_RGB_black_and_white'

# Get a list of grayscale BMP image files in the folder
grayscale_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]

# Iterate through each grayscale BMP image
for file_name in grayscale_files:
    # Load grayscale BMP image
    grayscale_img = cv2.imread(os.path.join(folder_path, file_name), cv2.IMREAD_GRAYSCALE)

    # Apply denoising
    denoised_img = cv2.fastNlMeansDenoising(grayscale_img, None, h=10, templateWindowSize=7, searchWindowSize=21)

    # Convert denoised grayscale image to RGB
    denoised_rgb = cv2.cvtColor(denoised_img, cv2.COLOR_GRAY2RGB)

    # Enhance sharpness
    enhanced_img = cv2.detailEnhance(denoised_rgb, sigma_s=10, sigma_r=0.15)

    # Save the enhanced RGB image as JPG to the output folder
    output_file_name = os.path.splitext(file_name)[0] + '.jpg'
    output_file_path = os.path.join(output_folder_path, output_file_name)
    cv2.imwrite(output_file_path, enhanced_img)

    print(f"Converted {file_name} to enhanced RGB JPG.")

    # Load the saved enhanced RGB image
    rgb_image = cv2.imread(output_file_path)

    # Get the number of color channels in the image
    num_channels = rgb_image.shape[2]

    # Check if the image is in RGB format
    if num_channels == 3:
        print("The image is in RGB format.")
    else:
        print("The image is not in RGB format.")

print("Conversion and enhancement completed.")


# import os
# import cv2
# import numpy as np
# import matplotlib.pyplot as plt

# # Folder path containing grayscale BMP images
# folder_path = 'Thesis-Dataset/TEM Tomography_Ex2/Janustomo2_thumb'

# # Output folder path to save enhanced RGB images
# output_folder_path = 'Thesis-Dataset/TEM Tomography_Ex2/output_RGB_color_map'

# # Get a list of grayscale BMP image files in the folder
# grayscale_files = [f for f in os.listdir(folder_path) if f.endswith('.bmp')]

# # Iterate through each grayscale BMP image
# for file_name in grayscale_files:
#     # Load grayscale BMP image
#     grayscale_img = cv2.imread(os.path.join(folder_path, file_name), cv2.IMREAD_GRAYSCALE)

#     # Apply denoising
#     denoised_img = cv2.fastNlMeansDenoising(grayscale_img, None, h=10, templateWindowSize=7, searchWindowSize=21)

#     # Apply color mapping to the denoised grayscale image
#     colormap = cv2.COLORMAP_VIRIDIS
#     colored_img = cv2.applyColorMap(denoised_img, colormap)

#     # Save the colored RGB image as JPEG to the output folder
#     output_file_path = os.path.join(output_folder_path, os.path.splitext(file_name)[0] + '.jpg')
#     cv2.imwrite(output_file_path, colored_img)

#     print(f"Converted {file_name} to enhanced RGB using color mapping.")

# print("Conversion and enhancement completed.")
