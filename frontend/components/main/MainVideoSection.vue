<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
const text = ref("Начни сейчас и никогда не останавливайся.".split(""));
</script>
<template>
  <section class="main-video-section">
    <video autoplay muted loop playsinline class="main-video-section__video">
      <source src="/video/sport_1.mp4" type="video/mp4" />
      Ваш браузер не поддерживает видео.
    </video>
    <div class="main-video-section__overlay"></div>
    <div class="main-video-section__wraper container">
      <h1 class="main-video-section__wraper-title">
        <span
          v-for="(letter, indx) in text"
          :key="indx"
          class="letter"
          :class="{ 'letter__last': indx === text.length - 1 }"
          :style="{ animationDelay: `${indx * 0.08}s` }"
        >
          {{ letter === " " ? "\u00A0" : letter }}
        </span>
      </h1>
      <a
        class="main-video-section__wraper-arrow"
        href="#main-about-section"
      >
        <Icon
          class="main-video-section__wraper-arrow-icon"
          :name="HeroIcons.DOWN"
        />
        <Icon
          class="main-video-section__wraper-arrow-icon"
          :name="HeroIcons.DOWN"
        />
        <Icon
          class="main-video-section__wraper-arrow-icon"
          :name="HeroIcons.DOWN"
        />
      </a>
    </div>
  </section>
</template>

<style scoped lang="scss">
.main-video-section {
  position: relative;
  width: 100%;
  height: 100vh;
  overflow: hidden;
}

.main-video-section__video {
  position: absolute;
  top: 0;
  left: 0;
  object-fit: cover;
  width: 100%;
  height: 100%;
  z-index: -2;
}

.main-video-section__overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5); /* Тёмный полупрозрачный слой */
  z-index: -1;
}

.main-video-section__wraper {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 20px;

  &-arrow {
    display: flex;
    flex-direction: column;
    color: $accent;

    &-icon {
      font-size: 48px;
    }
  }

  &-title {
    font-weight: 400;
    font-size: 46px;
    width: 600px;
    margin-bottom: 20px;
    text-align: center;
    text-shadow: 0px 4px 4px rgba(160, 33, 33, 0.25);
  }
}

.letter {
  display: inline-block;
  opacity: 0;
  color: $white;
  animation: opacity_letter 0.5s ease forwards;

  &__last{
    color: $accent;
  }
}

@keyframes opacity_letter {
  from {
    opacity: 0;
    scale: 0.9;
  }
  to {
    opacity: 1;
    scale: 1;
  }
}
.main-video-section__wraper-arrow-icon:nth-child(1) {
  animation: arrow_wave 2s ease-in-out 0s infinite;
}
.main-video-section__wraper-arrow-icon:nth-child(2) {
  animation: arrow_wave 2s ease-in-out 0.4s infinite;
}
.main-video-section__wraper-arrow-icon:nth-child(3) {
  animation: arrow_wave 2s ease-in-out 0.8s infinite;
}

@keyframes arrow_wave {
  0% {
    opacity: 0.2;
    transform: translateY(0px) scale(0.5);
  }
  50% {
    opacity: 1;
    transform: translateY(-10px) scale(1);
  }
  100% {
    opacity: 0;
    transform: translateY(0px) scale(0.5);
  }
}
</style>
