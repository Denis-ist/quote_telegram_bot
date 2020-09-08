"""
Скрипт, генерирующий цитаты из текста
"""
import logging
from PIL import Image, ImageDraw, ImageFont
import textwrap

""" Путь к файлу шрифта """
FONT_PATH_OMAR = 'fonts/marta/Marta_Italic.otf'
FONT_PATH_JASON_MAIN = 'fonts/jason_main/19442.ttf'
# FONT_PATH_JASON_SUB = 'fonts/jason_sub/19514.otf'
""" Размер шрифта """
FONT_SIZE_OMAR = 65
FONT_SIZE_JASON_MAIN = 60
# FONT_SIZE_JASON_SUB = 65
""" Путь к изображению для фона """
IMG_BACKGROUND_OMAR = 'images/quote_bg.jpg'
IMG_BACKGROUND_JASON = 'images/quote_bg_2.jpg'


def generate_quote(text: str, command) -> Image:
    """
    Рисует текст на изображении.

    Вначале инициализируются базовые переменные:
    - изображение (im)
    - объект для рисования (draw)
    - ширина и высота изображения (w, h)
    - отступ между строками текста (padding)
    - список строк с шириной 20 символов (text_lines)
    - шрифт для текста (font)
    - стартовая высота (current_height)

    Далее перебираются строки и, для каждой строки текста происходит следующее:
    - Высчитывается ширина текущей строки с помощью draw.textsize()
    - Строка отрисовывается на изображении со следующими параметрами:
    -- отступ слева - чтобы текст был ровно посередине, он должен быть равен (w - w_text) / 2, однако, в данном случае,
       чтобы текст не наезжал на портрет, текст дополнительно сдвигается на 150 пикселей вправо
    -- отступ сверху равен текущей высоте (current_height)
    -- цвет текста (fill) равен rgb(193, 99, 55) или #C16337
    -- текст строки и шрифт
    - Отступ сверху (current_height) увеличивается для того, чтобы следующая строка не наезжала предыдущую

    :param text: str - текст для изображения цитаты
    :return: PIL.Image - объект изображения
    """
    if command == 1:
        back = IMG_BACKGROUND_OMAR
        font_path = FONT_PATH_OMAR
        font_size = FONT_SIZE_OMAR
        fill_color = (193, 99, 55)
        width = 20
        r_offset = 150
    elif command == 2:
        back = IMG_BACKGROUND_JASON
        font_path = FONT_PATH_JASON_MAIN
        font_size = FONT_SIZE_JASON_MAIN
        fill_color = (0, 0, 0)
        width = 13
        r_offset = 180
    im = Image.open(back)
    draw = ImageDraw.Draw(im)
    w, h = im.size
    if command == 1:
        height_of_image = h / 3
    elif command == 2:
        height_of_image = h / 6
    padding = font_size + 5
    text_lines = textwrap.wrap(text, width=width)
    font = ImageFont.truetype(font_path, font_size)
    current_height = height_of_image
    for line in text_lines:
        w_text, h_text = draw.textsize(line, font=font)
        draw.text(
            ((w - w_text) / 2 + r_offset, current_height),
            line,
            fill=fill_color,
            font=font,
        )
        current_height += padding
    if command == 2:
        draw.text((400, h - 90), '@JasonStathem', fill=fill_color,
                  font=font, )
    return im


if __name__ == '__main__':
    """ Код для проверки работы модуля """
    logging.basicConfig(level=logging.INFO)
    image = generate_quote(text=input('Введите текст > '))
    image.save('images/quote_text.jpg', quality=30)
    logging.info('Успех! Результат сохранился в images/quote_text.jpg')
