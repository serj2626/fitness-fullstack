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
const errorValue = defineModel("error");

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
  <label
    class="base-input"
    :class="{ 'base-input_isfocused': isFocused, 'base-input_error': error }"
  >
    <input
      ref="inputRef"
      v-model="inputValue"
      v-maska="maskOptions"
      :type="currentType"
      class="base-input__input"
      @focus="handleFocus"
      @blur="handleBlur"
    />
    <span v-if="!inputValue && !error" class="base-input__placeholder">
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
  border: 1px solid #6e666688;
  border-radius: 10px;
  transition: outline 0.6s ease-in;

  &_isfocused {
    outline: 1px solid $accent;
    .base-input__placeholder {
      opacity: 0;
      scale: 0.1;
    }
  }
  &_error {
    outline: 1px solid $red;
  }

  &__placeholder {
    position: absolute;
    color: $white;
    padding-left: 15px;
    transition: all 0.5s ease-in-out;
  }
  &__error {
    position: absolute;
    color: $red;
    padding-left: 15px;
    font-size: 16px;
  }

  &__input {
    padding: 15px 19px 15px 15px;
    cursor: auto;
    border-radius: 5px;
    color: $white;
    transition: outline $desctop_wide;

    // &:focus {
    //   .base-input {
    //     outline: 1px solid $accent;
    //   }
    // }
  }

  &__icon {
    position: absolute;
    top: 50%;
    right: 10px;
    transform: translateY(-50%);
    background-color: $white;
    opacity: 0.7;
    cursor: pointer;
  }
}
</style>
