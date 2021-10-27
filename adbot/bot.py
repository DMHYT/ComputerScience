import pyautogui
from utils import get_positive_int_input as int_input


class Bot:

    def __init__(self) -> None:
        self.minutes = int_input("Enter your video duration in minutes")
        self.seconds = int_input("Enter the seconds left after minutes")
        self.interval = int_input("Enter integer interval between ad pauses")
        self.current_minutes = 0
        self.current_seconds = 0
        self.timeline_x = 0
        self.timeline_y = 0
        self.add_x = 0
        self.add_y = 0

    def specify_coords(self, tx: int, ty: int, ax: int, ay: int) -> None:
        self.timeline_x = tx
        self.timeline_y = ty
        self.add_x = ax
        self.add_y = ay

    def __can_time_be_incremented__(self) -> bool:
        return self.current_minutes < self.minutes or \
            (self.current_minutes == self.minutes and \
                self.current_seconds <= self.seconds)
    
    def __increment_time__(self) -> None:
        self.current_seconds += self.interval
        if self.current_seconds >= 60:
            self.current_minutes += self.current_seconds // 60
            self.current_seconds %= 60

    def __write_colon__(self) -> None:
        pyautogui.press(["shift", ":"])

    def __clear_timeline__(self) -> None:
        pyautogui.moveTo(x=self.timeline_x, y=self.timeline_y)
        pyautogui.click(clicks=3, interval=0.1)
        pyautogui.press("backspace")

    def __add_pause__(self) -> None:
        pyautogui.moveTo(x=self.add_x, y=self.add_y)
        pyautogui.click()
    
    def __write_time__(self) -> None:
        pyautogui.write("0" + str(self.current_minutes) \
            if self.current_minutes < 10 else str(self.current_minutes))
        self.__write_colon__()
        pyautogui.write("0" + str(self.current_seconds) \
            if self.current_seconds < 10 else str(self.current_seconds))
        self.__write_colon__()
        pyautogui.write("00")
    
    def run(self) -> None:
        while self.__can_time_be_incremented__():
            self.__clear_timeline__()
            self.__write_time__()
            self.__add_pause__()
            self.__increment_time__()
        print("Finished!")