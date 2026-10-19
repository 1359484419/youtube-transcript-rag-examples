"""Load YouTube transcripts into LangChain Documents, one Document per chapter."""
import os

from apify_client import ApifyClient
from langchain_apify import ApifyDatasetLoader
from langchain_core.documents import Document
from langchain_text_splitters import MarkdownHeaderTextSplitter

token = os.environ["APIFY_TOKEN"]
run = ApifyClient(token).actor("xiaoliang527/youtube-transcript-rag").call(
    run_input={"videos": ["https://www.youtube.com/watch?v=aircAruvnKk"]}
)
docs = ApifyDatasetLoader(
    dataset_id=run["defaultDatasetId"],
    apify_token=token,
    dataset_mapping_function=lambda i: Document(
        page_content=i.get("markdown_by_chapter") or "",
        metadata={"video_id": i["video_id"], "title": (i.get("meta") or {}).get("title")},
    ),
).load()

splitter = MarkdownHeaderTextSplitter([("#", "title"), ("##", "chapter")])
chunks = [c for d in docs for c in splitter.split_text(d.page_content)]
for c in chunks:
    print(c.metadata.get("chapter"), "-", len(c.page_content), "chars")
# next: vector_store.add_documents(chunks)
