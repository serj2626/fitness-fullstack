<script setup lang="ts">
import type { ICoach } from "~/types";

defineProps<{ trainer: ICoach }>();
</script>
<template>
  <div class="card">
    <div class="card__image-wrapper">
      <img
        class="card__image"
        :src="trainer.avatar"
        :alt="trainer.first_name"
      />
      <span class="card__position">{{ trainer.position }}</span>
    </div>
    <div class="card__body">
      <h3 class="card__name">
        {{ trainer.first_name }} {{ trainer.last_name }}
      </h3>
      <p class="card__experience">
        🏆 Стаж: <strong>{{ trainer.experience }} лет</strong>
      </p>
      <p class="card__bio">
        {{ trainer.content }}
      </p>
      <BaseButton
        label="Подробнее"
        size="lg"
        class="card__btn"
        @click="$router.push(`/coaches/${trainer.id}`)"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.card {
  background: linear-gradient(145deg, #ffffff, #f3f3f3);
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 12px 25px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease-in-out;
  display: flex;
  flex-direction: column;

  &:hover {
    transform: translateY(-6px);
    box-shadow: 0 20px 40px rgba(0, 0, 0, 0.15);
  }

  &__image-wrapper {
    position: relative;
    height: 320px;
    overflow: hidden;
    border-top-left-radius: 20px;
    border-top-right-radius: 20px;
  }

  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: center top;
    transition: all 0.3s ease-in-out;
  }

  &__image-wrapper:hover .card__image {
    transform: scale(1.05);
  }

  &__position {
    position: absolute;
    bottom: 16px;
    left: 16px;
    background: rgba(255, 255, 255, 0.85);
    padding: 6px 14px;
    border-radius: 20px;
    font-weight: 600;
    color: #333;
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
    color: white;
    font-weight: 600;
  }
}
</style>
