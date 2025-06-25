<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IMainAbonementResponse } from "~/types";
const modalsStore = useModalsStore();
defineProps<{ plan: IMainAbonementResponse }>();
</script>
<template>
  <div class="abonement-card-by-home-page">
    <p v-if="plan.is_popular" class="abonement-card-by-home-page_popular">
      популярный
    </p>
    <p class="abonement-card-by-home-page__top">
      {{ plan.title }}
    </p>
    <div class="abonement-card-by-home-page__body">
      <p class="abonement-card-by-home-page__body-price-months">
        <span class="abonement-card-by-home-page__body-price">
          {{ formatNumberCustom(plan.price) }} &nbsp;₽
        </span>
        <span class="abonement-card-by-home-page__body-period">
          {{ plan.number_of_months }} месяцев
        </span>
      </p>
      <p class="abonement-card-by-home-page__body-desc">
        {{ plan.description }}
      </p>
    </div>
    <div class="abonement-card-by-home-page__footer">
      <ul class="abonement-card-by-home-page__footer-services">
        <li
          v-for="(service, idx) in plan.services"
          :key="idx"
          class="abonement-card-by-home-page__footer-services-item"
        >
          <Icon
            class="abonement-card-by-home-page__footer-services-item-icon"
            :style="{ color: '#facc15' }"
            :name="HeroIcons.CHECK"
          />
          <span class="abonement-card-by-home-page__footer-services-item-text">
            {{ service }}
          </span>
        </li>
      </ul>
    </div>
    <BaseButtonOutline
      class="abonement-card-by-home-page__btn"
      label="Забронировать"
      size="lg"
      @click="modalsStore.openModal('orderAbonement')"
    />
  </div>
</template>
<style scoped lang="scss">

.abonement-card-by-home-page:hover {
  .abonement-card-by-home-page__btn {
    color: $txt;
    &:before {
      transform: scale3d(1, 1, 1);
      transform-origin: 0% 50%;
      transition-timing-function: ease;
    }
  }
}





.abonement-card-by-home-page {
  position: relative;
  display: flex;
  flex-direction: column;
  padding: 25px 32px;
  background-color: $bg;
  border-radius: 15px;
  border: 1px solid rgba(255, 255, 255, 0.222);
  color: $white;
  transition: all 0.35s ease-in;

  &_popular {
    position: absolute;
    top: 0;
    right: 0;
    padding: 10px 15px;
    background-color: $accent;
    border-radius: 0 15px 0 15px;
    color: $txt;
    font-size: 12px;
    font-weight: 600;
  }

  &:hover {
    box-shadow: 0 0 20px $accent;
  }
  &__top {
    text-transform: uppercase;
    padding-bottom: 30px;
    border-bottom: 1px solid #bdbdbd82;
    font-weight: 600;
  }
  &__body {
    padding-top: 30px;
    &-desc {
      color: $white;
      font-weight: 350;
      margin-top: 20px;
    }
    &-price {
      font-weight: 500;
      font-size: 30px;
    }
    &-period {
      color: $accent;
    }
    &-price-months {
      display: flex;
      align-items: start;
      justify-content: space-between;
    }
  }
  &__btn {
    position: relative;
    margin-top: 30px;
    width: 100%;
    padding: 15px 0;
    background-color: transparent;
    color: $white;
    border-radius: 10px;
    border: 1px solid $accent;
    cursor: pointer;
    overflow: hidden;
    transition: all 0.3s ease-in;
    z-index: 2;

    &:before {
      content: "";
      position: absolute;
      left: 0;
      bottom: 0;
      width: 100%;
      height: 100%;
      background-color: $accent;
      z-index: -1;
      transition: transform 0.7s;
      transition-timing-function: cubic-bezier(0.05, 0.73, 0.48, 0.97);
      transform: scale3d(0, 1, 1);
      transform-origin: 100% 50%;
      will-change: transform, background-color;
    }
  }

  &__footer {
    flex: 1;
    padding-top: 30px;
    &-services {
      padding-top: 30px;
      display: flex;
      flex-direction: column;
      gap: 20px;
      &-item {
        display: flex;
        align-items: center;
        gap: 10px;
        &-icon {
          // #ffc451
          // color: $accent;
          font-size: 26px;
        }
      }
    }
  }
}
</style>
