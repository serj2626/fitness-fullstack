<script setup>
defineProps({
  error: {
    type: Object,
    default: null,
    required: false,
  },
  errorText: {
    type: String,
    default: null,
  },
});
</script>
<template>
  <div class="error-component">
    <div class="error-component__inner container">
      {{ errorText }}
    </div>

    <pre v-if="$config.public.isDebug" class="error-component__debug">
      {{ error }}
    </pre>
  </div>
</template>
<style lang="scss" scoped>
.error-component {
  &__inner {
  }
  &__debug {
    position: absolute;
    top: 100px;
    left: 0;
    background-color: #fff;
  }
}
</style>
