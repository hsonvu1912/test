from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch("jIS2eB-rGv0")

for entry in transcript:
      print(entry.text)
