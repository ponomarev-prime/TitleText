# "data/app_background_image.png"
# "result/next_result.png"
# 'data/fonts/Archangelsk.ttf'

from PIL import Image, ImageDraw, ImageFont

# Открытие фонового изображения
background_image = Image.open("data/app_background_image.png")

# Создание объекта ImageDraw для рисования на изображении
draw = ImageDraw.Draw(background_image)

# Задание параметров шрифта
font_size = int(background_image.width * 0.1)  # Пример: размер шрифта 10% от ширины изображения
font = ImageFont.truetype("data/fonts/Archangelsk.ttf", font_size)

# Задание текста и координат для первой строки (заголовка)
title_text = "Заголовок"
title_x = background_image.width // 2
title_y = background_image.height // 2 - font_size  # Пример: вертикальное смещение на половину размера шрифта

# Задание текста и координат для второй строки
subtitle_text = "Подзаголовок"
subtitle_x = background_image.width // 2
subtitle_y = background_image.height // 2 + font_size  # Пример: вертикальное смещение на половину размера шрифта

# Рисование текста на изображении
draw.text((title_x/2, title_y/2), title_text, fill="white", font=font, align='center')  # Заголовок
draw.text((subtitle_x/2, subtitle_y/2), subtitle_text, fill="white", font=font, align='left')  # Подзаголовок

# Сохранение изображения
background_image.save("result/next_result3.png")
