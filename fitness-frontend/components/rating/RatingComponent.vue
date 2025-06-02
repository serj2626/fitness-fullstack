<script lang="ts" setup>
</script>
<template>
  <div class="rating">
    <svg
      class="rating__star rating__star--active"
      xmlns="http://www.w3.org/2000/svg"
      fill="currentColor"
      viewBox="0 0 24 24"
      width="30"
      height="30"
    >
      <path
        fill-rule="evenodd"
        d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        clip-rule="evenodd"
      />
    </svg>
    <svg
      class="rating__star rating__star--active"
      xmlns="http://www.w3.org/2000/svg"
      fill="currentColor"
      viewBox="0 0 24 24"
      width="30"
      height="30"
    >
      <path
        fill-rule="evenodd"
        d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        clip-rule="evenodd"
      />
    </svg>
    <svg
      class="rating__star rating__star--active"
      xmlns="http://www.w3.org/2000/svg"
      fill="currentColor"
      viewBox="0 0 24 24"
      width="30"
      height="30"
    >
      <path
        fill-rule="evenodd"
        d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        clip-rule="evenodd"
      />
    </svg>
    <svg
      class="rating__star rating__star--active"
      xmlns="http://www.w3.org/2000/svg"
      fill="currentColor"
      viewBox="0 0 24 24"
      width="30"
      height="30"
    >
      <path
        fill-rule="evenodd"
        d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"
        clip-rule="evenodd"
      />
    </svg>
    <svg
      class="rating__star"
      xmlns="http://www.w3.org/2000/svg"
      fill="currentColor"
      viewBox="0 0 24 24"
      width="30"
      height="30"
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

  &__star {
    font-size: 24px;
    color: #d1d5db; // серый цвет для неактивной звезды

    &--active {
      color: #facc15; // желтый цвет для активной звезды
    }
  }
}
</style>
