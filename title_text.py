from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1366, 768), color = 'black')

fnt = ImageFont.truetype('Archangelsk.ttf', 100)
text = 'Variable Text'
d = ImageDraw.Draw(img)

textwidth, textheight = d.textbbox((0, 0), text, font=fnt)[2:]
x = (1366 - textwidth) / 2
y = (768 - textheight) / 2

gradient = [(0, 0, 255), (255, 0, 255)]
d.text((x, y), text, font=fnt, fill=(200, 111, 200))

img.save('image.png')
