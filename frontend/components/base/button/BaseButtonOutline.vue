<script lang="ts" setup>
interface IBaseButton {
  size?: "xs" | "sm" | "md" | "lg";
  color?: string;
  label: string;
  disabled?: boolean;
  radius?: string;
}

const {
  color = "fff",
  size = "md",
  radius = "8px",
  label,
} = defineProps<IBaseButton>();
</script>

<template>
  <button
    :class="[
      'base-button-outline',
      `base-button-outline__${size}`,
      { 'base-button-outline_disabled': disabled },
    ]"
  >
    {{ label }}
  </button>
</template>
<style scoped lang="scss">
.base-button-outline {
  background-color: v-bind(color);
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  color: $accent;

  border-radius: v-bind(radius);
  border: 1px solid $accent;
  transition: all .3s ease-in-out;
  cursor: pointer;

  &:hover {
    background-color: $accent;
    color: $txt;
  }

  &__xs {
    padding: 6px 9px;
  }

  &__sm {
    padding: 6px 12px;
  }

  &__md {
    padding: 8px 16px;
  }

  &__lg {
    padding: 16px 28px;
  }
}
</style>
