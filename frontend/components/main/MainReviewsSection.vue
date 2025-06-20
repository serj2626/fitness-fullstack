<script lang="ts" setup>
import { reviews } from "~/assets/data/moke.data";
</script>
<template>
  <section id="main-reviews-section" class="main-reviews-section">
    <BaseSwiper :auto-delay="5000">
      <swiper-slide v-for="(review, idx) in reviews" :key="idx" class="slide">
        <ReviewComponent :review />
      </swiper-slide>
    </BaseSwiper>
  </section>
</template>
<style lang="scss" scoped>
// .swiper-pagination {
//   position: absolute;
//   bottom: 20px; /* Отступ снизу */
//   left: 0;
//   width: 100%;
//   height: 5px; /* Высота прогресс-бара */
//   background-color: rgba(0, 0, 0, 0.3); /* Цвет фона */
//   border-radius: 10px; /* Радиус скругления */
// }

// .swiper-pagination-progressbar {
//   background-color: #ffcc00;
//   height: 100%;
//   transition: width 0.3s ease-in-out; /* Плавное изменение ширины */
// }
.swiper-button-prev,
.swiper-button-next {
  // position: absolute;
  // top: 50%;
  // transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: none;
  padding: 10px;
  color: #fff;
  font-size: 24px;
  z-index: 10;
  border-radius: 5%;
}

.swiper-button-prev {
}

.swiper-button-next {
}

.main-reviews-section {
  padding: 100px 30px;
}
.review {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: $white;
  border-radius: 5px;
  gap: 10px;
  &__header {
    position: relative;
    margin: 0;
    border-bottom: 1px solid transparent;
    display: flex;
    align-items: start;
    justify-content: space-between;
    padding: 1.5em 22px 0.8em;
    &-author {
      flex-grow: 1;
      display: flex;
      flex-direction: column;
      margin-left: 10px;
      &-date {
        display: flex;
        align-items: center;
        gap: 10px;
        color: #787878;
        font-size: 15px;
        font-weight: 500;
        opacity: 0.8;
      }
    }
    &-rating {
      &:deep(.iconify) {
        background-color: $accent !important;
      }
    }
  }
  &__body {
    padding: 0 22px;
    height: 100px;
    overflow: auto;
    flex-grow: 1;
    &-text {
      @include text_overflow(3);
    }
  }
  &__footer {
    display: flex;
    background: #f0efef;
    border-top: 1px solid #e6e6e6;
    padding: 0.8em 22px;
    &-company {
      display: flex;
      align-items: center;
      gap: 10px;

      &-icon {
        color: #787878;
        font-size: 26px;
        font-weight: 600;
      }
      &-name {
        color: #635757;
        &-sub {
          font-size: 15px;
          text-transform: lowercase;
          font-weight: 500;
          opacity: 0.8;
        }
      }
    }
  }
}
</style>
