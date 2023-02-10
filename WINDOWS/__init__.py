import platform
import ctypes

def enable_virtual_terminal_processing():
    if platform.system() != 'Windows':
        return

    stdout_handle = ctypes.windll.kernel32.GetStdHandle(-11)
    stderr_handle = ctypes.windll.kernel32.GetStdHandle(-12)

    mode = ctypes.c_uint32()
    ctypes.windll.kernel32.GetConsoleMode(stdout_handle, ctypes.byref(mode))
    mode.value = mode.value | 0x4
    ctypes.windll.kernel32.SetConsoleMode(stdout_handle, mode)

    ctypes.windll.kernel32.GetConsoleMode(stderr_handle, ctypes.byref(mode))
    mode.value = mode.value | 0x4
    ctypes.windll.kernel32.SetConsoleMode(stderr_handle, mode)

def __init__():
    if platform.system() == 'Windows':
        enable_virtual_terminal_processing()

