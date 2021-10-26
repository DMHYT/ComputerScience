from ctypes import windll
from os import walk
from os.path import join


def get_positive_int_input(hint: str) -> int:
    try:
        result = int(input(hint + ": "))
        if result <= 0:
            raise ValueError()
        else:
            return result
    except ValueError:
        print("ERROR! Input data must be of integer type. Try again...")
        return get_positive_int_input(hint)


def get_monitor_size() -> tuple:
    return (
        windll.user32.GetSystemMetrics(0),
        windll.user32.GetSystemMetrics(1)
    )


def find_files(filename, search_path) -> list:
    result = []
    for root, d, files in walk(search_path):
        if filename in files:
            result.append(join(root, filename))
    return result


if __name__ == "__main__":
    width, height = get_monitor_size()
    print("Your monitor is " + str(width) + "x" + str(height))