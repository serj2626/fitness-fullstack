<script lang="ts" setup>
import { HeroIcons } from "~/assets/icons/types/hero-icons";
</script>
<template>
  <form class="base-modal">
    <div class="base-modal__content">
      <button class="base-modal__content-close" @click="$emit('close')">
        <Icon class="base-modal__content-close-icon" :name="HeroIcons.CLOSE" />
      </button>
      <slot />
    </div>
  </form>
</template>
<style lang="scss">
.base-modal {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  
  background-color: $txt;
  border-radius: 12px;
  box-shadow: 0 0 20px #fff;
  z-index: 130;
  overflow: hidden;
  // max-width: 550px;
  // width: 100%;
  &__content {
    position: relative;
    &-close {
      position: absolute;
      top: 10px;
      right: 10px;
      &-icon {
        font-size: 26px;
        color: $txt;
        transition: opacity 0.3s ease-in;
        &:hover {
          opacity: 0.8;
        }
      }
    }
  }
}
</style>
