import subprocess
from pathlib import Path

LINKS_FILE = Path(Path(__file__).parent, "links.txt")
CMD_ARGS = "--extract-audio --audio-format mp3 -o ~/Downloads/%(title)s_%(id)s.%(ext)s --no-check-certificate --no-playlist"

if not LINKS_FILE.is_file():
    print("Couldn't find links.txt, creating....")
    LINKS_FILE.touch()
    print(
        "Open this file in your text editor of choice and populate it with links (one per line).\nExiting...."
    )
    exit(0)

if __name__ == "__main__":
    with open(LINKS_FILE) as infile:
        for i, line in enumerate(infile.readlines(), start=1):
            link = line.strip()
            if link:
                one_command = f"yt-dlp {link} {CMD_ARGS}"
                print(f"Link #{i}:\n\t{one_command}")
                try:
                    subprocess.call(one_command)
                except Exception as e:
                    print(e)
                    print("Encountered an error, skipping....")
                print()
    print("Done!")
