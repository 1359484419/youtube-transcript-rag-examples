# YouTube Transcript → LLM / RAG examples

Runnable examples for getting YouTube transcripts into **LangChain**, **LlamaIndex**, **MCP clients (Claude, Cursor)**, Python and JavaScript — split by chapter, as Markdown, with token counts.

They use the [YouTube Transcript (RAG-ready)](https://apify.com/xiaoliang527/youtube-transcript-rag) Actor on Apify, so you don't have to deal with YouTube IP blocks, proxies or yt-dlp breakage yourself.

Each video comes back as:

```json
{
  "video_id": "aircAruvnKk",
  "status": "ok",
  "language": "en",
  "token_count": 3817,
  "markdown_by_chapter": "# But what is a neural network?...\n\n## Introduction example\n\n...",
  "segments": [{"start": 0.0, "dur": 4.2, "text": "..."}],
  "meta": {"title": "...", "channel": "3Blue1Brown", "chapters": [{"title": "Introduction example", "start": 0}]}
}
```

Inputs can be video URLs, IDs, playlists or channels (`https://www.youtube.com/@handle`).

## Setup

Get a token at [console.apify.com/settings/integrations](https://console.apify.com/settings/integrations) (the free plan includes monthly credit), then:

```bash
export APIFY_TOKEN=...
pip install -r requirements.txt
```

## Examples

| File | What it does |
|---|---|
| [`python/basic.py`](python/basic.py) | Transcripts for any videos / playlists / channels passed on the command line |
| [`python/langchain_rag.py`](python/langchain_rag.py) | LangChain `Document`s, split into one chunk per video chapter |
| [`python/llamaindex_rag.py`](python/llamaindex_rag.py) | LlamaIndex `Document`s with title / channel metadata |
| [`js/basic.mjs`](js/basic.mjs) | Node.js: latest videos of a channel with token counts |
| [`mcp/mcp.json`](mcp/mcp.json) | Give Claude Desktop, Cursor or any MCP client a YouTube transcript tool |

```bash
python python/basic.py https://www.youtube.com/watch?v=aircAruvnKk
python python/langchain_rag.py
cd js && npm i && node basic.mjs https://www.youtube.com/@3blue1brown
```

### MCP (Claude Desktop, Cursor, …)

Add [`mcp/mcp.json`](mcp/mcp.json) to your client's MCP config with your token, then ask:
*"Summarize the chapters of https://youtu.be/aircAruvnKk"*.

### n8n / Make / Zapier

Apify node → **Run Actor** → `xiaoliang527/youtube-transcript-rag` → **Get dataset items**.

## Why chapter-split Markdown?

Fixed-size chunking cuts a video mid-thought. Splitting on the creator's own chapters keeps each chunk on one topic, and the chapter title becomes useful metadata for retrieval and citations.

## Cost

$0.005 per transcript returned. Videos without captions, private or deleted videos are reported with a status and not charged.

## License

MIT
