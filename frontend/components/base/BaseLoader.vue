<script lang="ts" setup>
const {
  color = "#ffc451",
  bgColor = "rgba(255, 255, 255, 0.3)",
  size = "sm",
} = defineProps<{
  color?: string;
  bgColor?: string;
  size?: "sm" | "md" | "lg" | "xl";
}>();
</script>
<template>
  <div class="base-loader" role="status">
    <span class="loader" :class="`loader--${size}`" />
    <span class="visually-hidden">Загрузка...</span>
  </div>
</template>

<style scoped lang="scss">
.base-loader {
  position: absolute;
  top: 10%;
  left: 50%;
  z-index: 100;
  transform: translateX(-50%);
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 2rem;
}

.loader {
  border: 1px solid v-bind(bgColor);
  border-top-color: v-bind(color);
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
  &--sm {
    width: 40px;
    height: 40px;
    border-width: 4px;
  }
  &--md {
    width: 50px;
    height: 50px;
    border-width: 5px;
  }
  &--lg {
    width: 60px;
    height: 60px;
    border-width: 6px;
  }
  &--xl {
    width: 80px;
    height: 80px;
    border-width: 8px;
  }
}

.visually-hidden {
  position: absolute;
  width: 1px;
  height: 1px;
  margin: -1px;
  padding: 0;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  border: 0;
}

@keyframes spin {
  to {
    transform: rotate(360deg);
  }
}
</style>
