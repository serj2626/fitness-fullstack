<script setup lang="ts">
const value = defineModel<boolean>();
</script>
<template>
  <span class="base-input-checkbox">
    <input v-model="value" type="checkbox" class="base-input-checkbox__input" />
    <span class="base-input-checkbox__label">
      <slot> Отправить анонимно </slot>
    </span>
  </span>
</template>
<style scoped lang="scss">
.base-input-checkbox {
  display: flex;
  align-items: center;
  gap: 8px;
  color: $white;
  font-size: 0.9rem;

  &__input {
    appearance: none;
    -webkit-appearance: none; /* для Safari */

    width: 20px;
    height: 20px;
    border: 2px solid #ccc;
    border-radius: 4px;
    background: $white;
    cursor: pointer;
    transition: 0.1s ease;

    /* выравнивание с текстом, если нужно */
    vertical-align: middle;
    margin: 0;

    &:checked {
      background-color: $accent;
      border-color: $accent;
      position: relative;
    }

    /* Рисуем галочку через псевдоэлемент */
    &:checked::before {
      content: "✓";
      display: block;
      text-align: center;
      color: $txt;
      position: absolute;
      top: 50%;
      left: 50%;
      transform: translate(-50%, -50%);
    }
  }
}
</style>
