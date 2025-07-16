<script setup lang="ts">
import { NuxtImg } from "#components";
import type { IEequipmentResponse } from "~/types";
defineProps<{ equipment: IEequipmentResponse }>();
</script>
<template>
  <div class="main-equipment-card">
    <div class="main-equipment-card__top">
      <h3 class="main-equipment-card__top-title">{{ equipment.title }}</h3>
      <p class="main-equipment-card__top-description">
        {{ equipment.description }}
      </p>
      <ul
        v-if="equipment.services.length > 0"
        class="main-equipment-card__services"
      >
        <li
          v-for="service in equipment.services.split(',')"
          :key="service"
          class="main-equipment-card__services-item"
        >
          {{ service }}
        </li>
      </ul>
    </div>
    <div class="main-equipment-card__slider">
      <NuxtImg
        :src="equipment.image ?? ''"
        alt="Кардио-зона"
        class="main-equipment-card__slider-image"
      />
    </div>
  </div>
</template>
<style scoped lang="scss">
.main-equipment-card {
  display: grid;
  grid-template-columns: 1fr 1fr;
  min-height: 400px;

  @media (max-width: $tablet) {
    grid-template-columns: 1fr;
  }

  background: transparent;
  color: $white;
  border: none;
  padding: 0.75rem 1.5rem;
  font-size: 1rem;
  border-radius: 4px;
  transition: all 0.3s ease;
  position: relative;

  &.active {
    color: $accent;
    font-weight: 600;

    &::after {
      content: "";
      position: absolute;
      bottom: -8px;
      left: 50%;
      transform: translateX(-50%);
      width: 50%;
      height: 2px;
      background: $accent;
    }
  }
  &__top {
    padding: 2rem;
    display: flex;
    flex-direction: column;
    gap: 10px;

    h3 {
      color: $accent;
      font-size: 1.5rem;
      margin-top: 0;
    }

    p {
      line-height: 1.6;
      margin-bottom: 1.5rem;
    }
  }
  &__services {
    list-style: none;
    padding: 0;
    margin: 1.5rem 0 0;

    li {
      position: relative;
      padding-left: 1.5rem;
      margin-bottom: 0.5rem;

      &::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0.6em;
        width: 8px;
        height: 8px;
        background: $accent;
        border-radius: 50%;
      }
    }
  }
  &__slider {
    position: relative;
    overflow: hidden;

    &-image {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s ease;
      filter: brightness(70%);

      &:hover {
        transform: scale(1.05);
      }
    }

    @media (max-width: $tablet) {
      height: 300px;
    }
  }
}
</style>
