<script setup lang="ts">
import type { ICoach } from "~/types";
import CoachFilters from "../CoachFilters.vue";

defineProps<{
  coaches: ICoach[] | null;
}>();

const scroll = ref(0);
function handleScroll() {
  scroll.value = window.scrollY;
}

const getScrollClass = computed(() => {
  return scroll.value > 220 ? true : false;
});

onMounted(() => {
  window.addEventListener("scroll", handleScroll);
});

onUnmounted(() => {
  window.removeEventListener("scroll", handleScroll);
});
</script>
<template>
  <div class="coach-list-content">
    <CoachFilters
      class="coach-list-content__filters"
      :class="{ 'coach-list-content__filters_scrolled': getScrollClass }"
    />
    <div class="coach-list-content__trainers">
      <TrainerCard v-for="trainer in coaches" :key="trainer.id" :trainer />
    </div>
  </div>
</template>
<style scoped lang="scss">
.coach-list-content {
  padding: 60px 0;
  &__filters {
    position: sticky;
    top: 100px;
    z-index: 10;
    transition: all 0.8s ease-in;
    &_scrolled {
      background-color: $txt;
      padding-block: 30px;
      border-radius: 5px;
    }
  }
  &__trainers {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;

    @media (max-width: $tablet) {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    }

    @media (max-width: $mobile) {
      grid-template-columns: 1fr;
    }
  }
}
</style>
