"""Fetch transcripts for a video, playlist or channel and print a summary line per video."""
import os
import sys

from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("xiaoliang527/youtube-transcript-rag").call(
    run_input={"videos": sys.argv[1:] or ["https://www.youtube.com/watch?v=aircAruvnKk"], "languages": ["en"]}
)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    if item["status"] == "ok":
        print(f'{item["video_id"]}  {item["token_count"]:>6} tokens  {item["meta"]["title"]}')
    else:
        print(f'{item["video_id"]}  {item["status"]} (not charged)')
