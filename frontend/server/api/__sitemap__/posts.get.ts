import type { IPost } from "~/types";
import type { SitemapUrlInput } from "#sitemap/types";
import { api } from "~/api";

const cache: {
  data: SitemapUrlInput[] | null;
  timestamp: number;
  ttl: number;
} = {
  data: null,
  timestamp: 0,
  ttl: 1000 * 60 * 15,
};

export default defineEventHandler(async () => {
  const now = Date.now();

  if (cache.data && now - cache.timestamp < cache.ttl) {
    return cache.data;
  }

  const config = useRuntimeConfig();
  const posts = await $fetch<IPost[]>(
    `${config.public.api_url}${api.posts.list}`
  );

  cache.data = posts.map((post) => ({
    loc: `/posts/${post.slug}`,
    priority: 0.8,
    changefreq: "weekly",
    lastmod: post.updated_at
      ? new Date(post.updated_at).toISOString()
      : undefined,
    _sitemap: "posts",
  }));

  cache.timestamp = now;

  return cache.data;
});
