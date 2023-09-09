from PIL import Image
import os

# Input and output directories
input_directory = "/data/stu225039/Datasets/BMP/Dataset_4"
output_directory = "/data/stu225039/Datasets/JPG/Dataset_4"

# Ensure the output directory exists
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# List all BMP files in the input directory
bmp_files = [f for f in os.listdir(input_directory) if f.lower().endswith(".bmp")]

# Convert BMP to JPG
for bmp_file in bmp_files:
    bmp_path = os.path.join(input_directory, bmp_file)
    jpg_file = os.path.splitext(bmp_file)[0] + ".jpg"
    jpg_path = os.path.join(output_directory, jpg_file)

    # Open the BMP image and save it as JPG without changing the size
    try:
        with Image.open(bmp_path) as img:
            img.convert('RGB').save(jpg_path, "JPEG")
            print(f"Converted {bmp_file} to {jpg_file}")
    except Exception as e:
        print(f"Error converting {bmp_file}: {str(e)}")

print("Conversion completed.")
