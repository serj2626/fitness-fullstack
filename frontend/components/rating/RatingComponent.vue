<script lang="ts" setup>
const {
  modelValue,
  editable,
  size = "sm",
} = defineProps<{
  modelValue: number | string;
  editable?: boolean;
  size?: "sm" | "md" | "lg" | "xl";
}>();

const emit = defineEmits<{
  (e: "update:modelValue", value: number): void;
}>();

function setRating(value: number) {
  if (!editable) return;
  emit("update:modelValue", value);
}
const hoverValue = ref(0);

const currentWidthHeight = computed(() => {
  if (size === "sm") {
    return 20;
  } else if (size === "md") {
    return 30;
  } else if (size === "lg") {
    return 40;
  }
  return 45;
});
</script>

<template>
  <div class="rating" :class="{ 'rating--editable': editable }">
    <svg
      v-for="star in 5"
      :key="star"
      class="rating__star"
      :class="{
        'rating__star--active': Number(modelValue) >= Number(star),
        'rating__star--hover': editable && hoverValue >= star,
      }"
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      :width="currentWidthHeight"
      :height="currentWidthHeight"
      fill="currentColor"
      @mouseenter="editable && (hoverValue = star)"
      @mouseleave="editable && (hoverValue = 0)"
      @click="setRating(star)"
    >
      <path
        fill-rule="evenodd"
        d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        clip-rule="evenodd"
      />
    </svg>
  </div>
</template>

<style scoped lang="scss">
.rating {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 4px;

  &--editable &__star {
    cursor: pointer;
  }

  &__star {
    color: #d1d5db;
    transition: color 0.2s;

    &--active {
      color: #facc15;
    }

    &--hover {
      color: #fde047; // более светлый жёлтый для предпросмотра
    }
  }
}
</style>
