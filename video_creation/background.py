from pathlib import Path
from random import randrange
from typing import Any, Tuple
from utils.CONSTANTS import URL
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from pytube import YouTube
from pytube.cli import on_progress

def get_start_and_end_times(video_length: int, length_of_clip: int) -> Tuple[int, int]:
    """Generates a random interval of time to be used as the background of the video.
    Args:
        video_length (int): Length of the video
        length_of_clip (int): Length of the video to be used as the background
    Returns:
        tuple[int,int]: Start and end time of the randomized interval
    """
    random_time = randrange(180, int(length_of_clip) - int(video_length))
    return random_time, random_time + video_length

def download_background():
    """ Downloads the stock footage needed for the video """
    Path("./assets/background/").mkdir(parents=True, exist_ok=True)
    if Path("assets/background/video.mp4").is_file():
        return
    print("We are downloading the stock footage needed!")
    print("This may take a while, please be patient.")
    print("While you wait, go get yourself a coffee!")
    YouTube(URL, on_progress_callback=on_progress).streams.filter(res="1080p").first().download(
        "assets/background", filename="video.mp4"
    )
    print("Background video downloaded successfully!")

def chop_background_video():
    """
    Generates the background footage to be used in the video
    """
    background = VideoFileClip(f"assets/background/video.mp4")
    start_time, end_time = get_start_and_end_times(15, background.duration)
    try:
        ffmpeg_extract_subclip(
            f"assets/background/video.mp4",
            start_time,
            end_time,
            targetname=f"assets/temp/background.mp4",
        )
    except (OSError, IOError):  # ffmpeg issue see #348
        print("FFMPEG issue. Trying again...")
        with VideoFileClip(f"assets/background/video.mp4") as video:
            new = video.subclip(start_time, end_time)
            new.write_videofile(f"assets/temp/background.mp4")
    print("Background video chopped successfully!")

