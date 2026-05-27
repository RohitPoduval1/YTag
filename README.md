# YTag

YTag is a command-line application to assign tags to songs in a YouTube playlist and play subsets of songs based on those tags.

## Usage
1. Create your CSV with `create_csv_from_playlist.py`
Given a YouTube playlist URL (first command-line arg), it will write the following contents to the specified CSV file (second arg):
- The title of the video
- The URL of the video
- Empty tags

```bash
python "https://youtube.com/playlist\?list=123ABC456DEF" "playlist_name.csv"
```

2. Once you have the CSV file, you can begin tagging using `ytag.py`!
```bash
python ytag.py "playlist_name.csv"
```

3. Finally, play a given playlist using `play_playlist.py` and a tag
```bash
python play_playlist "playlist_name.csv" "your_tag_here"
```

> NOTE: Multi-tag support is in the backlog

## Background 
I primarily listen to music via YouTube (no, I do not use Spotify) due to the variety of classical music recordings available (e.g., artists other than Hilary Hahn or Itzhak Perlman).
There are a variety of types of "Classical Music" such as Baroque, Romantic, and even more granular, Bach, Vivaldi, Beethoven, etc. This same idea applies to Indian music.

I have different music-listening moods, so why not create an app to fill this (what I believe to be) very real need.
