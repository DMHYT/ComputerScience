from os.path import join
import re
from mss import mss
from numpy import asarray
import pytesseract as tess
from cv2 import bitwise_not, cvtColor, COLOR_BGR2RGB
from utils import get_monitor_size
from tesseract import get_tesseract_cmd_path


MONITOR_SIZE = get_monitor_size()
TIMELINE_WITHOUT_COLONS = re.compile(r'^\d{6}')
TIMELINE_WITH_COLONS = re.compile(r'^\d{2}:\d{2}:\d{2}')


def take_screenshot():
    with mss() as screenshoter:
        screen = screenshoter.grab({
            'left': 0,
            'top': 0,
            'width': MONITOR_SIZE[0],
            'height': MONITOR_SIZE[1]
        })
        img = asarray(screen)
        rgb = cvtColor(img, COLOR_BGR2RGB)
        rgb = bitwise_not(rgb)
        return rgb


def filter_data_dict(dic: dict) -> None:
    del dic['level']
    del dic['page_num']
    del dic['block_num']
    del dic['par_num']
    del dic['line_num']
    del dic['word_num']
    for i in range(len(dic['conf'])):
        if not isinstance(dic['conf'][i], int):
            dic['conf'][i] = int(float(dic['conf'][i]))
    done: bool = False
    while not done:
        try:
            index = dic['conf'].index(-1)
            for key in ('left', 'top', 'width', 'height', 'conf', 'text'):
                dic[key].pop(index)
        except ValueError:
            done = True


def structurize(dic: dict) -> list:
    return [
        (
            dic['left'][i],
            dic['top'][i],
            dic['width'][i],
            dic['height'][i],
            dic['conf'][i],
            dic['text'][i]
        ) for i in range(len(dic['left']))
    ]


def find_text(rgb, tess_path=get_tesseract_cmd_path()) -> list:
    if tess_path is None:
        print("Tesseract was not found on your machine :-(")
        return None
    else:
        tess.pytesseract.environ.setdefault(
            "TESSDATA_PREFIX",
            join(tess_path, "tessdata")
        )
        tess.pytesseract.tesseract_cmd = join(tess_path, "tesseract.exe")
        data: dict = tess.image_to_data(
            rgb, output_type=tess.pytesseract.Output.DICT,
            config=r'-l eng+rus'
        )
        filter_data_dict(data)
        result = structurize(data)
        # result = list(filter(lambda el: len(el[5]) > 4, structurize(data)))
        return result


def get_coords_for_bot(data: list) -> tuple:
    tx = ax = MONITOR_SIZE[0] + 1
    ty = ay = MONITOR_SIZE[1] + 1
    for item in data:
        print(item)
        if item[5] == "РЕКЛАМНАЯ":
            ax = item[0] + item[2]
            ay = item[1] + item[3] // 2
        if TIMELINE_WITH_COLONS.match(item[5]) or \
                TIMELINE_WITHOUT_COLONS.match(item[5]):
            print(item[5] + " matches regex!")
            if tx > item[0]:
                print("New tx and ty values set from " + item[5])
                tx = item[0] + item[2] // 2
                ty = item[1] + item[3] // 2
    return (tx, ty, ax, ay)


if __name__ == "__main__":
    from time import sleep
    sleep(3)
    [print(item) for item in find_text(take_screenshot())]