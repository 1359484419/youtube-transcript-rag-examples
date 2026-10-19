// Fetch the latest videos of a channel and print token counts.
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('xiaoliang527/youtube-transcript-rag').call({
  videos: [process.argv[2] ?? 'https://www.youtube.com/@3blue1brown'],
  maxPerSource: 3,
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
for (const i of items) console.log(i.video_id, i.status, i.token_count ?? '', i.meta?.title ?? '');
