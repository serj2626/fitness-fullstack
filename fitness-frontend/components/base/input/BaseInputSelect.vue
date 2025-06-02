<script setup>
const emit = defineEmits(["update:currentOption", "update:error"]);
const { options, currentOption, tabindex, error } = defineProps({
  options: {
    type: Array,
    default: () => [],
  },
  currentOption: {
    type: Object,
    default: () => ({}),
  },
  tabindex: {
    type: Number,
    default: 0,
  },
  error: {
    type: String,
    default: null,
  },
});

const filteredOptions = computed(() => {
  return options.filter((item) => item.slug !== currentOption.slug);
});

const opened = ref(false);

function optionHandler(option) {
  emit("update:currentOption", option);
  emit("update:error", null);
  closeHandler();
}
function toggleHandler() {
  opened.value = !opened.value;
}
function closeHandler() {
  opened.value = false;
}
</script>
<template>
  <div class="base-input-select" :tabindex="tabindex" @blur="closeHandler">
    <div
      class="base-input-select__handler"
      :class="{ 'base-input-select__handler_error': error }"
      @click="toggleHandler"
    >
      <span>
        {{ currentOption.title }}
      </span>
      <Icon
        class="base-input-select__handler-icon"
        :class="{ 'base-input-select__handler-svg_opened': opened }"
        name="arrow-down"
        filled
      />
    </div>
    <div
      class="base-input-select__items"
      :class="{ 'base-input-select__items_shown': opened }"
    >
      <div
        class="base-input-select__option"
        v-for="option of filteredOptions"
        :key="option.slug"
        @click="() => optionHandler(option)"
      >
        {{ option.title ? option.title : option.fcs }}
      </div>
    </div>
    <span v-if="error" class="base-input-select__error">
      {{ error }}
    </span>
  </div>
</template>

<style lang="scss" scoped>
.base-input-select {
  // @include txt_monrope(14px, 400, 19.6px, $txt_review);
  position: relative;
  width: 100%;

  &__handler {
    border: none;
    border-radius: 5px;
    padding: 14px 16px;
    background: $txt;
    color: $txt;
    cursor: pointer;
    user-select: none;

    &:hover {
      border: none;
    }

    &_error {
      outline: 1px solid $error;
    }

    &-icon {
      display: flex;
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      right: 32px;
      transition: transform 80ms ease;

      &_opened {
        transform: translateY(-50%) rotate(-180deg);
      }
    }
  }

  &__items {
    background-color: $txt;
    overflow: hidden;
    position: absolute;
    left: 0;
    right: 0;
    z-index: 2;
    display: none;
    border-bottom-right-radius: 5px;
    border-bottom-left-radius: 5px;

    &_shown {
      display: flex;
      flex-direction: column;
    }
  }

  &__option {
    width: 100%;
    cursor: pointer;
    padding-block: 10px;
    padding-left: 20px;
    user-select: none;
    border-bottom: 1px solid #01394323;
    // @include txt_monrope(14px, 400, 19.6px, $txt_review);

    &:hover {
      // background-color: $diamond_white;
    }
  }
  &__error {
    position: absolute;
    color: $error;
    opacity: 1;
    top: 100%;
    left: 14px;
    font-size: 12px;
    transition: opacity 0.3s ease;

    &::before {
      content: "*";
    }
  }
}
</style>
