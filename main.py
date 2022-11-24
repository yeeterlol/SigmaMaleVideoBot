from video_creation import videos, background, compile

print("Family Guy Video Bot")
print("Creates ASMR slime videos as Family Guy")

def main():
    background.download_background()
    background.chop_background_video()
    videos.download_familyguy()
    videos.chop_background_video()
    compile.compile_video()

if __name__ == "__main__":
    main()
