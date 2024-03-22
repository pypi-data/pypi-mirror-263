"""
函数

concat_video：合并视频

———————————

类 FFprobe

duration：获取视频时长

codec：获取视频编码

size：获取视频大小
"""

import json
import subprocess as sp
from pathlib import Path

from moviepy.editor import VideoFileClip, concatenate_videoclips


def concat_video(files: list[str], output_file: str):
    """
    合并视频

    后处理：删除原视频

    注意：只使用 CPU，合并大量视频很慢
    """
    clips = [VideoFileClip(f) for f in files]
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file)
    for f in files:
        f.unlink()


class MetadataParsedError(OSError):
    """
    metadata 解析错误
    """

    pass


class FFprobe:
    """
    方法

    duration：获取视频时长

    codec：获取视频编码

    size：获取视频大小
    """
    def __init__(self, file: str):
        self.metadata = self.__ffprobe(file)
        if not self.metadata:
            raise MetadataParsedError(file)

    def __repr__(self):
        return str(self.metadata)

    def __ffprobe(self, file: str) -> dict:
        """
        获取视频 metadata
        """
        cmd = f'ffprobe -print_format json -show_format -show_streams -v quiet "{file}"'
        output = sp.check_output(cmd, shell=True)
        return json.loads(output)

    def duration(self) -> str:
        return self.metadata["format"]["duration"]

    def codec_name(self) -> str:
        return self.metadata["streams"][0]["codec_name"]

    def size(self) -> str:
        return self.metadata["format"]["size"]

def is_hevc(file: Path) -> bool:
    """
    编码为 hevc 返回 True
    """
    return True if FFprobe(file).codec_name() == "hevc" else False

def is_not_hevc(file: Path) -> bool:
    """
    编码不是 hevc 返回 True
    """
    return True if FFprobe(file).codec_name() != "hevc" else False


if __name__ == "__main__":
    print(
        FFprobe(
            r"C:\Users\qf\Videos\大明王朝\大明王朝-03.mp4"
        )
    )
