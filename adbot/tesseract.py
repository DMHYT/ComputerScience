from urllib.request import urlretrieve
from os import getcwd, mkdir, remove
from os.path import join, exists, isdir, dirname
from zipfile import ZipFile
from utils import find_files


TESS_ARCHIVE_URL = "https://download1478.mediafire.com/pi2i3mh4v4rg/mni87p6m5f7c1qt/Tesseract-OCR.zip"


def try_find_tesseract() -> str:
    for letter in list("ABCDEFGHIJKLMNOPQRSTUVYXYZ"):
        for pf_folder in ["Program Files", "Program Files (x86)"]:
            arr = find_files("tesseract.exe", \
                             join(letter + ":\\", pf_folder))
            if len(arr) > 0:
                return dirname(arr[0])
    return None


def get_tesseract_cmd_path():
    tess = try_find_tesseract()
    if tess is None:
        print("WARNING: Tesseract was not found on your machine! Downloading binaries archive...")
        archive_path = join(getcwd(), "tess-binaries.zip")
        urlretrieve(url=TESS_ARCHIVE_URL, filename=archive_path)
        print("DEBUG: Archive has been downloaded, extracting...")
        binaries_path = join(getcwd(), ".tess")
        if exists(binaries_path) and not isdir(binaries_path):
            remove(binaries_path)
        if not exists(binaries_path):
            mkdir(binaries_path)
        with ZipFile(archive_path) as archive:
            archive.extractall(binaries_path)
        print("DEBUG: Archive has been extracted!")
        remove(archive_path)
        print("DEBUG: Archive has been removed!")
        return binaries_path
    else:
        print("DEBUG: Tesseract was successfully found on your machine at " + tess)
        return tess


if __name__ == "__main__":
    get_tesseract_cmd_path()