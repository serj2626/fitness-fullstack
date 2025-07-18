<script setup lang="ts">
import { Navigation, Pagination, Autoplay } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import type { Swiper as SwiperClass } from "swiper/types";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation"; // Добавлено
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const swiperRef = ref<InstanceType<typeof Swiper> | null>(null);
const prevBtn = ref<HTMLElement | null>(null);
const nextBtn = ref<HTMLElement | null>(null);
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

// Очистка при размонтировании
onBeforeUnmount(() => {
  if (swiperInstance.value) {
    swiperInstance.value.destroy(true, true);
    swiperInstance.value = null;
  }
});
</script>

<template>
  <div class="main-first-section">
    <div class="main-first-section__swiper-container">
      <Swiper
        ref="swiperRef"
        :modules="[Pagination, Navigation, Autoplay]"
        :breakpoints="{
          0: { slidesPerView: 1 },
          768: { slidesPerView: 1 },
          1024: { slidesPerView: 1 },
        }"
        :autoplay="{
          delay: 3000, // Интервал в миллисекундах (3 секунды)
          disableOnInteraction: false, // Продолжать после взаимодействия
          pauseOnMouseEnter: false, // Пауза при наведении
        }"
        :loop="true"
        :navigation="{
          enabled: true,
          prevEl: prevBtn,
          nextEl: nextBtn,
        }"
        :slides-per-group="1"
        class="swiper"
        @swiper="onSwiper"
        @slide-change="onSlideChange"
      >
        <SwiperSlide>
          <NuxtImg class="slide-img" src="/first/zal.jpg" />
        </SwiperSlide>
        <SwiperSlide>
          <NuxtImg format="webp" class="slide-img" src="/first/spa_zona.jpeg" />
        </SwiperSlide>
        <SwiperSlide>
          <NuxtImg class="slide-img" format="webp" src="/first/group.jpg" />
        </SwiperSlide>
      </Swiper>

      <NuxtImg
        alt="decorative woman"
        class="main-first-section__swiper-container-img"
        format="webp"
        src="/woman.png"
      />
      <button ref="prevBtn" class="prev-btn">
        <Icon :name="HeroIcons.CHEVRON_LEFT" size="22" />
      </button>
      <button ref="nextBtn" class="next-btn">
        <Icon :name="HeroIcons.CHEVRON_RIGHT" size="22" />
      </button>
      <!-- <BaseButtonNavigation ref="prevBtn" class="prev-btn" />
      <BaseButtonNavigation ref="nextBtn" type="next" class="next-btn" /> -->
    </div>
  </div>
</template>

<style scoped lang="scss">
.main-first-section {
  width: 100%;
  height: 400px;
  @include mediaMobile {
    height: 600px;
  }
  @include mediaTablet {
    width: 100%;
    height: 100vh;
  }

  &__swiper-container {
    width: 100%;
    height: 100%;
    position: relative;

    &-img {
      position: absolute;
      left: 50%;
      bottom: 0;
      transform: translateX(-50%);
      z-index: 10;
      display: none;
      pointer-events: none;

      @include mediaCustom(500px) {
        display: block;
        height: 400px;
      }

      @include mediaTablet {
        height: 600px;
      }
    }
  }
}

.swiper {
  position: relative;
  width: 100%;
  height: 100%;
}

.slide-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(50%) grayscale(80%);
}

.prev-btn,
.next-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  z-index: 1000;
  background: $accent;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  border: none;
  cursor: pointer;
  color: $txt;
  transition: opacity 0.3s ease-in-out;

  &:hover {
    opacity: 0.8;
  }
}

.prev-btn {
  left: 20px;
}

.next-btn {
  right: 20px;
}
</style>
