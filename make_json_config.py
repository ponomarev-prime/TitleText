import configparser
import json

def ini_to_json(ini_file_path):
    config = configparser.ConfigParser()
    config.read(ini_file_path)

    data = {}

    for section in config.sections():
        section_data = {}
        for key, value in config.items(section):
            if ',' in value:
                value = tuple(map(int, value.split(',')))
            section_data[key] = value
        data[section] = section_data

    return data

def main():
    ini_file_path = 'config.ini'  # Замените на путь к вашему .ini файлу
    json_data = ini_to_json(ini_file_path)

    json_file_path = 'config.json'  # Путь к выходному JSON файлу
    with open(json_file_path, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f'JSON файл успешно создан: {json_file_path}')

if __name__ == "__main__":
    main()
