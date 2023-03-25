![](data/readme_title_text.png)

## Title Text

Создаёт текст в центре изображения. В качестве изображения используется градиент.

Just for fun!

RGB https://www.rapidtables.com/web/color/RGB_Color.html

Управляется из файла `config.ini`.

Скрипты работают на базе [Pillow](https://pypi.org/project/Pillow/).

`img_back.py` создаёт бэкграунд. 

`img_text_gen2.py` создаёт изображение с текстом из бэкграунда.

---

Как это работает:

Настраиваем фон в `config.ini`:
```
[img_back]
RES_WIDTH: 7200 - ширина изображения
RES_HEIGHT: 4800 - высота изображения
COLOUR_LEFT: 253, 46, 216 - градиентный цвет слева
COLOUR_RIGHT: 23, 214, 255 - градиентный цвет справа
```

Изображение со шрифтом:
```
[text_gen]
BACKGROUND_COLOUR: 13, 13, 13 - цвет фона изображения
FONT_FILE: data\Archangelsk.ttf - файл шрифта
COEF_FONT_SIZE: 128 - корректировка ширины текста
THE_TEXT: TitleText - текст
RESULT_IMAGE_FILE: result\title_text.png - файл изображения

[common]
BACKGROUND_IMAGE_FILE: data\background_image.png - файл фонового изображения шрифта
```

---

`baranch rm`