import os
from PIL import Image

def insert_png_into_jpeg_folder(jpeg_folder, png_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(jpeg_folder):
        if filename.endswith((".jpg", ".jpeg", ".JPG", ".JPEG")):
            jpeg_path = os.path.join(jpeg_folder, filename)
            jpeg_image = Image.open(jpeg_path)

            jpeg_width, jpeg_height = jpeg_image.size

            png_image = Image.open(png_path)

            png_width, png_height = png_image.size

            if (jpeg_width > jpeg_height):
                new_png_width = int(0.22 * jpeg_width)
            else:
                new_png_width = int(0.22 * 3 / 2 * jpeg_height)
            new_png_height = int(new_png_width * (png_height / png_width))

            x_position = jpeg_width - new_png_width - 65
            y_position = jpeg_height - new_png_height - 15

            resized_png_image = png_image.resize((new_png_width, new_png_height))

            jpeg_image_copy = jpeg_image.copy()

            jpeg_image_copy.paste(resized_png_image, (x_position, y_position), resized_png_image)

            output_path = os.path.join(output_folder, filename)
            jpeg_image_copy.save(output_path)

jpeg_folder_path = input("Введите абсолютный путь к папке с JPEG-изображениями: ")
png_path = input("Введите абсолютный путь к PNG-изображению: ")

output_folder = os.path.join(jpeg_folder_path, "output_logo")
insert_png_into_jpeg_folder(jpeg_folder_path, png_path, output_folder)
