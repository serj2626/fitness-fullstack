<script setup lang="ts">
import type { IMainAbonementResponse } from "~/types";

defineProps<{ plan: IMainAbonementResponse; isActive: boolean }>();
</script>
<template>
  <div
    class="abonement-card-by-form"
    :class="{ 'abonement-card-by-form_active': isActive }"
  >
    <h3 class="abonement-card-by-form__title">{{ plan.title }}</h3>
    <p class="abonement-card-by-form__price">
      {{ formatNumberCustom(plan.price) }} ₽
    </p>
    <ul class="abonement-card-by-form__features">
      <li v-for="feature in plan.services" :key="feature">
        {{ feature }}
      </li>
    </ul>
    <div class="abonement-card-by-form__sale" v-if="1 > 0">-4%</div>
    <div v-if="plan.is_popular" class="abonement-card-by-form__popular">
      Популярный
    </div>
  </div>
</template>
<style scoped lang="scss">
.abonement-card-by-form {
  position: relative;
  background: lighten($bg, 5%);
  border: 2px solid lighten($bg, 10%);
  border-radius: 12px;
  padding: 20px;
  cursor: pointer;
  transition: all 0.3s ease;
  overflow: hidden;

  &:hover {
    transform: translateY(-5px);
    border-color: $accent;
  }

  &_active {
    border-color: $accent;
    box-shadow: 0 0 0 2px $accent;
  }

  &__title {
    color: $white;
    font-size: 1.3rem;
    margin-bottom: 10px;
  }

  &__price {
    color: $accent;
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 15px;
  }

  &__features {
    color: rgba($white, 0.8);
    padding-left: 20px;
    margin-bottom: 0;
    line-height: 1.6;

    li {
      margin-bottom: 8px;
      position: relative;

      &::before {
        content: "•";
        color: $accent;
        position: absolute;
        left: -15px;
      }
    }
  }

  &__sale {
    position: absolute;
    top: 5px;
    right: 5px;
    background: $red;
    color: $white;
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
  }

  &__popular {
    position: absolute;
    top: 35px;
    right: -10px;
    background: $accent;
    color: rgba($txt, 0.6);
    padding: 3px 10px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    rotate: 45deg;
  }
}
</style>
