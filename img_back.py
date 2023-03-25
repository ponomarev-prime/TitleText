from PIL import Image, ImageDraw
import configparser


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8-sig")

RES_WIDTH = config.get("img_back", "RES_WIDTH")
RES_HEIGHT = config.get("img_back", "RES_HEIGHT")
COLOUR_LEFT = config.get("img_back", "COLOUR_LEFT")
COLOUR_RIGHT = config.get("img_back", "COLOUR_RIGHT")
BACKGROUND_IMAGE_FILE = config.get("common", "BACKGROUND_IMAGE_FILE")

print('')
print(f'Resolution :: {RES_WIDTH} x {RES_HEIGHT}')
print(f'Gradient :: ({COLOUR_LEFT}) > ({COLOUR_RIGHT})')
print(f'Path :: {BACKGROUND_IMAGE_FILE}')
print('')

def interpolate(f_co, t_co, interval):
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]


imgsize=(int(RES_WIDTH),int(RES_HEIGHT)) # 2K 2560,1440 ; FHD 1920,1080 ; VK обложка 2х 3840,1536 ;
gradient = Image.new('RGBA', imgsize, color=0)
draw = ImageDraw.Draw(gradient)

f_co = (tuple(map(int, COLOUR_LEFT.split(', '))))
t_co = (tuple(map(int, COLOUR_RIGHT.split(', '))))
for i, color in enumerate(interpolate(f_co, t_co, gradient.width * 2)):
    draw.line([(i, 0), (0, i)], tuple(color), width=1)
gradient.save(BACKGROUND_IMAGE_FILE)

print('')
print('OK')
print('')
