<script lang="ts" setup>
interface IBaseButtonWithIcon {
  size?: "xs" | "sm" | "md" | "lg";
  color?: string;
  label: string;
  icon: string;
  disabled?: boolean;
  radius?: string;
  reverse?: boolean;
}

const {
  color = "fff",
  size = "md",
  radius = "8px",
  label,
  reverse = false,
} = defineProps<IBaseButtonWithIcon>();
</script>

<template>
  <button
    :class="[
      'base-button-with-icon',
      `base-button-with-icon__${size}`,
      { 'base-button-with-icon_disabled': disabled },
    ]"
  >
    <span class="base-button-with-icon__label">{{ label }}</span>

    <Icon class="base-button-with-icon__icon" :name="icon" />
  </button>
</template>
<style scoped lang="scss">
.base-button-with-icon {
  background-color: v-bind(color);
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 5px;
  color: $accent;

  border-radius: v-bind(radius);
  border: 1px solid $accent;
  transition: all 0.3s ease-in-out;
  cursor: pointer;

  &:hover {
    background-color: $accent;
    color: $txt;
  }

  &__label {
  }

  &__icon {
    width: 20px;
    height: 20px;
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
