<script setup lang="ts">
interface IInputProps {
  placeholder?: string;
  error?: string;
}

const inputValue = defineModel<string | number>('inputValue');

defineProps<IInputProps>();
</script>
<template>
  <label class="base-input-text-area">
    <textarea
      v-model="inputValue"
      :class="{ 'base-input-text-area__input--error': error }"
      class="base-input-text-area__input"
    />
    <span v-if="!inputValue" class="base-input-text-area__placeholder">{{
      placeholder
    }}</span>
    <small v-if="error" class="base-input-text-area__error">{{ error }}</small>
  </label>
</template>

<style lang="scss" scoped>
.base-input-text-area__input:focus {
  .base-input-text-area__placeholder {
    left: 20px;
  }
}
.base-input-text-area {
  position: relative;
  display: flex;
  flex-direction: column;
  gap: 5px;
  width: 100%;
  background-color: #323232;
  border: 1px solid #323232;

  &__placeholder {
    position: absolute;
    left: 20px;
    top: 20px;
    color: $white;
  }

  &__input {
    resize: vertical;
    border: none;
    background-color: transparent;
    padding: 16px 20px;
    width: 100%;
    height: 200px;
    color: $white;

    box-shadow: 10px 14px 20px  rgba(252, 252, 252, 0.469);
    border-radius: 5px;

    &:focus {
      outline: none;
    }

    // &--error {
    //   border-bottom: 1px solid $error;
    // }
  }

  &__error {
    color: $error;
  }
}
</style>