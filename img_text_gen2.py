from PIL import Image, ImageDraw, ImageFont
import configparser


config = configparser.ConfigParser()
config.read("config.ini", encoding="utf-8-sig")


BACKGROUND_IMAGE_FILE = config.get("common", "BACKGROUND_IMAGE_FILE")
BACKGROUND_COLOUR = config.get("text_gen", "BACKGROUND_COLOUR")
FONT_FILE = config.get("text_gen", "FONT_FILE")
COEF_FONT_SIZE = config.get("text_gen", "COEF_FONT_SIZE")
THE_TEXT = config.get("text_gen", "THE_TEXT")
RESULT_IMAGE_FILE = config.get("text_gen", "RESULT_IMAGE_FILE")

# Read the background image and convert to an RGB image with Alpha.
with open(BACKGROUND_IMAGE_FILE, 'rb') as file:
    bgr_img = Image.open(file)
    bgr_img = bgr_img.convert('RGBA')  # Give iamge an alpha channel.
    bgr_img_width, bgr_img_height = bgr_img.size
    cx, cy = bgr_img_width//2, bgr_img_height//2  # Center of image.

# Create a transparent foreground to be result of non-text areas.
fgr_img = Image.new('RGBA', bgr_img.size, color=(tuple(map(int, BACKGROUND_COLOUR.split(', ')))))

font_size = bgr_img_width//len(THE_TEXT)
print(font_size)

font = ImageFont.truetype(FONT_FILE, font_size + int(COEF_FONT_SIZE))

txt_width, txt_height = font.getsize(THE_TEXT)  # Size of text w/font if rendered.
tx, ty = cx - txt_width//2, cy - txt_height//2  # Center of text.

mask_img = Image.new('L', bgr_img.size, color=255)
mask_img_draw = ImageDraw.Draw(mask_img)
mask_img_draw.text((tx, ty), THE_TEXT, fill=0, font=font, align='center')

res_img = Image.composite(fgr_img, bgr_img, mask_img)
res_img.save(RESULT_IMAGE_FILE)
#res_img.show()

print('')
print('OK')
print('')