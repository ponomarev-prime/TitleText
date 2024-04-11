import configparser
from PIL import Image, ImageDraw, ImageFont
from logger import logger
import json

def interpolate(f_co, t_co, interval):
    logger.debug('Function interpolate started')
    det_co =[(t - f) / interval for f , t in zip(f_co, t_co)]
    for i in range(interval):
        yield [round(f + det * i) for f, det in zip(f_co, det_co)]

def imaging(res_w, res_h, col_l, col_r, file_bg):
    logger.debug('Function imaging started')
    imgsize=(int(res_w),int(res_h))
    gradient = Image.new('RGBA', imgsize, color=0)
    draw = ImageDraw.Draw(gradient)
    f_co = (tuple(map(int, col_l.split(', '))))
    t_co = (tuple(map(int, col_r.split(', '))))
    for i, color in enumerate(interpolate(f_co, t_co, gradient.width * 2)):
        draw.line([(i, 0), (0, i)], tuple(color), width=1)
    gradient.save(file_bg)

def printer(file_bg, col_bg, print_text, file_font, font_corr, file_result):
    logger.debug('Function printer started')
    # Read the background image and convert to an RGB image with Alpha.
    with open(file_bg, 'rb') as file:
        bgr_img = Image.open(file)
        bgr_img = bgr_img.convert('RGBA')  # Give iamge an alpha channel.
        bgr_img_width, bgr_img_height = bgr_img.size
        cx, cy = bgr_img_width//2, bgr_img_height//2  # Center of image.
        
    # Create a transparent foreground to be result of non-text areas.
    fgr_img = Image.new('RGBA', bgr_img.size, color=(tuple(map(int, col_bg.split(', ')))))
    font_size = bgr_img_width//len(print_text)
    
    logger.debug(f'Font size without corr is {font_size}')
    
    font = ImageFont.truetype(file_font, font_size + int(font_corr))

    left, top, right, bottom = font.getbbox(print_text)  # Size of text w/font if rendered.
    txt_width = right - left
    txt_height = bottom - top

    tx, ty = cx - txt_width//2, cy - txt_height//2  # Center of text.

    mask_img = Image.new('L', bgr_img.size, color=255)
    mask_img_draw = ImageDraw.Draw(mask_img)
    mask_img_draw.text((tx, ty), print_text, fill=0, font=font, align='center')

    res_img = Image.composite(fgr_img, bgr_img, mask_img)

    logger.debug(f'Saving result image to {file_result}')
    res_img.save(file_result)

def collect_data_from_config(config_file):
    logger.debug('Collecting data from config file')
    
    config = configparser.ConfigParser()
    config.read(config_file, encoding="utf-8-sig")
    
    data = {}
    data['res_w'] = config.get("backgrounder", "RES_WIDTH")
    data['res_h'] = config.get("backgrounder", "RES_HEIGHT")

    data['col_l'] = config.get("backgrounder", "COLOUR_LEFT")
    logger.debug(f"config.ini :: col_l={data['col_l']}")
    data['col_r'] = config.get("backgrounder", "COLOUR_RIGHT")
    logger.debug(f"config.ini :: col_r={data['col_r']}")

    data['file_bg'] = config.get("backgrounder", "BACKGROUND_IMAGE_GEN")
    data['col_bg'] = config.get("printer", "BACKGROUND_COLOUR")
    data['print_text'] = config.get("printer", "THE_TEXT")
    data['file_font'] = config.get("printer", "FONT_FILE")
    data['font_corr'] = config.get("printer", "COEF_FONT_SIZE")
    data['file_result'] = config.get("printer", "RESULT_IMAGE_FILE")
    
    return data

def collect_data_from_json(json_file):
    logger.debug('Collecting data from JSON file')
    
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    backgrounder_data = data.get("backgrounder", {})
    printer_data = data.get("printer", {})
    
    collected_data = {}
    
    collected_data['res_w'] = backgrounder_data.get("res_width", "")
    collected_data['res_h'] = backgrounder_data.get("res_height", "")
    
    collected_data['col_l'] = ', '.join(map(str, backgrounder_data.get("colour_left", [])))
    logger.debug(f"config.json :: col_l={collected_data['col_l']}")
    collected_data['col_r'] = ', '.join(map(str, backgrounder_data.get("colour_right", [])))
    logger.debug(f"config.json :: col_r={collected_data['col_r']}")
    
    collected_data['file_bg'] = backgrounder_data.get("background_image_gen", "")
    
    collected_data['col_bg'] = printer_data.get("background_colour", "")
    collected_data['print_text'] = printer_data.get("the_text", "")
    collected_data['file_font'] = printer_data.get("font_file", "")
    collected_data['font_corr'] = printer_data.get("coef_font_size", "")
    collected_data['file_result'] = printer_data.get("result_image_file", "")
    
    return collected_data

def make_print(data):
    logger.debug('Function make_print started')
    imaging(data['res_w'], data['res_h'], data['col_l'], data['col_r'], data['file_bg'])
    printer(data['file_bg'], data['col_bg'], data['print_text'], data['file_font'], data['font_corr'], data['file_result'])

def main():
    logger.debug('Printer app started')
    
    # data = collect_data_from_config('config.ini')
    data = collect_data_from_json('config.json')
    make_print(data)

if __name__ == "__main__":
    main()