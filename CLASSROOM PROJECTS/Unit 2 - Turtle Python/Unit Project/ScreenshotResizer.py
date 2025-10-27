import os
from PIL import Image


def resize_images(input_folder, output_folder, size=(800, 800)):
    """
    Resizes all images in an input folder to a specified size
    and saves them to an output folder.
    """
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of all files in the input folder
    files = os.listdir(input_folder)

    for file_name in files:
        input_path = os.path.join(input_folder, file_name)

        # Check if the file is an image
        try:
            img = Image.open(input_path)
            img.thumbnail(size, Image.Resampling.LANCZOS)
            new_img = Image.new("RGB", size, (255, 255, 255))
            paste_x = (size[0] - img.width) // 2
            paste_y = (size[1] - img.height) // 2
            new_img.paste(img, (paste_x, paste_y))
            output_path = os.path.join(output_folder, file_name)
            new_img.save(output_path)
            print(f"Resized and saved: {file_name}")
        # Skip files that are not images
        except IOError:
            print(f"Skipping non-image file: {file_name}")


# --- Usage ---
# Create an 'images' folder and an 'output' folder in the same directory as the script
input_folder_name = 'submissions (29)'
output_folder_name = 'resized_screenshots'

resize_images(input_folder_name, output_folder_name)