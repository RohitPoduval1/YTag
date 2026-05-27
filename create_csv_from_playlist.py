"""Create a YTag compatible CSV from a raw YouTube playlist URL"""
import csv
import json
import re
import sys

import yt_dlp

if __name__ == "__main__":
    ydl_opts = {
        'extract_flat': True, 
        'quiet': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Fetching playlist data. This may take a moment...")
        raw_playlist_url = sys.argv[1]
        match = re.match(r"((?:https://)?.+/)(.+)", raw_playlist_url)
        if not match:
            raise Exception("Regex failed")
        playlist_id = match.group(2)
        playlist_id = playlist_id.replace("\\", "")
        cleaned_playlist_url = match.group(1) + playlist_id

        info_dict = ydl.extract_info(cleaned_playlist_url, download=False)

        entries = info_dict.get('entries', [])

        csv_filename = sys.argv[2]

        # Open a new CSV file to write the data
        with open(csv_filename, mode='w+', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)

            # Loop through the playlist and write each video's title and URL
            for entry in entries:
                # yt-dlp flat extraction usually returns just the url, title, and id
                url = entry.get('url')
                title = entry.get('title')
                if re.match(r"\[\w+ video\]", title):
                    continue

                writer.writerow([title.strip(), url, ""])

    print(f"Success! {len(entries)} videos saved to {csv_filename}.")
