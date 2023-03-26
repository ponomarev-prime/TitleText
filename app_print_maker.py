#

import configparser
from random import randint
from PIL import Image, ImageDraw, ImageFont

config = configparser.ConfigParser()
config.read("app_config.ini", encoding="utf-8-sig")

en_ikato = ["Alfa", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliett", "Kilo", "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor", "Whiskey", "Xray", "Yankee", "Zulu"]


class backgrounder:
    def __init__(self, name, res_w, res_h, col_l, col_r, file_bg):
        self.name = name
        self.res_w = res_w
        self.res_h = res_h
        self.col_l = col_l
        self.col_r = col_r
        self.file_bg = file_bg

    def interpolate(self, f_co, t_co, interval):
        det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
        for i in range(interval):
            yield [round(f + det * i) for f, det in zip(f_co, det_co)]
    
    def imaging(self):
        imgsize=(int(self.res_w),int(self.res_h))
        gradient = Image.new('RGBA', imgsize, color=0)
        draw = ImageDraw.Draw(gradient)
        f_co = (tuple(map(int, self.col_l.split(', '))))
        t_co = (tuple(map(int, self.col_r.split(', '))))
        for i, color in enumerate(self.interpolate(f_co, t_co, gradient.width * 2)):
            draw.line([(i, 0), (0, i)], tuple(color), width=1)
        gradient.save(self.file_bg)


class printer():
    def __init__(self, name, col_bg, file_font, font_corr, print_text, file_result, file_bg):
        self.name = name
        self.col_bg = col_bg
        self.file_font = file_font
        self.font_corr = font_corr
        self.print_text = print_text
        self.file_result = file_result
        self.file_bg = file_bg
    
    def print(self):
        # Read the background image and convert to an RGB image with Alpha.
        with open(self.file_bg, 'rb') as file:
            bgr_img = Image.open(file)
            bgr_img = bgr_img.convert('RGBA')  # Give iamge an alpha channel.
            bgr_img_width, bgr_img_height = bgr_img.size
            cx, cy = bgr_img_width//2, bgr_img_height//2  # Center of image.
        # Create a transparent foreground to be result of non-text areas.
        fgr_img = Image.new('RGBA', bgr_img.size, color=(tuple(map(int, self.col_bg.split(', ')))))
        font_size = bgr_img_width//len(self.print_text)
        print(f'Font size without corr :: {font_size}\n')
        font = ImageFont.truetype(self.file_font, font_size + int(self.font_corr))
        txt_width, txt_height = font.getsize(self.print_text)  # Size of text w/font if rendered.
        tx, ty = cx - txt_width//2, cy - txt_height//2  # Center of text.
        mask_img = Image.new('L', bgr_img.size, color=255)
        mask_img_draw = ImageDraw.Draw(mask_img)
        mask_img_draw.text((tx, ty), self.print_text, fill=0, font=font, align='center')
        res_img = Image.composite(fgr_img, bgr_img, mask_img)
        res_img.save(self.file_result)


bg = backgrounder(
    str("bg::"+en_ikato[randint(0, 25)]+en_ikato[randint(0, 25)]+en_ikato[randint(0, 25)]),
    config.get("backgrounder", "RES_WIDTH"), 
    config.get("backgrounder", "RES_HEIGHT"), 
    config.get("backgrounder", "COLOUR_LEFT"), 
    config.get("backgrounder", "COLOUR_RIGHT"),
    config.get("common", "BACKGROUND_IMAGE_FILE")
    )

print(bg.__dict__)

bg.imaging()

pr = printer(
    str("pr::"+en_ikato[randint(0, 25)]+en_ikato[randint(0, 25)]+en_ikato[randint(0, 25)]),
    config.get("printer", "BACKGROUND_COLOUR"), 
    config.get("printer", "FONT_FILE"), 
    config.get("printer", "COEF_FONT_SIZE"), 
    config.get("printer", "THE_TEXT"), 
    config.get("printer", "RESULT_IMAGE_FILE"), 
    config.get("common", "BACKGROUND_IMAGE_FILE")
)

print(pr.__dict__)

pr.print()