import type { ICoachesListResponse } from "~/types";
import type { SitemapUrlInput } from "#sitemap/types";
import { api } from "~/api";
import { defineSitemapEventHandler } from "#imports";

export default defineSitemapEventHandler(async () => {
  const config = useRuntimeConfig();
  const res = await $fetch<ICoachesListResponse>(
    `${config.public.api_url}${api.coaches.list}`
  );

  const sitemapUrls: SitemapUrlInput[] = res.results.map((coach) => {
    return {
      loc: `/coaches/${coach.id}`,
      _sitemap: "coaches",
      priority: 0.9,
      changefreq: "weekly",
    };
  });

  return sitemapUrls;
});
