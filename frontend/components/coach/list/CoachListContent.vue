<script setup lang="ts">
import type { ICoach } from "~/types";
const coachesStore = useCoachesStore();
const { loading } = storeToRefs(coachesStore);

defineProps<{
  coaches: ICoach[] | null;
}>();
</script>
<template>
  <div class="coach-list-content">
    <BaseLoader
      v-if="loading"
      style="
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        z-index: 100;
      "
    />
    <!-- <CoachFilters class="coach-list-content__filters" /> -->
    <div class="coach-list-content__trainers">
      <CoachCard v-for="trainer in coaches" :key="trainer.id" :trainer />
    </div>
  </div>
</template>
<style scoped lang="scss">
.coach-list-content {
  position: relative;
  padding: 60px 0;
  min-height: 700px;

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
