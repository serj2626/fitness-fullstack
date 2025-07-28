import type { ICoach, IReview } from "~/types";

import { api } from "~/api";

export const useTrainerStore = defineStore("trainer", () => {
  const trainer = ref<ICoach | null>(null);
  const reviews = ref<IReview[]>([]);
  const loadingTrainer = ref(false);
  const loadingReviews = ref(false);
  const error = ref<string | null>(null);

  const fetchTrainer = async (id: string) => {
    const { $api } = useNuxtApp();
    loadingTrainer.value = true;
    error.value = null;

    try {
      const res = await $api(api.coaches.detail(id));
      trainer.value = res as ICoach;
      return res;
    } catch (err) {
      error.value = extractError(err);
    } finally {
      loadingTrainer.value = false;
    }
  };

  const fetchReviews = async (id: string) => {
    const { $api } = useNuxtApp();
    loadingReviews.value = true;
    error.value = null;

    try {
      reviews.value = await $api(api.coaches.reviews(id));
    } catch (err) {
      error.value = extractError(err);
    } finally {
      loadingReviews.value = false;
    }
  };

  const reset = () => {
    trainer.value = null;
    reviews.value = [];
    error.value = null;
    loadingTrainer.value = false;
    loadingReviews.value = false;
  };

  return {
    trainer,
    reviews,
    loadingTrainer,
    loadingReviews,
    error,
    fetchTrainer,
    fetchReviews,
    reset,
  };
});
