import configparser
from PIL import Image, ImageDraw, ImageFont



def interpolate(f_co, t_co, interval):
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]

def imaging(res_w, res_h, col_l, col_r, file_bg):
    imgsize=(int(res_w),int(res_h))
    gradient = Image.new('RGBA', imgsize, color=0)
    draw = ImageDraw.Draw(gradient)
    f_co = (tuple(map(int, col_l.split(', '))))
    t_co = (tuple(map(int, col_r.split(', '))))
    for i, color in enumerate(interpolate(f_co, t_co, gradient.width * 2)):
        draw.line([(i, 0), (0, i)], tuple(color), width=1)
    gradient.save(file_bg)

def printer(file_bg, col_bg, print_text, file_font, font_corr, file_result):
    # Read the background image and convert to an RGB image with Alpha.
    with open(file_bg, 'rb') as file:
        bgr_img = Image.open(file)
        bgr_img = bgr_img.convert('RGBA')  # Give iamge an alpha channel.
        bgr_img_width, bgr_img_height = bgr_img.size
        cx, cy = bgr_img_width//2, bgr_img_height//2  # Center of image.
    # Create a transparent foreground to be result of non-text areas.
    fgr_img = Image.new('RGBA', bgr_img.size, color=(tuple(map(int, col_bg.split(', ')))))
    font_size = bgr_img_width//len(print_text)
    
    print(f'Font size without corr :: {font_size}\n')
    
    font = ImageFont.truetype(file_font, font_size + int(font_corr))
    txt_width, txt_height = font.getsize(print_text)  # Size of text w/font if rendered.
    tx, ty = cx - txt_width//2, cy - txt_height//2  # Center of text.
    mask_img = Image.new('L', bgr_img.size, color=255)
    mask_img_draw = ImageDraw.Draw(mask_img)
    mask_img_draw.text((tx, ty), print_text, fill=0, font=font, align='center')
    res_img = Image.composite(fgr_img, bgr_img, mask_img)
    res_img.save(file_result)

def main():
    config = configparser.ConfigParser()
    config.read("app_config.ini", encoding="utf-8-sig")
    
    res_w = config.get("backgrounder", "RES_WIDTH")
    res_h = config.get("backgrounder", "RES_HEIGHT")
    col_l = config.get("backgrounder", "COLOUR_LEFT")
    col_r = config.get("backgrounder", "COLOUR_RIGHT")
    file_bg = config.get("backgrounder", "BACKGROUND_IMAGE_GEN")
    
    col_bg = config.get("printer", "BACKGROUND_COLOUR")
    print_text = config.get("printer", "THE_TEXT")
    file_font = config.get("printer", "FONT_FILE")
    font_corr = config.get("printer", "COEF_FONT_SIZE")
    file_result = config.get("printer", "RESULT_IMAGE_FILE")
    
    imaging(res_w, res_h, col_l, col_r, file_bg)
    
    printer(file_bg, col_bg, print_text, file_font, font_corr, file_result)

if __name__ == "__main__":
    main()