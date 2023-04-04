# "data/app_background_image.png"
# "result/next_result.png"
# 'data/fonts/Archangelsk.ttf'

from PIL import Image, ImageDraw, ImageFont
import textwrap

# Загрузка фонового изображения
background_image = Image.open("data/app_background_image.png")

# Создание объекта ImageDraw для рисования на изображении
draw = ImageDraw.Draw(background_image)

# Текст для отображения
text = "Это длинный текст, который нужно разбить на несколько строк для отображения на изображении."

# Шрифт и размер
font = ImageFont.truetype("arial.ttf", 124)  # Замените на путь к вашему шрифту и размер шрифта

# Разделение текста на строки
lines = textwrap.wrap(text, width=40)  # Здесь 30 - это максимальная ширина строки

# Координаты начальной точки для отображения текста
x = background_image.width // 2
y = background_image.height // 2

# Отображение каждой строки текста
for line in lines:
    # Рассчитываем размер текста
    text_width, text_height = draw.textsize(line, font=font)
    
    # Определение координат для выравнивания текста по центру
    x_start = x - text_width // 2
    y_start = y - text_height // 2
    
    # Рисуем текст на изображении
    draw.text((x_start, y_start), line, fill="white", font=font)
    
    # Сдвигаем координату y для отображения следующей строки текста
    y += text_height + 20  # 10 - это расстояние между строками

# Сохраняем результат
background_image.save("result/next_result2.png")

