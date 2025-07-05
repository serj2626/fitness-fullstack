<script setup lang="ts">
defineProps<{
  error?: string;
  text?: string;
}>();

const agree = defineModel<boolean>("agreeValue");

// const emit = defineEmits(["update:modelValue"]);
</script>

<template>
  <label class="base-input-checkbox">
    <input
      type="checkbox"
      class="base-input-checkbox__input"
      :checked="agree"
      @change="agree = $event.target.checked"
    />

    <p  class="base-input-checkbox__text">
      Согласен на
      <NuxtLink class="base-input-checkbox__link">
        обработку своих персональных данных
      </NuxtLink>
    </p>

    <div v-if="error && !agree" class="base-input-checkbox__error">
      {{ error }}
    </div>
  </label>
</template>

<style scoped lang="scss">
.base-input-checkbox {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 20px;

  &__input {
    flex-shrink: 0;
  }

  &__text {
    color: white;

    & .base-input-checkbox__link {
      color: #ffc551c4;
      cursor: pointer;
      text-decoration: underline;
    }
  }

  &__error {
    color: red;
    font-size: 14px;
    font-weight: 600;
    display: block;
  }
}
</style>
