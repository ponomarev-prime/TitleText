from PIL import Image, ImageDraw

# Создаем изображение
img = Image.new('RGB', (500, 500), color='white')

# Создаем объект ImageDraw
draw = ImageDraw.Draw(img)

# Определяем начальный и конечный цвета градиента
start_color = (255, 0, 0)
end_color = (0, 0, 255)

# Применяем градиентный фон
draw.linear_gradient(
    (0, 0, img.width, img.height), 
    start_color, 
    end_color, 
    gradient='linear'
)

# Сохраняем изображение
img.save('gradient.png')