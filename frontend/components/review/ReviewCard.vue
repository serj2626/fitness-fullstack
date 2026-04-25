<script setup lang="ts">
import type { IReview } from "~/types";

defineProps<{ review: IReview }>();
</script>
<template>
  <div class="review-card">
    <div class="review-card__header">
      <div class="review-card__header-author">
        <div class="review-card__header-author-info">
          <h3 class="review-card__header-author-info-name">
            {{ review?.user || "Аноним" }}
          </h3>
          <div class="review-card__header-author-info-date">
            {{ review.time_ago || "" }}
          </div>
        </div>
      </div>
      <RatingComponent :model-value="review?.rating" />
    </div>

    <div class="review-card__content">
      <p class="review-card__content-text">{{ review?.text || "" }}</p>
    </div>
  </div>
</template>
<style scoped lang="scss">
.review-card {
  background: rgba($white, 0.05);
  border-radius: 12px;
  padding: 20px;
  transition: transform 0.3s;

  &:hover {
    transform: translateY(-3px);
  }
  &__header {
    display: flex;
    justify-content: space-between;
    align-items: start;
    margin-bottom: 15px;
    &-author {
      display: flex;
      align-items: center;
      gap: 15px;
      &-info {
        display: flex;
        flex-direction: column;
        &-name {
          font-size: 16px;
          font-weight: 600;
          color: $white;
          margin-bottom: 3px;
        }
        &-date {
          font-size: 14px;
          color: rgba($white, 0.6);
        }
      }
    }
  }
  &__content {
    padding-left: 5px;
    &-text {
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
  }
}
</style>
