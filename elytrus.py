import time, os, ctypes, msvcrt, subprocess # Time for the delay, os to center the text
from ctypes import wintypes

wait = 0.1 # Delay between each line

# Clear the screen
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def maximise(lines=None):
    kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
    user32 = ctypes.WinDLL('user32', use_last_error=True)

    SW_MAXIMIZE = 3

    kernel32.GetConsoleWindow.restype = wintypes.HWND
    kernel32.GetLargestConsoleWindowSize.restype = wintypes._COORD
    kernel32.GetLargestConsoleWindowSize.argtypes = (wintypes.HANDLE,)
    user32.ShowWindow.argtypes = (wintypes.HWND, ctypes.c_int)
    fd = os.open('CONOUT$', os.O_RDWR)
    try:
        hCon = msvcrt.get_osfhandle(fd)
        max_size = kernel32.GetLargestConsoleWindowSize(hCon)
        if max_size.X == 0 and max_size.Y == 0:
            raise ctypes.WinError(ctypes.get_last_error())
    finally:
        os.close(fd)
    cols = max_size.X
    hWnd = kernel32.GetConsoleWindow()
    if cols and hWnd:
        if lines is None:
            lines = max_size.Y
        else:
            lines = max(min(lines, 9999), max_size.Y)

        subprocess.check_call('mode.com con cols={} lines={}'.format(cols, lines))
        user32.ShowWindow(hWnd, SW_MAXIMIZE)

# Intro
def intro():
    width = os.get_terminal_size().columns # Width of the console
    print(r"""         _               _      _        _          _                _         _                       _        """.center(width))
    time.sleep(wait)
    print(r"""        /\ \            _\ \   /\ \     /\_\       /\ \             /\ \      /\_\                    / /\      """.center(width))
    time.sleep(wait)
    print(r"""       /  \ \          /\__ \  \ \ \   / / /       \_\ \           /  \ \    / / /         _         / /  \     """.center(width))
    time.sleep(wait)
    print(r"""      / /\ \ \        / /_ \_\  \ \ \_/ / /        /\__ \         / /\ \ \   \ \ \__      /\_\      / / /\ \__  """.center(width))
    time.sleep(wait)
    print(r"""     / / /\ \_\      / / /\/_/   \ \___/ /        / /_ \ \       / / /\ \_\   \ \___\    / / /     / / /\ \___\ """.center(width))
    time.sleep(wait)
    print(r"""    / /_/_ \/_/     / / /         \ \ \_/        / / /\ \ \     / / /_/ / /    \__  /   / / /      \ \ \ \/___/ """.center(width))
    time.sleep(wait)
    print(r"""   / /____/\       / / /           \ \ \        / / /  \/_/    / / /__\/ /     / / /   / / /        \ \ \       """.center(width))
    time.sleep(wait)
    print(r"""  / /\____\/      / / / ____        \ \ \      / / /          / / /_____/     / / /   / / /     _    \ \ \      """.center(width))
    time.sleep(wait)
    print(r""" / / /______     / /_/_/ ___/\       \ \ \    / / /          / / /\ \ \      / / /___/ / /     /_/\__/ / /      """.center(width))
    time.sleep(wait)
    print(r"""/ / /_______\   /_______/\__\/        \ \_\  /_/ /          / / /  \ \ \    / / /____\/ /      \ \/___/ /       """.center(width))
    time.sleep(wait)
    print(r"""\/__________/   \_______\/             \/_/  \_\/           \/_/    \_\/    \/_________/        \_____\/        """.center(width))
    time.sleep(wait)
    print("\n") # A new line doesn't work with .center :(
    print("Studios".center(width))
    time.sleep(3)
    clear() # Clears the console for the next text