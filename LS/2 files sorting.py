import os
from random import shuffle

#РАЗДЕЛЕНИЕ ФАЙЛОВ НА trainval, test, valid ПО ИМЕНАМ В ПАПКЕ PNG В СООТНОШЕНИИ 70/20/10

images_folder = './PNG/'

# Получаем список всех PNG файлов в папке
png_files = [file for file in os.listdir(images_folder) if file.lower().endswith('.png')]

# Перемешиваем список для случайного распределения
shuffle(png_files)

# Рассчитываем количество файлов для каждого списка
total_files = len(png_files)
trainval_count = int(0.7 * total_files)
test_count = int(0.2 * total_files)
valid_count = total_files - trainval_count - test_count

# Создаем списки для каждого файла
trainval_files = png_files[:trainval_count]
test_files = png_files[trainval_count:trainval_count + test_count]
valid_files = png_files[trainval_count + test_count:]
list_files = png_files

# Функция для записи списка файлов в файл
def write_to_file(file_list, filename):
    with open(filename, 'w') as f:
        for file in file_list:
            f.write(file.split('.')[0] + '\n')

# Записываем списки в соответствующие файлы
write_to_file(trainval_files, 'trainval.txt')
write_to_file(test_files, 'test.txt')
write_to_file(valid_files, 'valid.txt')
write_to_file(list_files, 'list.txt')