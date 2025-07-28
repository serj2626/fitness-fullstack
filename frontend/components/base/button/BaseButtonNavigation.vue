<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

type typeButton = "prev" | "next";

const { type = "prev", size = 20 } = defineProps<{
  type?: typeButton;
  size?: number;
}>();
</script>
<template>
  <button
    v-bind="$attrs"
    class="base-button-navigation"
    :class="{ 'base-button-navigation__next': type === 'next' }"
  >
    <Icon :name="HeroIcons.CHEVRON_LEFT" :size="size" />
  </button>
</template>
<style scoped lang="scss">
.base-button-navigation {
  background-color: $accent;
  color: $txt;
  &__next {
    transform: rotate(180deg);
  }
}
</style>
