import type { ICoach } from "~/types";
import { api } from "~/api";
import { defineStore } from "pinia";

export const useCoachesStore = defineStore("coaches-store", () => {
  const loading = ref(false);
  const error = ref<string | null>(null);
  const coaches = ref<ICoach[]>([]);
  const activeCategory = ref<string | null>(null);

  const fetchAllCoaches = async () => {
    const { $api } = useNuxtApp();

    try {
      loading.value = true;
      error.value = null;
      const res = await $api<ICoach[]>(api.coaches.list);
      coaches.value = res;
    } catch {
      error.value = "Не удалось загрузить тренеров";
    } finally {
      loading.value = false;
    }
  };

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
    activeCategory,
    fetchAllCoaches,
    filterCoaches,
  };
});
