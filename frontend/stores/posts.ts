import { defineStore } from "pinia";
import { api } from "~/api";
import type { IPost, IPostsResponse } from "~/types";
import { useDebounceFn } from "@vueuse/core";

export const usePostsStore = defineStore("posts", () => {
  const current = ref<number>(1);
  const next = ref<number | null>(null);
  const previous = ref<number | null>(null);
  const count = ref<number>(0);
  const total_pages = ref<number>(0);
  const type = ref<"article" | "news" | null>(null);
  const posts = ref<IPost[]>([]);
  const loadingPosts = ref<boolean>(false);
  const errorPosts = ref<string | null>(null);

  async function getAllPosts(page: number = 1, page_size: number = 6) {
    const { $api } = useNuxtApp();
    loadingPosts.value = true;
    errorPosts.value = null;

    try {
      const query: { page: number; page_size: number; type?: string } = {
        page,
        page_size,
      };

      if (type.value) {
        query.type = type.value;
      }

      const res = await $api<IPostsResponse>(api.posts.list, { query });

      if (res.results) {
        if (page === 1) {
          posts.value = res.results;
        } else {
          posts.value = [...posts.value, ...res.results];
        }
      }

      current.value = res.current;
      next.value = res.next;
      previous.value = res.previous;
      count.value = res.count ?? 0;
      total_pages.value = res.total_pages;

      return res;
    } catch {
      errorPosts.value = "Произошла ошибка при загрузке постов";
    } finally {
      loadingPosts.value = false;
    }
  }

  const changeType = (newType: "article" | "news") => {
    type.value = type.value === newType ? null : newType;
  };


  watch(
    () => type.value,
    useDebounceFn(async () => {
      await getAllPosts(1, 6);
    }, 500),
  );

  function reset() {
    posts.value = [];
    current.value = 1;
    next.value = null;
    previous.value = null;
    count.value = 0;
    total_pages.value = 0;
    type.value = null;
  }

  return {
    posts,
    current,
    next,
    previous,
    count,
    type,
    total_pages,
    loadingPosts,
    errorPosts,
    getAllPosts,
    changeType,
    reset,
  };
});
