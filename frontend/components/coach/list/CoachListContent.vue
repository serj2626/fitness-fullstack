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
    <div class="coach-list-content__trainers">
      <CoachCard
        v-for="(trainer, index) in coaches"
        :key="trainer.id"
        :trainer
        class="coach-list-content__trainers-card"
        :style="{ animationDuration: `${(index + 0.5) * 0.2}s` }"
      />
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
    &-card {
      width: 100%;
      animation-name: zal;
      animation-timing-function: ease-in-out;
      animation-iteration-count: 1;
    }
  }
}
@keyframes zal {
  0% {
    opacity: 0;
    scale: 0.9;
  }
  100% {
    opacity: 1;
    scale: 1;
  }
}
</style>
