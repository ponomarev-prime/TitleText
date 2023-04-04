![](data/readme_title_text.png)

## Title Text

Скрипт для создания принта с текстом. Фон можно использовать любой, либо сгенерировать скриптом.

Just for fun!

RGB https://www.rapidtables.com/web/color/RGB_Color.html

Управляется из файла `config.ini`.

Скрипты работают на базе [Pillow](https://pypi.org/project/Pillow/).

`app_print_maker.py` скрипт творящий волшебство.

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
FONT_FILE: data\fonts\Archangelsk.ttf - файл шрифта
COEF_FONT_SIZE: 128 - корректировка ширины текста
THE_TEXT: TitleText - текст
RESULT_IMAGE_FILE: result\title_text.png - файл изображения

[common]
BACKGROUND_IMAGE_FILE: data\background_image.png - файл фонового изображения
```
## Цвета

Colours: Git balck: (13, 17, 23) Zero: (0, 0, 0, 0) Google doc black: (27, 27, 27) Google white: (255, 255, 255); 

blue > pink
COLOUR_LEFT: 253, 46, 216
COLOUR_RIGHT: 23, 214, 255

green > red
COLOUR_LEFT: 169, 220, 118
COLOUR_RIGHT: 218, 108, 98

some colours
BLACK, DARKGRAY, GRAY = ((0,0,0), (63,63,63), (127,127,127))
LIGHTGRAY, WHITE = ((191,191,191), (255,255,255))
BLUE, GREEN, RED = ((0, 0, 255), (0, 255, 0), (255, 0, 0))

Resolution: 2K 2560,1440 ; FHD 1920,1080 ; VK обложка 2х 3840,1536; | 4k 3840 x 2160 | 7200 4800

## Описание

Данный код является примером программы на языке программирования Python, которая создает изображение с градиентным фоном и наносит текст на это изображение. Программа использует библиотеки `configparser`, `random`, `PIL` (Python Imaging Library) для работы с изображениями.

Программа начинается с чтения настроек из файла `app_config.ini` с помощью библиотеки `configparser`. Затем она создает объект класса `backgrounder`, который представляет фоновое изображение. Этот объект инициализируется с помощью значений из файла конфигурации, таких как ширина и высота изображения, цвета левого и правого градиента, и файлового имени фонового изображения. Затем вызывается метод `imaging()`, который создает градиентное изображение и сохраняет его в файл.

Далее программа создает объект класса `printer`, который представляет текст, который будет нанесен на фоновое изображение. Этот объект инициализируется с помощью значений из файла конфигурации, таких как цвет фона, файл шрифта, поправка размера шрифта, текст, имя файла результата и имя файла фонового изображения. Затем вызывается метод `print()`, который открывает фоновое изображение, создает изображение с текстом, комбинирует их вместе с помощью маски и сохраняет результат в файл.