import sys
from time import sleep
from bot import Bot
from core import get_coords_for_bot, find_text, take_screenshot, NotEverythingFoundError


if __name__ == "__main__":
    print("Welcome to adbot by vsdum! Please follow the instructions...")
    bot = Bot()
    print("Bot object is initialized!")
    print("Now you will have 10 seconds to open your YouTube video's ad pauses editor page.")
    input("Press Enter to start this timer. ")
    sleep(10)
    data = find_text(take_screenshot())
    if data is None:
        sys.exit()
    else:
        try:
            coords = get_coords_for_bot(data)
            bot.specify_coords(coords[0], coords[1], coords[2], coords[3])
            bot.run()
            print("Thank you for using my bot! I wish you good luck with your YouTube channel!")
            input("Press Enter to exit. ")
        except NotEverythingFoundError:
            print("ERROR: Not all the needed coords were found by OCR system. Try again (try change browser theme to light, or increase the GUI scale)")