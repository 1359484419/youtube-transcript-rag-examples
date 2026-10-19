"""Load YouTube transcripts into LlamaIndex Documents with video metadata."""
import os

from apify_client import ApifyClient
from llama_index.core import Document

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("xiaoliang527/youtube-transcript-rag").call(
    run_input={"videos": ["https://www.youtube.com/watch?v=aircAruvnKk"]}
)
docs = [
    Document(
        text=i["markdown_by_chapter"],
        metadata={"video_id": i["video_id"], "title": i["meta"]["title"], "channel": i["meta"]["channel"]},
    )
    for i in client.dataset(run["defaultDatasetId"]).iterate_items()
    if i["status"] == "ok"
]
print(len(docs), "documents,", sum(len(d.text) for d in docs), "chars")
# next: VectorStoreIndex.from_documents(docs).as_query_engine().query("...")
