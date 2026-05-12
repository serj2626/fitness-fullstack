<script setup lang="ts">
import type { IVacancy } from "~/types";

defineProps<{ vacancy: IVacancy }>();
</script>
<template>
  <div class="vacancy-card">
    <h3 class="vacancy-card__title">{{ vacancy?.title }}</h3>

    <div class="vacancy-card__meta">
      <time
        class="vacancy-card__date"
        :datetime="vacancy.created_at.toString()"
      >
        {{ formatDate(String(vacancy?.created_at)) }}
      </time>
      <span v-if="vacancy.location" class="vacancy-card__location">
        {{ vacancy?.location }}
      </span>
    </div>

    <p class="vacancy-card__description">
      {{ vacancy?.description }}
    </p>

    <div class="vacancy-card__footer">
      <span v-if="vacancy.salary" class="vacancy-card__salary">
        {{ vacancy?.salary }}
      </span>
      <NuxtLink :to="`/vacancies/${vacancy.id}`" class="vacancy-card__link">
        Подробнее
        <span class="vacancy-card__arrow">→</span>
      </NuxtLink>
    </div>
  </div>
</template>
<style scoped lang="scss">
.vacancy-card {
  background: $bg_block;
  backdrop-filter: blur(2px);
  border-radius: 24px;
  border: 1px solid rgba($white, 0.08);
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  cursor: pointer;

  &__title {
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1.3;
    margin: 0 0 16px 0;
    color: $white;
    letter-spacing: -0.02em;

    @media (max-width: $tablet) {
      font-size: 1.3rem;
    }
  }

  &__meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 20px;
    font-size: 0.85rem;
    color: $text-secondary;
  }

  &__date {
    display: inline-flex;
    align-items: center;
    gap: 6px;

    &::before {
      content: "📅";
      font-size: 0.9rem;
      opacity: 0.8;
    }
  }

  &__location {
    display: inline-flex;
    align-items: center;
    gap: 6px;

    &::before {
      content: "📍";
      font-size: 0.9rem;
    }
  }

  &__description {
    color: rgba($white, 0.75);
    line-height: 1.55;
    margin: 0 0 28px 0;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  &__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    border-top: 1px solid rgba($white, 0.08);
    padding-top: 20px;
  }

  &__salary {
    background: rgba($accent, 0.12);
    color: $accent;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 6px 14px;
    border-radius: 40px;
    letter-spacing: 0.01em;
  }

  &__link {
    color: rgba($white, 0.8);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: color 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;

    &:hover {
      color: $accent;
    }
  }

  &__arrow {
    transition: transform 0.2s ease;
    display: inline-block;
  }
}
</style>
