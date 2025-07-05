import { api } from "~/api";
import { defineStore } from "pinia";

export const usePostsStore = defineStore("posts", () => {
  const posts = ref<IPost[]>([]);

  return {
    posts,
  };
});
