<script lang="ts" setup>
import "swiper/css";
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IServicesResponse } from "~/types";
const modalsStore = useModalsStore();
defineProps<{ services: IServicesResponse[] }>();
</script>

<template>
  <section id="main-services-section" class="main-services-section">
    <div class="container">
      <h2
        class="main-services-section__title"
        data-aos="zoom-in"
        data-aos-duration="1000"
      >
        Наши услуги <BaseDot />
      </h2>
    </div>
    <BaseSwiper
      :desctop-between="0"
      :laptop-between="0"
      :tablet-between="0"
      :auto-delay="0"
    >
      <swiper-slide
        v-for="slide in services"
        :key="slide.id"
        class="slide"
        @click="modalsStore.openModal('service', slide)"
      >
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

  &__title {
    color: $accent;
    font-size: 2rem;
    margin-bottom: 5rem;
    text-align: center;
  }
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
    z-index: 100;
    color: $white;
    font-weight: 600;
    font-size: 22px;
    text-transform: uppercase;
    transition: all 0.5s ease-in-out;
  }

  &__btn {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%) scale(0);
    z-index: 100;
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background-color: rgba(255, 197, 81, 0.6);
    opacity: 0;
    transition: all 0.6s ease-in-out;
    display: flex;
    justify-content: center;
    align-items: center;
    border: none;
    outline: none;
    cursor: pointer;
    will-change: transform, opacity;

    &-icon {
      transform: rotate(90deg);
      font-size: 40px;
      color: $white;
    }
  }

  &__img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    filter: brightness(0.8);
    transition: filter 0.3s ease-in, transform 4s ease-in-out;
  }

  &:hover {
    .slide__title {
      transform: translate(-10px, 100%);
      opacity: 0;
    }

    .slide__btn {
      opacity: 1;
      transform: translate(-50%, -50%) scale(1);
    }

    .slide__img {
      filter: brightness(1);
      transform: scale(1.1);
    }
  }
}
</style>
