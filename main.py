from video_creation import images, background, compile

print("Sigma Male Video Bot")

def main():
    images.download_images()
    background.download_background()
    background.chop_background_video()
    compile.compile_video()

if __name__ == "__main__":
    main()
