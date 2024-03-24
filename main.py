import os
from PIL import Image


def compress_images(folder_path):
    if not os.path.isdir(folder_path):
        print("Указанный путь не существует или не является папкой.")
        return

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path, filename)
        if os.path.isdir(filepath):
            if filename.lower() == "all":
                continue
            compress_images(filepath)
        elif os.path.isfile(filepath) and any(filename.lower().endswith(ext) for ext in ('.jpg', '.jpeg', '.png')):
            file_size_mb = os.path.getsize(filepath) / (1024 * 1024)
            if file_size_mb > 3:
                try:
                    img = Image.open(filepath)
                    img.save(filepath, quality=85)
                    print(f"Изображение {filename} было сжато.")
                except Exception as e:
                    print(f"Ошибка при сжатии изображения {filename}: {e}")
            else:
                print(f"Изображение {filename} не требует сжатия.")


folder_path = input("Введите путь к папке с изображениями: ")
compress_images(folder_path)
