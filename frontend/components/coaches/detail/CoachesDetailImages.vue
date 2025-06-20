<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Mousewheel, Zoom, Pagination } from "swiper/modules";

const { startIndex, images = [] } = defineProps<{
  startIndex: number;
  images?: string[];
}>();

const currentSlide = ref(startIndex);

const onSlideChange = (swiper: any) => {
  currentSlide.value = swiper.realIndex;
};
</script>

<template>
  <div class="coaches-detail-images">
    <BaseButtonClose
      :size="40"
      top="20px"
      right="20px"
      color="#fff"
      @click="$emit('close')"
    />
    <Swiper
      :loop="true"
      :pagination="{ el: '.swiper-pagination', clickable: true }"
      :modules="[Mousewheel, Zoom, Pagination]"
      :initial-slide="startIndex"
      :mousewheel="true"
      :zoom="true"
      :slides-per-view="1"
      class="swiper-container"
      @slide-change="onSlideChange"
    >
      <SwiperSlide v-for="(photo, i) in images" :key="i">
        <div class="swiper-zoom-container">
          <NuxtImg class="thumb" :src="photo" />
        </div>
      </SwiperSlide>
    </Swiper>
    <div class="swiper-pagination" />
  </div>
</template>

<style scoped lang="scss">
@import "swiper/css";
@import "swiper/css/zoom";
@import "swiper/css/mousewheel";
@import "swiper/css/pagination";

::v-deep(.swiper-pagination-bullets) {
  bottom: 20px !important;
  position: absolute;
}

::v-deep(.swiper-pagination-bullet) {
  background: white;
  opacity: 0.6;
  transition: opacity 0.3s;
}

::v-deep(.swiper-pagination-bullet-active) {
  background: #ff4081;
  opacity: 1;
}

// Галерея превьюшек
.gallery {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

// Превью изображений
.thumb {
  width: 500px;
  height: auto;
  cursor: pointer;
  border-radius: 8px;
  object-fit: cover;
}

// Оверлей слайдера
.coaches-detail-images {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.9);
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

// Контейнер Swiper
.swiper-container {
  width: 80vw;
  height: 80vh;
}

// Пагинация внизу по центру (если нужно числовое отображение)
/*
.pagination {
  position: absolute;
  bottom: 20px;
  right: 50%;
  transform: translateX(-50%);
  color: white;
  font-size: 18px;
  background: rgba(0, 0, 0, 0.5);
  padding: 6px 12px;
  border-radius: 6px;
  user-select: none;
}
*/
</style>
