// import type { ICoach, IReview } from "~/types";

import type { ICoach, IReview } from "~/types";

import { api } from "~/api";

// import { api } from "~/api";

// export const useTrainerStore = defineStore("trainer", () => {
//   const trainer = ref<ICoach | null>(null);
//   const reviews = ref<IReview[]>([]);
//   const loading = ref(false);
//   const error = ref<string | null>(null);

//   const fetchTrainerWithReviews = async (id: string | number) => {
//     const { $api } = useNuxtApp();
//     loading.value = true;
//     error.value = null;

//     try {
//       const [coach, comments] = await Promise.all([
//         $api(api.coaches.detail(String(id))) as Promise<ICoach>,
//         $api(api.coaches.reviews(String(id))) as Promise<IReview[]>,
//       ]);

//       trainer.value = coach;
//       reviews.value = comments;
//     } catch (err) {
//       error.value = extractError(err);
//     } finally {
//       loading.value = false;
//     }
//   };

//   const addReview = async (reviewData: { text: string; rating: number }) => {
//     const { $api } = useNuxtApp();
//     if (!trainer.value) return;

//     try {
//       const newReview = await $api<IReview>(
//         api.coaches.reviewsCreate(trainer.value.id),
//         {
//           method: "POST",
//           body: {
//             trainer: trainer.value.id,
//             ...reviewData,
//           },
//         }
//       );
//       reviews.value.unshift(newReview);
//     } catch (err) {
//       error.value = extractError(err);
//     }
//   };

//   const updateReview = async (
//     id: string,
//     reviewData: { text: string; rating: number }
//   ) => {
//     const { $api } = useNuxtApp();
//     try {
//       const updated = await $api<IReview>(`${api.reviews.update}${id}/`, {
//         method: "PUT",
//         body: reviewData,
//       });

//       const index = reviews.value.findIndex((r) => r.id === id);
//       if (index !== -1) reviews.value[index] = updated;
//     } catch (err) {
//       error.value = extractError(err);
//     }
//   };

//   const reset = () => {
//     trainer.value = null;
//     reviews.value = [];
//     error.value = null;
//     loading.value = false;
//   };

//   return {
//     trainer,
//     reviews,
//     loading,
//     error,
//     fetchTrainerWithReviews,
//     addReview,
//     updateReview,
//     reset,
//   };
// });

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
