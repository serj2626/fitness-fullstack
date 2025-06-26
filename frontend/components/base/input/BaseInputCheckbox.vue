<script lang="ts" setup>
const agreeValue = defineModel("agreeValue");
const agreeError = defineModel("agreeError");
</script>
<template>
  <div class="base-input-checkbox">
    <input
      id="check"
      v-model="agreeValue"
      type="checkbox"
      class="base-input-checkbox__element"
    />
    <label for="check" class="base-input-checkbox__label">
      <slot />
    </label>
  </div>
</template>
<style lang="scss" scoped>
.base-input-checkbox {
  display: inline-flex;
  align-items: center;
  margin-bottom: 10px;
  gap: 8px;
  font-weight: 400;
  font-size: 15px;
  &__element {
  }
  &__label {
  }
}
</style>
