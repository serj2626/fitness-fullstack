<script setup lang="ts">
import type { IReview } from '~/types';
const openPhotoViewer = (photos: string[], index: number) => {
  // Здесь можно реализовать открытие полноэкранного просмотрщика
  console.log("Открыть фото:", photos[index]);
};

const props = defineProps<{ sortedReviews: IReview[] }>();
</script>
<template>
  <div v-for="review in sortedReviews" :key="review.id" class="review-card">
    <div class="review-header">
      <div class="review-author">
        <NuxtImg :src="review.avatar" class="review-avatar" alt="Аватар" />
        <div class="author-info">
          <h3 class="author-name">{{ review.name }}</h3>
          <div class="review-date">{{ review.date }}</div>
        </div>
      </div>
      <RatingComponent :rating="review.rating" :size="20" readonly />
    </div>

    <div class="review-content">
      <p class="review-text">{{ review.text }}</p>

      <!-- Фото отзыва -->
      <div v-if="review.photos.length" class="review-photos">
        <NuxtImg
          v-for="(photo, index) in review.photos"
          :key="index"
          :src="photo"
          class="review-photo"
          @click="openPhotoViewer(review.photos, index)"
        />
      </div>
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
