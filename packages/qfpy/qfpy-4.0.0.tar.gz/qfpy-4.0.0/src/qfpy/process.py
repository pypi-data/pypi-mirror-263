import psutil


def exist(process_name: str) -> bool:
    """
    检查进程是否存在
    """
    if not process_name.endswith(".exe"):
        process_name += ".exe"
    for p in psutil.process_iter():
        if process_name in p.name().lower():
            return True
    return False


if __name__ == "__main__":
    print(exist("edge"))