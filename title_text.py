from PIL import Image, ImageDraw, ImageFont

img = Image.new('RGB', (1366, 768), color = (13, 17, 23))

fnt = ImageFont.truetype('Archangelsk.ttf', 100)
text = 'Variable Text'
d = ImageDraw.Draw(img)

textwidth, textheight = d.textbbox((0, 0), text, font=fnt)[2:]
x = (1366 - textwidth) / 2
y = (768 - textheight) / 2

gradient = [(0, 0, 255), (255, 0, 255)]
d.text((x, y), text, font=fnt, fill=(201, 209, 217))

img.save('image.png')
