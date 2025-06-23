<script setup lang="ts">
import type { ICoach } from "~/types";

defineProps<{ trainer: ICoach }>();
</script>
<template>
  <div class="trainer-card">
    <div class="trainer-card__top">
      <img
        class="trainer-card__top-image"
        :src="trainer.avatar"
        :alt="trainer.first_name"
      />
      <span class="trainer-card__top-position">{{ trainer.position }}</span>
    </div>
    <div class="trainer-card__info">
      <h3 class="trainer-card__info-name">
        {{ trainer.first_name }} {{ trainer.last_name }}
      </h3>
      <p class="trainer-card__info-experience">
        {{ trainer.experience }} лет опыта
      </p>
      <p
        v-if="trainer.content.length > 0"
        class="trainer-card__info-bio"
        v-html="trainer.content"
      />

      <!-- <button @click="$router.push(`/coaches/${trainer.id}`)" class="btn-book">
        Профиль
      </button> -->
      <BaseButton
        label="Подробнее"
        size="lg"
        class="btn-book"
        style="width: 100%"
        @click="$router.push(`/coaches/${trainer.id}`)"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.trainer-card {
  background: $white;
  border-radius: 8px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(255, 243, 243, 0.1);
  transition: transform 0.3s, box-shadow 0.3s;
  cursor: pointer;

  &:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 30px rgba(0, 0, 0, 0.2);
  }
  &__top {
    position: relative;
    height: 400px;
    overflow: hidden;
    &-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s;
    }
    &__position {
      position: absolute;
      bottom: 20px;
      left: 20px;
      background: $accent;
      color: $txt;
      padding: 5px 15px;
      border-radius: 20px;
      font-weight: 600;
    }
    &:hover img {
      transform: scale(1.05);
    }
  }

  &__info {
    padding: 20px;
    &-name {
      font-size: 1.4rem;
      margin-bottom: 5px;
    }
    &-experience {
      color: $grey;
      margin-bottom: 10px;
      font-size: 0.9rem;
    }
    &-bio {
      color: $grey;
      margin-bottom: 20px;
      line-height: 1.5;
    }
  }
}
</style>
