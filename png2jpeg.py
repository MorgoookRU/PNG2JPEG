import os
import time
from PIL import Image

# Путь к папке с изображениями
input_folder = 'input'
output_folder = 'output'

# Создаем папки, если они не существуют
os.makedirs(input_folder, exist_ok=True)
os.makedirs(output_folder, exist_ok=True)

# Ожидаем, пока в папке "input" появятся файлы
while True:
    files_to_convert = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]
    if files_to_convert:
        break
    else:
        print("Ожидание файлов в папке 'input'...")
        time.sleep(5)  # Подождать 5 секунд перед следующей проверкой

for filename in files_to_convert:
    # Открываем изображение в формате PNG
    img_png = Image.open(os.path.join(input_folder, filename))

    # Сохраняем изображение в формате JPEG
    root, _ = os.path.splitext(filename)
    jpg_file = os.path.join(output_folder, f'{root}.jpg')
    img_png.convert('RGB').save(jpg_file, 'JPEG')

print("Изображения успешно конвертированы и сохранены в папке 'output'!")
