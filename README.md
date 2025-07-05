# yt-dlp-local-bulk-converter
Reads a list of YouTube URLs and converts all to MP3

# Prerequisites

This script is intended to be ran on Windows, but should work on Linux and macOS as well.

The following programs should be installed and on your system's `PATH` variable so they're callable from anywhere:

* [Python](https://www.python.org/downloads/)
* [yt-dlp](https://github.com/yt-dlp/yt-dlp/releases)
* [ffmpeg](https://ffmpeg.org/download.html)

# Usage

Create a file named `links.txt` in this repository (so it sits alongside `main.py`) and populate it with links to videos, one per line.

This script doesn't use any third-party Python libraries, so you can run the script with the following command:

```
python main.py
```

Videos are downloaded to the current user's Downloads folder.

A batch file is provided for quick runs on a Windows machine.
