<script setup lang="ts">
import { Swiper, SwiperSlide } from "swiper/vue";
import { Mousewheel, Zoom, Pagination, Navigation } from "swiper/modules";
import 'swiper/css';
import 'swiper/css/zoom';
import 'swiper/css/mousewheel';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

const props = defineProps<{
  startIndex: number;
  images?: string[];
}>();

const emit = defineEmits(['close']);

const currentSlide = ref(props.startIndex);
const zoomed = ref(false);
const swiperInstance = ref<any>(null);

const onSlideChange = (swiper: any) => {
  currentSlide.value = swiper.realIndex;
};

const handleZoomChange = (swiper: any) => {
  zoomed.value = swiper.zoom.scale > 1;
  // Отключаем листание при зуме
  if (swiperInstance.value) {
    swiperInstance.value.mousewheel.disable = zoomed.value;
  }
};

const handleKeyDown = (e: KeyboardEvent) => {
  if (e.key === 'Escape') {
    emit('close');
  }
};

const onSwiper = (swiper: any) => {
  swiperInstance.value = swiper;
};

onMounted(() => {
  window.addEventListener('keydown', handleKeyDown);
});

onUnmounted(() => {
  window.removeEventListener('keydown', handleKeyDown);
});
</script>

<template>
  <div class="image-viewer">
    <div class="viewer-overlay" @click.self="emit('close')" />
    
    <button class="close-button" @click="emit('close')">
      <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
        <path d="M18 6L6 18M6 6L18 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
      </svg>
    </button>

    <div class="counter">
      {{ currentSlide + 1 }} / {{ images?.length }}
    </div>

    <Swiper
      :loop="true"
      :pagination="{ 
        el: '.swiper-pagination', 
        clickable: true,
        type: 'fraction'
      }"
      :navigation="{
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev'
      }"
      :modules="[Mousewheel, Zoom, Pagination, Navigation]"
      :initial-slide="startIndex"
      :mousewheel="{
        forceToAxis: false,
        sensitivity: 1,
        releaseOnEdges: true,
        thresholdDelta: 10
      }"
      :zoom="{
        maxRatio: 3,
        toggle: true
      }"
      :slides-per-view="1"
      class="swiper-container"
      @swiper="onSwiper"
      @slide-change="onSlideChange"
      @zoom-change="handleZoomChange"
    >
      <SwiperSlide v-for="(photo, i) in images" :key="i">
        <div class="swiper-zoom-container">
          <NuxtImg 
            class="slide-image" 
            :src="photo" 
            :alt="`Фото тренера ${i + 1}`"
            loading="lazy"
          />
        </div>
      </SwiperSlide>

      <div class="swiper-button-prev" :class="{ hidden: zoomed }">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M15 18L9 12L15 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>
      <div class="swiper-button-next" :class="{ hidden: zoomed }">
        <svg width="24" height="24" viewBox="0 0 24 24" fill="none">
          <path d="M9 18L15 12L9 6" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>
        </svg>
      </div>
    </Swiper>

    <div class="swiper-pagination" :class="{ hidden: zoomed }" />
    
    <div class="hint" :class="{ hidden: zoomed }">
      <span>Колесико мыши</span> для листания
    </div>
  </div>
</template>

<style scoped lang="scss">
.image-viewer {
  position: fixed;
  inset: 0;
  z-index: 9999;
  display: flex;
  align-items: center;
  justify-content: center;
}

.viewer-overlay {
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.9);
  backdrop-filter: blur(5px);
}

.close-button {
  position: absolute;
  top: 30px;
  right: 30px;
  width: 50px;
  height: 50px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  border-radius: 50%;
  color: white;
  cursor: pointer;
  z-index: 10;
  transition: all 0.3s ease;

  &:hover {
    background: rgba(255, 255, 255, 0.2);
    transform: rotate(90deg);
  }

  svg {
    width: 24px;
    height: 24px;
  }
}

.counter {
  position: absolute;
  top: 30px;
  left: 30px;
  color: white;
  font-size: 16px;
  background: rgba(0, 0, 0, 0.5);
  padding: 8px 16px;
  border-radius: 20px;
  z-index: 10;
}

.swiper-container {
  width: 90vw;
  height: 90vh;
  position: relative;
  z-index: 1;
}

.slide-image {
  width: 100%;
  height: 100%;
  object-fit: contain;
  max-height: 90vh;
}

.swiper-button-prev,
.swiper-button-next {
  color: white;
  width: 60px;
  height: 60px;
  background: rgba(0, 0, 0, 0.3);
  border-radius: 50%;
  transition: all 0.3s ease;
  opacity: 0.7;

  &:hover {
    opacity: 1;
    background: rgba(0, 0, 0, 0.5);
  }

  &.hidden {
    opacity: 0;
    pointer-events: none;
  }

  &::after {
    display: none;
  }

  svg {
    width: 24px;
    height: 24px;
  }
}

.swiper-pagination {
  color: white;
  font-size: 16px;
  background: rgba(0, 0, 0, 0.5);
  padding: 8px 16px;
  border-radius: 20px;
  width: auto;
  left: 50%;
  transform: translateX(-50%);
  bottom: 30px !important;

  &.hidden {
    opacity: 0;
    pointer-events: none;
  }
}

.hint {
  position: absolute;
  bottom: 80px;
  left: 50%;
  transform: translateX(-50%);
  color: rgba(255, 255, 255, 0.7);
  font-size: 14px;
  background: rgba(0, 0, 0, 0.5);
  padding: 6px 12px;
  border-radius: 20px;
  z-index: 10;
  transition: opacity 0.3s;

  span {
    color: $accent;
    font-weight: 500;
  }

  &.hidden {
    opacity: 0;
  }
}

@media (max-width: 768px) {
  .swiper-container {
    width: 100vw;
    height: 100vh;
  }

  .close-button {
    top: 20px;
    right: 20px;
    width: 40px;
    height: 40px;
  }

  .counter {
    top: 20px;
    left: 20px;
  }

  .swiper-button-prev,
  .swiper-button-next {
    width: 40px;
    height: 40px;
  }

  .swiper-pagination {
    bottom: 20px !important;
  }

  .hint {
    display: none;
  }
}
</style>