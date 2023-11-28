import json
import os


#ПЕРЕИМЕНОВЫВАЕМ png МАСКИ ИЗ "task-8438-annotation-311-by-1-tag-Tiger-0.png" В "8438.png"
def rename_png_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            # Извлечь четыре цифры после "task-"
            new_filename = filename.split("task-")[1][:4] + ".png"

            # Полный путь к текущему файлу
            current_path = os.path.join(folder_path, filename)
            # Полный путь к новому файлу
            new_path = os.path.join(folder_path, new_filename)
            # Переименовать файл
            os.rename(current_path, new_path)

#РАЗБИРАЕМ json ПРОЕКТА LS НА json ПО КАЖДОМУ ФАЙЛУ + ПЕРЕИМЕНОВЫВАЕМ json И png В ИСХОДНОЕ ИМЯ ФАЙЛА ДО ПОПАДАНИЯ В LS
def split_json(input_file, folder_path):
    with open(input_file, 'r', encoding='utf-8') as file:
        data = json.load(file)

    for item in data:
        #получение оригинального имени файла
        image_name = item['file_upload']
        output_filename = f"{image_name[9:-4]}.json"

        #переименование png масок в оригинальное имя
        id = item['id']
        filename = f"{id}.png"
        new_filename = f"{output_filename[:-5]}.png"
        # Полный путь к текущему файлу
        current_path = os.path.join(folder_path, filename)
        # Полный путь к новому файлу
        new_path = os.path.join(folder_path, new_filename)
        # Переименовать файл
        os.rename(current_path, new_path)

        #Сохранение json по каждому файлу (ЕСЛИ JSON НЕ НУЖНЫ, ТО ЗАКОМЕНТИТЬ)
        with open("./JSON/" + output_filename, 'w', encoding='utf-8') as output_file:
            json.dump([item], output_file, ensure_ascii=False)

#путь до папки с png
rename_png_files("./PNG/")

# input_file - Файл проекта LS json, folder_path - папка где хранятся png маски
split_json("./project-21-at-2023-11-28-06-20-d6f9ff85.json", "./PNG/")