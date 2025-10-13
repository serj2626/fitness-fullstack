import type { IAbonementResponse } from "~/types";
import { api } from "~/api";
import { defineStore } from "pinia";

export const useAbonementsStore = defineStore("abonements", () => {
  const abonements = ref<IAbonementResponse[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);

  const getAllAbonements = async () => {
    if (abonements.value.length) return abonements.value;

    const { $api } = useNuxtApp();
    try {
      loading.value = true;
      const res = await $api<IAbonementResponse[]>(api.abonements.list);
      abonements.value = res;
      error.value = null;
      return res;
    } catch (e: unknown) {
      error.value = extractError(e);
      throw e;
    } finally {
      loading.value = false;
    }
  };

  return {
    abonements,
    loading,
    error,
    getAllAbonements,
  };
});
