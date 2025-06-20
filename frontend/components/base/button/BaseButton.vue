<script lang="ts" setup>
interface IProps {
  label?: string;
  size?: "sm" | "md" | "lg";
  color?: string;
  type?: "submit" | "reset" | "button";
  disabled?: boolean;
}

const {
  label = "Button",
  size = "md",
  color = "#ffc451",
  type = "button",
  disabled = false,
} = defineProps<IProps>();
</script>
<template>
  <button
    :type="type"
    class="base-button"
    :class="{
      [`base-button_${size}`]: size,
      [`base-button_disabled`]: disabled,
    }"
  >
    {{ label }}
  </button>
</template>
<style lang="scss">
.base-button {
  font-size: 14px;
  padding: 8px 30px;
  border-radius: 4px;
  transition: all 0.3s ease-in;
  border: 2px solid v-bind(color);
  color: $header_link;

  &_sm {
    padding: 6px 12px;
  }
  &_md {
    padding: 8px 30px;
  }
  &_lg {
    padding: 15px 30px;
  }

  &:hover {
    background-color: v-bind(color);
    color: $txt;
  }
}
</style>
