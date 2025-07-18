<script setup lang="ts">
import type { IPost } from "~/types";
import { Navigation, Pagination } from "swiper/modules";
import { Swiper, SwiperSlide } from "swiper/vue";
import type { Swiper as SwiperClass } from "swiper/types";
import "swiper/css";
import "swiper/css/pagination";
import "swiper/css/navigation";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

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
  <div class="post-swiper-container">
    <div class="post-swiper-container__header">
      <div class="post-swiper-container__header-wrapper">
        <h2 class="post-swiper-container__header-wrapper-title">
          Последние статьи
        </h2>
        <p class="post-swiper-container__header-wrapper-subtitle">
          Полезные материалы от наших тренеров
        </p>
      </div>
      <div class="post-swiper-container__header-btns">
        <button ref="prevPostEl" class="button-prev">
          <Icon :name="HeroIcons.CHEVRON_LEFT" size="22" />
        </button>
        <button ref="nextPostEl" class="button-next">
          <Icon :name="HeroIcons.CHEVRON_RIGHT" size="22" />
        </button>
      </div>
    </div>
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
  </div>
</template>

<style scoped lang="scss">
.swiper {
  width: 100%;
}
.post-swiper-container {
  width: 100%;
  overflow: visible;
  margin-block: 50px;
  position: relative;
  &__header {
    display: flex;
    flex-direction: column;
    align-items: center;
    @include mediaTablet {
      flex-direction: row;
      align-items: start;
      justify-content: center;
    }
    &-wrapper {
      display: flex;
      flex-direction: column;

      @include mediaTablet {
        flex: 1;
      }
      &-title {
        font-size: 2.5rem;
        margin-bottom: 15px;
        color: $accent;
        text-align: center;
      }
      &-subtitle {
        font-size: 1.2rem;
        margin-bottom: 10px;
        text-align: center;
        color: $header_link;
        @include mediaTablet {
          margin-bottom: 40px;
        }
      }
    }
    &-btns {
      display: flex;
      align-items: center;
      gap: 10px;
      padding: 10px;

      @include mediaTablet {
        margin-left: auto;
      }
    }
  }
}

.button-next,
.button-prev {
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

  span {
    color: $txt;
  }
}

.button-next::after,
.button-prev::after {
  font-size: 16px;
  font-weight: 600;
  color: $txt;
}

.button-next:hover,
.button-prev:hover {
  opacity: 0.7;
}
</style>
