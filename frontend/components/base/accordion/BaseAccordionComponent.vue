<script setup lang="ts">
const { isOpen = false } = defineProps<{ isOpen?: boolean }>();
</script>
<template>
  <div
    class="base-accordion-component"
    :class="{ 'base-accordion-component_open': isOpen }"
  >
    <div class="base-accordion-component__summary">
      <slot name="summary" />
    </div>
    <div class="base-accordion-component__content">
      <slot />
    </div>
  </div>
</template>
<style lang="scss" scoped>
.base-accordion-component {
  display: flex;
  flex-direction: column;
  width: 100%;
  background-color: $grey;
  padding: 15px 15px 15px 30px;
  border-radius: 15px;
  cursor: pointer;
  transition: box-shadow 0.3s ease-in;

  &__content {
    overflow: hidden;
    max-height: 0;
    transition: max-height 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  }

  &_open {
    box-shadow: 0 5px 15px $accent;
    gap: 15px;

    .base-accordion-component__content {
      max-height: 1500px; // Достаточно большое значение для вашего контента
      transition: max-height 0.5s cubic-bezier(0.4, 0, .6, 1);
    }
  }
}
</style>
