<script setup lang="ts">
import type { ICoach } from "~/types";

defineProps<{ trainer: ICoach }>();
</script>
<template>
  <div class="coach-card">
    <div class="coach-card__image-wrapper">
      <NuxtImg
        format="webp"
        lazy="loading"
        class="coach-card__image-wrapper-img"
        :src="getMedia(trainer?.avatar as string)"
        :alt="`${trainer.first_name} ${trainer.last_name}`"
      />
      <span class="coach-card__position">{{
        getCategories(trainer.categories)
      }}</span>
    </div>
    <div class="coach-card__body">
      <h3 class="coach-card__name">
        {{ trainer.first_name }} {{ trainer.last_name }}
      </h3>
      <p class="coach-card__experience">
        🏆 Стаж:
        <strong>{{ getExperience(trainer.experience) }} </strong>
      </p>
      <BaseButton
        label="Подробнее"
        size="lg"
        class="coach-card__btn"
        @click="$router.push(`/coaches/${trainer.id}`)"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.coach-card {
  background: linear-gradient(145deg, #ffffff, #f3f3f3);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease-in-out;
  display: flex;
  flex-direction: column;

  &:hover {
    // transform: translateY(-2px);

    .coach-card__position {
      opacity: 1;
    }
    .coach-card__image-wrapper-img {
      transform: scale(1.05);
    }
  }

  &__image-wrapper {
    position: relative;
    height: 320px;
    overflow: hidden;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;

    &-img {
      display: block;
      width: 100%;
      height: 100%;
      object-fit: cover; 
      object-position: center top; 
      transition: all 0.3s ease-in-out;
    }
  }

  &__position {
    position: absolute;
    inset: 0;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    // bottom: 10px;
    background: rgba(0, 0, 0, 0.336);
    transition: all 0.3s ease-in-out;
    opacity: 0;
    padding: 6px 14px;
  
    font-weight: 600;
    color: #fff;
    font-size: 0.9rem;
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  }

  &__body {
    padding: 24px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  &__name {
    font-size: 1.4rem;
    font-weight: 700;
    color: #222;
  }

  &__experience {
    color: #555;
    font-size: 0.95rem;
  }

  &__bio {
    color: #666;
    font-size: 0.9rem;
    line-height: 1.6;
    flex-grow: 1;
  }

  &__btn {
    width: 100%;
    margin-top: auto;
    color: rgb(1, 1, 1);
    font-weight: 600;
  }
}
</style>
