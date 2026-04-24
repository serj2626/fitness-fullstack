<script setup lang="ts">
interface Props {
  modelValue?: boolean;
  activeColor?: string; // цвет активного состояния (фон)
  inactiveColor?: string; // цвет неактивного состояния (фон)
  size?: "sm" | "md" | "lg";
  disabled?: boolean;
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: false,
  activeColor: "#2ecc71",
  inactiveColor: "#bdc3c7",
  size: "lg",
  disabled: false,
});

const emit = defineEmits<{
  (e: "update:modelValue", value: boolean): void;
}>();

const toggle = () => {
  if (props.disabled) return;
  emit("update:modelValue", !props.modelValue);
};
</script>

<template>
  <label
    class="base-toggle"
    :class="[
      `base-toggle--${size}`,
      { 'base-toggle--active': modelValue, 'base-toggle--disabled': disabled },
    ]"
    :style="{
      '--active-color': activeColor,
      '--inactive-color': inactiveColor,
    }"
  >
    <input
      type="checkbox"
      :checked="modelValue"
      :disabled="disabled"
      class="base-toggle__input"
      @change="toggle"
    />
    <span class="base-toggle__slider"></span>
    <span class="base-toggle__label">
      <slot>{{ modelValue ? "Вкл" : "Выкл" }}</slot>
    </span>
  </label>
</template>

<style scoped lang="scss">
.base-toggle {
  display: inline-flex;
  align-items: center;
  cursor: pointer;
  user-select: none;
  gap: 0.75rem;

  &--disabled {
    opacity: 0.5;
    cursor: not-allowed;
  }

  // размеры
  &--sm {
    .base-toggle__slider {
      width: 36px;
      height: 20px;
      &::before {
        width: 16px;
        height: 16px;
      }
    }
    &.base-toggle--active .base-toggle__slider::before {
      transform: translateX(16px);
    }
  }
  &--md {
    .base-toggle__slider {
      width: 48px;
      height: 26px;
      &::before {
        width: 22px;
        height: 22px;
      }
    }
    &.base-toggle--active .base-toggle__slider::before {
      transform: translateX(22px);
    }
  }
  &--lg {
    .base-toggle__slider {
      width: 60px;
      height: 32px;
      &::before {
        width: 28px;
        height: 28px;
      }
    }
    &.base-toggle--active .base-toggle__slider::before {
      transform: translateX(28px);
    }
  }

  // ползунок
  &__slider {
    position: relative;
    display: inline-block;
    background-color: var(--inactive-color);
    border-radius: 34px;
    transition: background-color 0.2s ease;
    flex-shrink: 0;

    &::before {
      content: "";
      position: absolute;
      top: 2px;
      left: 2px;
      background-color: rgb(255, 255, 255);
      border-radius: 50%;
      transition: transform 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
  }

  &--active &__slider {
    background-color: var(--active-color);
  }

  &__input {
    position: absolute;
    opacity: 0;
    width: 0;
    height: 0;
    pointer-events: none;
  }

  &__label {
    font-size: 1rem;
    line-height: 1;
  }
}
</style>
