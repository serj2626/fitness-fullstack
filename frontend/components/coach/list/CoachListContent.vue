<script setup lang="ts">
import type { ICoach } from "~/types";

defineProps<{
  coaches: ICoach[] | null;
}>();
</script>
<template>
  <div class="coach-list-content">
    <!-- <CoachFilters class="coach-list-content__filters" /> -->
    <div class="coach-list-content__trainers">
      <TrainerCard v-for="trainer in coaches" :key="trainer.id" :trainer />
    </div>
  </div>
</template>
<style scoped lang="scss">
.coach-list-content {
  position: relative;
  padding: 60px 0;
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
