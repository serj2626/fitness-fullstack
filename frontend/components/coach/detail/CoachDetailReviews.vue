<script setup lang="ts">
import { ref, computed } from "vue";
import type { IReview, TOrderingReview } from "~/types";
import { useIntersectionObserver } from "@vueuse/core";

defineProps<{
  reviews: IReview[];
  loading: boolean;
  reviewsCount: number;
}>();

const { id } = useRoute().params;

const reviewsStore = useReviewsStore();

const { next, orderingValue } = storeToRefs(reviewsStore);

const scroll = ref(0);

function handleScroll() {
  scroll.value = window.scrollY;
}

const getScrollClass = computed(() => {
  return scroll.value > 70 ? true : false;
});
const observerTarget = ref<HTMLElement | null>(null);

onMounted(() => {
  useIntersectionObserver(
    observerTarget,
    async ([entry]) => {
      if (entry.isIntersecting && next.value && !reviewsStore.loading) {
        await reviewsStore.getAllReviews(next.value as number, 6, id as string);
      }
    },
    {
      threshold: 0.1, // при 10% видимости
      rootMargin: "300px", // дополнительный отступ
    },
  );
});

const sortOptions = [
  { value: "-created_at", label: "Сначала новые" },
  { value: "created_at", label: "Сначала старые" },
  { value: "-rating", label: "Высокий рейтинг" },
  { value: "rating", label: "Низкий рейтинг" },
];

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
<template>
  <div class="coach-detail-reviews">
    <!-- <CoachDetailAlertByLogin /> -->
    <div
      class="coach-detail-reviews__top"
      :class="{ 'coach-detail-reviews__top_scrolled': getScrollClass }"
    >
      <CoachDetailReviewForm />
      <div
        v-if="reviewsCount > 0"
        class="coach-detail-reviews__sorting"
        :class="{ 'coach-detail-reviews__sorting_border': getScrollClass }"
      >
        <button
          v-for="sort in sortOptions"
          :key="sort.value"
          :class="{ active: orderingValue === sort.value }"
          @click="reviewsStore.setOrder(sort.value as TOrderingReview)"
        >
          {{ sort.label }}
        </button>
      </div>
    </div>
    <BaseLoader v-if="loading" />

    <div v-if="reviews.length > 0" class="coach-detail-reviews__list">
      <ReviewCard v-for="review in reviews" :key="review.id" :review="review" />
    </div>
    <BaseEmpty
      v-else
      text="Отзывов нет"
      subtitle="Будьте перым кто оставит отзыв"
    />
    <div
      v-show="next"
      ref="observerTarget"
      class="observer-trigger"
      style="height: 1px; margin-top: 140px"
    />
  </div>
</template>
<style lang="scss">
.coach-detail-reviews {
  padding: 20px;
  background-color: $bg_block;
  border-radius: 12px;
  position: relative;
  &__top {
    position: sticky;
    top: 75px;
    z-index: 10;
    transition: all 0.5s ease-in;
    &_scrolled {
      background-color: $bg;
      padding: 10px 15px;
      border-radius: 12px;
    }
  }
  &__sorting {
    display: flex;
    gap: 15px;
    margin-bottom: 20px;
    padding-bottom: 15px;
    border-bottom: 1px solid rgba($white, 0.1);
    transition: all 0.5s ease-in;

    &_border {
      border-color: transparent;
      padding-bottom: 0;
    }

    button {
      background: none;
      border: none;
      color: rgba($white, 0.7);
      font-size: 14px;
      cursor: pointer;
      padding: 5px 10px;
      border-radius: 6px;
      transition: all 0.3s;

      &.active {
        background: rgba($accent, 0.2);
        color: $accent;
      }

      &:hover:not(.active) {
        color: $white;
      }
    }
  }
  &__list {
    display: flex;
    flex-direction: column;
    gap: 25px;
  }
}
.load-more {
  margin-top: 30px;
  width: 100%;
}
</style>
