<script setup lang="ts">
import type { MaskInputOptions } from "maska";
import { HeroIcons } from "~/assets/icons/types/hero-icons";

const inputRef = ref<HTMLInputElement | null>(null);
const isFocused = ref(false);

const handleFocus = () => {
  isFocused.value = true;
};

const handleBlur = () => {
  isFocused.value = false;
};

type TInputTypes =
  | "button"
  | "checkbox"
  | "color"
  | "date"
  | "datetime-local"
  | "email"
  | "file"
  | "hidden"
  | "image"
  | "month"
  | "number"
  | "password"
  | "radio"
  | "range"
  | "reset"
  | "search"
  | "submit"
  | "tel"
  | "text"
  | "time"
  | "url"
  | "week";

interface IInputProps {
  placeholder?: string;
  error?: string;
  maskOptions?: MaskInputOptions;
  type?: TInputTypes;
}

const inputValue = defineModel("inputValue");

const props = defineProps<IInputProps>();

const showPassword = ref(false);

const currentType = computed(() => {
  if (props.type === "password" && showPassword.value) {
    return "text";
  }
  return props.type;
});
</script>
<template>
  <label class="base-input" :class="{ 'base-input_isfocused': isFocused }">
    <input
      ref="inputRef"
      v-model="inputValue"
      v-maska="maskOptions"
      :class="{ 'base-input__input_error': error }"
      :type="currentType"
      @focus="handleFocus"
      @blur="handleBlur"
      class="base-input__input"
    />
    <span v-if="!inputValue" class="base-input__placeholder">
      {{ placeholder }}</span
    >
    <small v-if="error" class="base-input__error">
      {{ error }}
    </small>
    <Icon
      v-if="type === 'password'"
      :name="showPassword ? HeroIcons.EYE_CLOSE : HeroIcons.EYE"
      size="20"
      class="base-input__icon"
      @click="showPassword = !showPassword"
    />
  </label>
</template>
<style lang="scss" scoped>
.base-input {
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  gap: 5px;
  background-color: #323232;
  border: 1px solid #323232;
  border-radius: 10px;
  transition: outline 1.1s ease-in;
  padding: 8px 30px;

  &_isfocused {
    outline: 1px solid $accent;
  }

  &__placeholder {
    position: absolute;
    color: $white;
    padding-left: 11px;
  }

  &__input {
    padding: 9px 19px 9px 11px;
    cursor: auto;
    border-radius: 5px;
    color: $white;
    transition: outline $desctop_wide;

    &:focus {
      .base-input {
        outline: 1px solid $accent;
      }
    }

    &_error {
      border-bottom: 1px solid $error;
    }
  }

  &__icon {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    background-color: $txt;
    opacity: 0.7;
    cursor: pointer;
  }

  &__error {
    color: $error;
  }
}
</style>
