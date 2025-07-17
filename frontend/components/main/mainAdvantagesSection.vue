<script setup lang="ts">
import type { IAdvantageResponse } from "~/types";

defineProps<{
  advantages: IAdvantageResponse[];
}>();
</script>
<template>
  <section class="main-advantages-section">
    <div class="container">
      <h2
        class="main-advantages-section__title"
        data-aos="zoom-in"
        data-aos-duration="1000"
      >
        Наши преимущества <BaseDot />
      </h2>
      <div class="main-advantages-section__list">
        <div
          v-for="(advantage, idx) in advantages"
          :key="advantage.id"
          class="main-advantages-section__list-card"
          data-aos="fade-up"
          :data-aos-delay="idx * 200"
        >
          <img
            class="main-advantages-section__list-card-icon"
            :src="advantage.icon"
            :alt="advantage.alt"
          />

          <h3 class="main-advantages-section__list-card-title">
            {{ advantage.title }}
          </h3>
          <p class="main-advantages-section__list-card-text">
            {{ advantage.description }}
          </p>
        </div>
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss">
.main-advantages-section {
  padding: 100px 0;

  &__title {
    color: $accent;
    font-size: 2rem;
    margin-bottom: 1.5rem;
    text-align: center;
  }
  &__list {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 20px;
    margin-top: 3rem;
    &-card {
      background: $bg_block;
      padding: 2rem;
      border-radius: 8px;
      text-align: center;
      transition: all 0.3s ease;
      border-bottom: 3px solid transparent;

      &:hover {
        transform: translateY(-10px);
        border-bottom-color: $accent;
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      }

      &-icon {
        margin-bottom: 1.5rem;
        width: 40px;
        height: 40px;
      }

      &-title {
        color: $accent;
        margin-bottom: 1rem;
        font-size: 1.3rem;
      }

      &-text {
        color: rgba($white, 0.8);
        line-height: 1.6;
        margin: 0;
      }
    }
  }
}
</style>
