import json
import subprocess as sp

from rich import print

COMMENT = "Comment"

def get_exif(file_path: str) -> dict:
    """
    获取文件 exif
    """
    cmd = ["exiftool", "-j", file_path]
    return json.loads(sp.check_output(cmd))[0]

def ch_tag(file_path: str, tag: str, value: str):
    """
    修改 exif 某个 tag
    """
    cmd = ["exiftool", f"-{tag}={value}", file_path]
    sp.run(cmd, capture_output=True)

if __name__ == "__main__":
    ch_tag(r"C:\Users\qf\Videos\9分钟HIIT燃脂跟练，中强度每天做3组，暴汗燃脂瘦全身.mp4", COMMENT, "123")
    print(get_exif(r"C:\Users\qf\Videos\9分钟HIIT燃脂跟练，中强度每天做3组，暴汗燃脂瘦全身.mp4"))