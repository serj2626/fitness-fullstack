<script setup lang="ts">
import { ref, computed } from "vue";
import { useModalsStore } from "~/stores/modals";
import type { IReview, TOrderingReview } from "~/types";
import { useIntersectionObserver } from "@vueuse/core";

defineProps<{
  reviews: IReview[];
  loading: boolean;
  reviewsCount: number;
}>();

const { id } = useRoute().params;

const modalsStore = useModalsStore();
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
    <div
      class="coach-detail-reviews__top"
      :class="{ 'coach-detail-reviews__top_scrolled': getScrollClass }"
    >
      <div class="coach-detail-reviews__header">
        <h2 class="coach-detail-reviews__header-title">
          Отзывы
          <span class="coach-detail-reviews__header-count">
            {{ reviewsCount }}
          </span>
        </h2>
        <BaseButton
          label="Оставить отзыв"
          size="md"
          color="#1a8f1a"
          style="color: white"
          @click="modalsStore.openModal('reviewCoachForm')"
        />
      </div>
      <div
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
      <div v-for="review in reviews" :key="review.id" class="review-card">
        <div class="review-header">
          <div class="review-author">
            <div class="author-info">
              <h3 class="author-name">
                {{ review?.user || "Аноним" }}
              </h3>
              <div class="review-date">{{ review.time_ago || "" }}</div>
            </div>
          </div>
          <RatingComponent :model-value="review?.rating" />
        </div>

        <div class="review-content">
          <p class="review-text">{{ review?.text || "" }}</p>
        </div>
      </div>
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

  &:deep(.p-editor-container) {
    border-radius: 10px;
    border: 1px solid rgba(255, 255, 255, 0.1);
    background-color: rgba(255, 255, 255, 0.03);
    overflow: hidden;

    .p-editor-toolbar {
      background-color: rgba(255, 255, 255, 0.05);
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);

      button {
        color: white;
        &:hover {
          background-color: rgba(
            26,
            143,
            26,
            0.2
          ); // можно заменить на переменную
        }
      }
    }

    .p-editor-content {
      background-color: transparent;
      color: white;
      min-height: 200px;
      padding: 16px;

      p {
        margin: 0 0 10px;
      }

      strong {
        color: #1a8f1a;
      }
    }
  }

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
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 25px;
    &-title {
      font-size: 24px;
      font-weight: 700;
      color: $white;
      display: flex;
      align-items: center;
      gap: 10px;
    }
    &-count {
      font-size: 16px;
      font-weight: 400;
      color: rgba($white, 0.7);
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

.review-card {
  background: rgba($white, 0.05);
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.3s;

  &:hover {
    transform: translateY(-3px);
  }
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: start;
  margin-bottom: 15px;
}

.review-author {
  display: flex;
  align-items: center;
  gap: 15px;
}

.review-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid $accent;
}

.author-info {
  display: flex;
  flex-direction: column;
}

.author-name {
  font-size: 16px;
  font-weight: 600;
  color: $white;
  margin-bottom: 3px;
}

.review-date {
  font-size: 14px;
  color: rgba($white, 0.6);
}

.review-content {
  padding-left: 5px;
}

.review-text {
  font-size: 14px;
  line-height: 1.6;
  color: rgba($white, 0.9);
  margin-bottom: 15px;
  text-indent: 20px;
  letter-spacing: 0.8px;

  &:first-letter {
    text-transform: uppercase;
    color: $accent;
    font-size: 22px;
    font-weight: 600;
    margin-right: 1px;
  }
}

.review-photo {
  width: 80px;
  height: 80px;
  border-radius: 8px;
  object-fit: cover;
  cursor: pointer;
  transition: transform 0.3s;

  &:hover {
    transform: scale(1.05);
  }
}

.load-more {
  margin-top: 30px;
  width: 100%;
}
</style>
