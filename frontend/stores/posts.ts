import type { IPost } from "~/types";
import { api } from "~/api";
import { defineStore } from "pinia";

export const usePostsStore = defineStore("posts", () => {
  const posts = ref<IPost[]>([]);
  const error = ref<string | null>(null);
  const loading = ref(false);
  const activeCategory = ref<string | null>(null);

  const categories = reactive([
    { value: "workout", label: "Тренировки" },
    { value: "nutrition", label: "Питание" },
    { value: "news", label: "Новости клуба" },
    { value: "promo", label: "Акции" },
  ]);

  const selectCategory = (cat: string) => {
    activeCategory.value = activeCategory.value !== cat ? cat : null;
  };

  const filterPosts = computed(() => {
    if (!activeCategory.value) return posts.value;
    return posts.value.filter((post) => post.category === activeCategory.value);
  });

  async function getAllPosts() {
    loading.value = true;
    try {
      const { $api } = useNuxtApp();
      const response = await $api<IPost[]>(api.posts.last);
      posts.value = response;
      error.value = null;
    } catch (e: unknown) {
      error.value = e instanceof Error ? e.message : "Неизвестная ошибка";
    } finally {
      loading.value = false;
    }
  }

  return {
    //state
    posts,
    error,
    loading,
    categories,
    activeCategory,
    //actions
    selectCategory,
    getAllPosts,
    //getter
    filterPosts,
  };
});
