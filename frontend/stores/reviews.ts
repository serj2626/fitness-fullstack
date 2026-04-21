import type {
  ICreateReview,
  IReview,
  IReviewResponse,
  TOrderingReview,
} from "~/types";
import { useDebounceFn } from "@vueuse/core";

import { api } from "~/api";

export const useReviewsStore = defineStore("reviews", () => {
  const reviews = ref<IReview[]>([]);
  const orderingValue = ref<TOrderingReview | null>(null);

  const current = ref<number>(1);
  const next = ref<number | null>(null);
  const previous = ref<number | null>(null);
  const count = ref<number>(0);
  const total_pages = ref<number>(0);
  const loading = ref<boolean>(false);
  const error = ref<string | null>(null);

  async function getAllReviews(
    page: number = 1,
    page_size: number = 6,
    id?: string,
  ) {
    const { $api } = useNuxtApp();
    loading.value = true;
    error.value = null;

    try {
      const query: {
        id?: string;
        page: number;
        page_size: number;
        ordering?: string;
      } = {
        id,
        page,
        page_size,
      };

      if (orderingValue.value) {
        query.ordering = orderingValue.value;
      }

      const res = await $api<IReviewResponse>(api.reviews.list, { query });

      if (res.results) {
        if (page === 1) {
          reviews.value = res.results;
        } else {
          reviews.value = [...reviews.value, ...res.results];
        }
      }

      current.value = res.current;
      next.value = res.next;
      previous.value = res.previous;
      count.value = res.count ?? 0;
      total_pages.value = res.total_pages;

      return res;
    } catch {
      error.value = "Произошла ошибка при загрузке постов";
    } finally {
      loading.value = false;
    }
  }

  async function createNewReview(review: ICreateReview) {
    const { $api } = useNuxtApp();
    loading.value = true;
    error.value = null;

    try {
      const res = await $api<ICreateReview>(api.reviews.create, {
        method: "POST",
        body: review,
      });

      return res;
    } catch (e: unknown) {
      console.log("e", e);
      error.value = "Произошла ошибка при создании отзыва";
    } finally {
      console.log("asdasd");
      loading.value = false;
    }
  }

  const setOrder = (newType: TOrderingReview) => {
    orderingValue.value = orderingValue.value === newType ? null : newType;
  };
  const reset = () => {
    reviews.value = [];
    current.value = 1;
    next.value = null;
    previous.value = null;
    count.value = 0;
    total_pages.value = 0;
    orderingValue.value = null;
  };

  watch(
    () => orderingValue.value,
    useDebounceFn(async () => {
      await getAllReviews(1, 6);
    }, 500),
  );

  return {
    reviews,
    orderingValue,
    loading,
    error,
    current,
    next,
    previous,
    count,
    total_pages,
    reset,
    getAllReviews,
    setOrder,
    createNewReview,
  };
});
