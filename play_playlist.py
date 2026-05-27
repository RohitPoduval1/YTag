import sys
import subprocess
import csv

if __name__ == "__main__":
    # python play_playlist.py playlist_csv_path tag_of_interest
    playlist_csv_path = sys.argv[1]
    tag_of_interest = sys.argv[2]

    with open(playlist_csv_path) as f:
        csv_reader = csv.reader(f)
        ids = [id for (_, id, tags) in csv_reader if tag_of_interest in tags]

    urls = [f"https://youtu.be/{id}" for id in ids]

    command = "mpv --no-video --script-opts=ytdl_hook-ytdl_path=yt-dlp --ytdl-format=bestaudio".split(" ")
    command.extend(urls)
    subprocess.run(command)
