import instaloader
import os
from pathlib import Path

def download_images():
    """
    Downloading random images from Instagram
    for the video to be generated
    """
    print("Downloading images from Instagram")
    Path("./assets/temp/png/").mkdir(parents=True, exist_ok=True)
    account = "sigma_male_daily"
    count = 0

    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=False,
        download_video_thumbnails=False,
        compress_json=False,
        download_geotags=False,
        post_metadata_txt_pattern=None,
        max_connection_attempts=0,
        download_comments=False,
        save_metadata=False,
        dirname_pattern="./assets/temp/png"
    )

    posts = instaloader.Profile.from_username(L.context, account).get_posts()
    for post in posts:
        if count == 15:
            dir_name = "./assets/temp/png"
            test = os.listdir(dir_name)
            for item in test:
                if item.endswith(".txt"):
                    os.remove(os.path.join(dir_name, item))
            return
        count += 1
        print(f"Downloaded {count} posts")
        L.download_post(post, account)
