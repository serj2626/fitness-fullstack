<script setup lang="ts">
import type { IPost } from "~/types";
import { Navigation, Pagination } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import type { Swiper as SwiperClass } from "swiper/types";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";

defineProps<{ posts: IPost[] | null }>();

const swiperRef = ref<InstanceType<typeof Swiper> | null>(null);
const prevPostEl = ref<HTMLElement | null>(null);
const nextPostEl = ref<HTMLElement | null>(null);
const swiperInstance = ref<SwiperClass | null>(null);
const currentSlideIndex = ref<number>(0);

const onSwiper = (swiper: SwiperClass): void => {
  swiperInstance.value = swiper;
};

const onSlideChange = (): void => {
  if (swiperInstance.value) {
    currentSlideIndex.value = swiperInstance.value.activeIndex;
  }
};
</script>
<template>
  <div class="swiper-container">
    <Swiper
      ref="swiperRef"
      :modules="[Pagination, Navigation]"
      :breakpoints="{
        0: { slidesPerView: 1 },
        768: { slidesPerView: 2 },
        1024: { slidesPerView: 3 },
      }"
      :space-between="20"
      :loop="true"
      :navigation="{
        prevEl: prevPostEl,
        nextEl: nextPostEl,
      }"
      :slides-per-group="1"
      class="swiper"
      @swiper="onSwiper"
      @slide-change="onSlideChange"
    >
      <SwiperSlide v-for="post in posts || []" :key="post.id">
        <PostCard :post />
      </SwiperSlide>
    </Swiper>

    <div class="swiper-btns">
      <div ref="prevPostEl" class="swiper-button-prev"></div>
      <div ref="nextPostEl" class="swiper-button-next"></div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.swiper {
  width: 100%;
}
.swiper-container {
  width: 100%;
  overflow: visible;
  margin-block: 50px;
  position: relative;
}

.swiper-btns {
  position: absolute;
  top: -100px;
  right: 0;
  z-index: 10;
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 10px;
}
.swiper-button-next,
.swiper-button-prev {
  position: static !important;
  width: 50px;
  height: 50px;
  background-color: $accent;
  border-radius: 50%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease-in;
}

.swiper-button-next::after,
.swiper-button-prev::after {
  font-size: 16px;
  font-weight: 600;
  color: $txt;
}

.swiper-button-next:hover,
.swiper-button-prev:hover {
  opacity: 0.7;
}
</style>
