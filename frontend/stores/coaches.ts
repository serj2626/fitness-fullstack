import type { ICoach, ICoachesListResponse } from "~/types";
import { useDebounceFn } from "@vueuse/core";
import { api } from "~/api";
import { defineStore } from "pinia";

export const useCoachesStore = defineStore("coaches-store", () => {
  const loading = ref(false);
  const error = ref<string | null>(null);
  const coaches = ref<ICoach[]>([]);
  const activeCategory = ref<string | null>(null);

  const current = ref<number>(1);
  const next = ref<number | null>(null);
  const previous = ref<number | null>(null);
  const count = ref<number>(0);
  const total_pages = ref<number>(0);

  async function fetchAllCoaches(page: number = 1, page_size: number = 6) {
    const { $api } = useNuxtApp();
    loading.value = true;
    try {
      const query: { page: number; page_size: number; category?: string } = {
        page,
        page_size,
      };
      if (activeCategory.value) {
        query.category = activeCategory.value;
      }
      const res = await $api<ICoachesListResponse>(api.coaches.list, {
        query,
      });

      if (res.results) {
        if (page > 1) {
          coaches.value = [...coaches.value, ...res.results];
        } else {
          coaches.value = res.results;
        }
      }

      current.value = page;
      count.value = res.count ?? 0;
      next.value = res.next;
      previous.value = res.previous;
      total_pages.value = res.total_pages;

      return res;
    } catch (e: unknown) {
      error.value = e instanceof Error ? e.message : "Неизвестная ошибка";
      throw e;
    } finally {
      loading.value = false;
    }
  }
  watch(
    () => activeCategory.value,
    useDebounceFn(async () => {
      await fetchAllCoaches(1, 6);
    }, 300),
  );

  function reset() {
    coaches.value = [];
    current.value = 1;
    next.value = null;
    previous.value = null;
    count.value = 0;
    total_pages.value = 0;
    activeCategory.value = null;
  }

  return {
    loading,
    error,
    coaches,
    current,
    next,
    previous,
    count,
    total_pages,

    activeCategory,
    reset,
    fetchAllCoaches, // <- Убедитесь, что метод возвращается!
  };
});

// Тип для использования в компонентах (опционально)
export type CoachesStore = ReturnType<typeof useCoachesStore>;
