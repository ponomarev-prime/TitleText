import json

def read_json(json_file_path):
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

def main():
    json_file_path = 'config.json'  # Путь к вашему JSON файлу
    config = read_json(json_file_path)

    # Получение значений переменных
    res_w = config["backgrounder"]["res_width"]
    res_h = config["backgrounder"]["res_height"]
    col_l = tuple(config["backgrounder"]["colour_left"])
    col_r = tuple(config["backgrounder"]["colour_right"])
    file_bg = config["backgrounder"]["background_image_gen"]
    
    col_bg = config["printer"]["background_colour"]
    print_text = config["printer"]["the_text"]
    file_font = config["printer"]["font_file"]
    font_corr = config["printer"]["coef_font_size"]
    file_result = config["printer"]["result_image_file"]
    
    # Вывод значений переменных
    print("backgrounder:")
    print(f"RES_WIDTH: {res_w}")
    print(f"RES_HEIGHT: {res_h}")
    print(f"COLOUR_LEFT: {col_l}")
    print(f"COLOUR_RIGHT: {col_r}")
    print(f"BACKGROUND_IMAGE_GEN: {file_bg}")

    print("\nprinter:")
    print(f"BACKGROUND_COLOUR: {col_bg}")
    print(f"THE_TEXT: {print_text}")
    print(f"FONT_FILE: {file_font}")
    print(f"COEF_FONT_SIZE: {font_corr}")
    print(f"RESULT_IMAGE_FILE: {file_result}")

if __name__ == "__main__":
    main()
