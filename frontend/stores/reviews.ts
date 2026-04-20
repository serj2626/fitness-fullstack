import type { ICoach, IReview } from "~/types";

import { api } from "~/api";

type TSortReview = "newest" | "highest" | "lowest";

export const useReviewsStore = defineStore("reviews", () => {
  const reviews = ref<IReview[]>([]);
  const sortingValue = ref<TSortReview | null>(null);

  const reset = () => {};

  return {
    reviews,
    sortingValue,
    reset,
  };
});
