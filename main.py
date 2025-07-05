import subprocess
from pathlib import Path

LINKS_FILE = Path(Path(__file__).parent, "links.txt")
CMD_BASE = "yt-dlp --extract-audio --audio-format mp3 -o 'C:\\Users\\%username%\\Downloads\\%(title)s %(id)s.%(ext)s' --no-check-certificate --no-playlist"

if __name__ == "__main__":
    with open(LINKS_FILE) as infile:
        for line in infile.readlines():
            link = line.strip()
            if link:
                one_command = f"{CMD_BASE} {link}"
                print(one_command)
                # subprocess.call(one_command)
