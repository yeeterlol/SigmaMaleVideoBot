from moviepy.editor import *
from pathlib import Path
from utils import cleanup
import random

def compile_video():
    ran = random.choice(os.listdir("./assets/temp/png/"))
    generate = random.randint(1, 999999)
    # Clip
    clip = VideoFileClip(f"./assets/temp/background.mp4").subclip(0, 15).without_audio().resize(height=1920).crop(
        x1=1166.6, y1=0, x2=2246.6, y2=1920)
    image = ImageClip(f"./assets/temp/png/{ran}").set_pos("center").resize(height=800).set_duration(15)

    combined = CompositeVideoClip([clip, image])
    Path("./results").mkdir(parents=True, exist_ok=True)
    combined.write_videofile(f"./results/video_{generate}.mp4")
    cleanup.cleanup()
