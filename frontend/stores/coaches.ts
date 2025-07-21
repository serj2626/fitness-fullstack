import type { ICoach, ICoachesListResponse } from "~/types";

import { api } from "~/api";
import { defineStore } from "pinia";

export const useCoachesStore = defineStore("coaches-store", () => {
  const loading = ref(false);
  const error = ref<string | null>(null);
  const coaches = ref<ICoach[]>([]);
  const activeCategory = ref<string | null>(null);

  const current = ref<number>(1);
  const next = ref<number | null>(2);
  const previous = ref<number | null>(null);
  const count = ref<number>(19);
  const total_pages = ref<number>(4);

  async function fetchAllCoaches(page: number = 1, page_size: number = 6) {
    const { $api } = useNuxtApp();
    loading.value = true;
    try {
      const res = await $api<ICoachesListResponse>(api.coaches.list, {
        query: {
          page,
          page_size,
        },
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

  const filterCoaches = computed(() => {
    if (!activeCategory.value) return coaches.value;
    return coaches.value.filter(
      (coach) => coach.position === activeCategory.value
    );
  });

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
    filterCoaches,
    fetchAllCoaches, // <- Убедитесь, что метод возвращается!
  };
});

// Тип для использования в компонентах (опционально)
export type CoachesStore = ReturnType<typeof useCoachesStore>;