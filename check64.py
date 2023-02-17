import win32file # pip package pywin32; has to be imported this way


def is_64bit(path_to_exe) -> bool:
'''returns True if executable is 64 bit'''
    try:
        return win32file.GetBinaryType(path_to_exe) == 6
    except Exception as e:
        raise e
