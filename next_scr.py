# "data/app_background_image.png"
# "result/next_result.png"
# 'data/fonts\Archangelsk.ttf'

from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(image, text, font_path, font_size_factor, text_color, text_position):
    """
    Добавляет текст на изображение.

    Args:
        image (PIL.Image.Image): Исходное изображение
        text (str): Текст для добавления на изображение
        font_path (str): Путь к файлу шрифта
        font_size_factor (float): Коэффициент размера шрифта относительно размера изображения (от 0 до 1)
        text_color (tuple): Цвет текста в формате RGB (например, (255, 255, 255) для белого цвета)
        text_position (tuple): Позиция текста на изображении в формате (x, y), где x и y - координаты в пикселях

    Returns:
        PIL.Image.Image: Изображение с добавленным текстом
    """
    draw = ImageDraw.Draw(image)
    font_size = int(image.height * font_size_factor)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(text_position, text, fill=text_color, font=font)
    return image

# Пример использования функции
# Загрузка изображения
background_image = Image.open('data/app_background_image.png')
# Текст для добавления на изображение
text = 'Пример текста'
# Путь к файлу шрифта
font_path = 'data/fonts\Archangelsk.ttf'
# Коэффициент размера шрифта (от 0 до 1)
font_size_factor = 0.2
# Цвет текста в формате RGB
text_color = (255, 255, 255)
# Позиция текста на изображении (по центру)
text_position = ((background_image.width - len(text) * int(background_image.height * font_size_factor)) // 2,
                 background_image.height // 2)
# Добавление текста на изображение
image_with_text = add_text_to_image(background_image, text, font_path, font_size_factor, text_color, text_position)
# Сохранение изображения с текстом
image_with_text.save('result/next_result.png')
