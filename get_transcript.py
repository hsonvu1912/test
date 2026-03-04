import subprocess
import json
import sys

video_url = "https://www.youtube.com/watch?v=jIS2eB-rGv0"

# Use yt-dlp to get subtitles
result = subprocess.run(
    ["yt-dlp", "--write-auto-sub", "--sub-lang", "en", "--skip-download", "--sub-format", "json3", "-o", "transcript", video_url],
    capture_output=True, text=True
)

print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)

# Try to read the subtitle file
import glob
sub_files = glob.glob("transcript*.json3") + glob.glob("transcript*.vtt") + glob.glob("transcript*.en.*")
print("Found subtitle files:", sub_files)

for f in sub_files:
    with open(f, "r", encoding="utf-8") as fh:
        content = fh.read()
        # If JSON3 format, parse it
        if f.endswith(".json3"):
            data = json.loads(content)
            for event in data.get("events", []):
                segs = event.get("segs", [])
                text = "".join(s.get("utf8", "") for s in segs).strip()
                if text:
                    print(text)
        else:
            print(content)
