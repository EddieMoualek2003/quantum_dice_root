from .dice_game_gui import *
from .dice_game_console import *
from .engines.env_detection import *
# dice_console_main()

mode = None

def set_mode(mode):
    # mode = None
    ## Start by env detection
    env = detect_environment()
    if "windows" in env['os'].lower():
        mode = "GUI"
    elif "linux" in env['os'].lower() and env['is_raspberry_pi']:
        print("Pi Mode")
        if not env['is_headless']:
            mode = "GUI"
        elif env['is_headless']:
            mode = "con"
    return mode


# if __name__ == "__main__":
#     mode = set_mode(mode)
#     if mode == "GUI":
#         dice_gui_main()
#     elif mode == "con":
#         dice_console_main()

def main():
    dice_gui_main()