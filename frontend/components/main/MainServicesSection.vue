<script lang="ts" setup>
// import { services } from "~/assets/data/moke.data";
import "swiper/css";
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IServicesResponse } from "~/types";

defineProps<{ services: IServicesResponse[] }>();
</script>
<template>
  <section id="main-services-section" class="main-services-section">
    <BaseSwiper
      :desctop-between="0"
      :laptop-between="0"
      :tablet-between="0"
      :auto-delay="0"
    >
      <swiper-slide v-for="slide in services" :key="slide.id" class="slide">
        <p class="slide__title">{{ slide.alt }}</p>
        <button class="slide__btn">
          <Icon class="slide__btn-icon" :name="HeroIcons.UP" />
        </button>
        <NuxtImg :src="slide.avatar" :alt="slide.alt" class="slide__img" />
      </swiper-slide>
    </BaseSwiper>
  </section>
</template>
<style lang="scss" scoped>
.main-services-section {
  padding-block: 100px;
}
.slide {
  display: flex;
  justify-content: center;
  align-items: center;
  height: auto;
  background-color: #f9f9f9;
  overflow: hidden;
  cursor: pointer;
  position: relative;

  &__title {
    position: absolute;
    top: 5%;
    left: 10%;
    transform: translate(-10%, -5%);
    z-index: 100;
    color: $white;
    text-align: center;
    font-weight: 600;
    font-size: 22px;
    text-transform: uppercase;
    transition: all 0.5s ease-in-out;
  }

  &:hover {
    .slide__title {
      transform: translate(-10px, 100%);
      opacity: 0;
    }
    .slide__btn {
      opacity: 1;
      scale: 1;
      // transform: translate(-50%, -50%) scale(1.2);
    }
  }

  &__btn {
    content: "";
    pointer-events: none;
    display: block;

    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    z-index: 100;

    width: 120px;
    height: 120px;
    border-radius: 50%;

    background-color: #ffc5519a;

    opacity: 0;
    scale: 0;
    transition: opacity 0.3s ease-in-out;
    &-icon {
      rotate: 90deg;
      font-size: 40px;
      color: $white;
    }
  }

  &__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.8);
    transition: filter 0.3s ease-in, transform 6s ease-in-out;

    &:hover {
      filter: brightness(1);
      transform: scale(2);
    }
  }
}
</style>
