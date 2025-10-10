<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const {
  size = 20,
  top = "0",
  right = "0",
  color = "#ffc451",
} = defineProps<{
  size?: number;
  top?: string;
  right?: string;
  color?: string;
}>();

const emit = defineEmits<{
  (e: "click"): void;
}>();
</script>

<template>
  <button class="base-button-close" @click="emit('click')">
    <Icon
      :size="size"
      :name="HeroIcons.CLOSE"
      class="base-button-close__icon"
      :style="{ color }"
    />
  </button>
</template>

<style scoped lang="scss">
.base-button-close {
  position: absolute;
  top: v-bind(top);
  right: v-bind(right);
  cursor: pointer;
  transition: all 0.3s ease-in;

  &:hover {
    scale: 1.2;
  }

  &__icon {
    display: block;
  }
}
</style>
