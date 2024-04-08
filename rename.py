import os


def rename_files(folder_path):
    if not os.path.isdir(folder_path):
        print("Указанный путь не является директорией")
        return

    files = os.listdir(folder_path)

    for filename in files:
        parts = filename.split('_')
        if len(parts) == 3 and parts[0] == 'IMG' and parts[2].endswith('.raw'):
            new_filename = f"{parts[0]}_{parts[1]}.raw"
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Файл {filename} переименован в {new_filename}")


folder_path = input("Введите путь к папке: ")
rename_files(folder_path)