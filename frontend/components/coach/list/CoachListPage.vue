<script setup lang="ts">
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import { useCoachesStore } from "~/stores/coaches";
import { useIntersectionObserver } from "@vueuse/core";
import { api } from "~/api";

const { $api } = useNuxtApp();
// const coachesStore = useCoachesStore();
// const { coaches, loading, next } = storeToRefs(coachesStore);

// const { pending } = await useAsyncData("coaches", () =>
//   coachesStore.fetchAllCoaches(),
// );

// const observerTarget = ref<HTMLElement | null>(null);

// useIntersectionObserver(observerTarget, async ([entry]) => {
//   if (entry.isIntersecting && next.value && !loading.value) {
//     await coachesStore.fetchAllCoaches(next.value);
//   }
// });

const { data: coaches, pending } = useAsyncData("coaches", () => $api(api.coaches.list));
</script>
<template>
  <div class="trainers-page">
    <PagesTopSection
      title="Наши тренеры"
      description="Профессионалы, которые выжмут из тебя все соки"
    />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsCoachesPage" />
      <BaseLoader v-if="pending" />
      {{ coaches }}
      <!-- <CoachListContent v-if="coaches" :coaches="coaches" />
      <div
        ref="observerTarget"
        class="observer-trigger"
        style="height: 1px; margin-top: 140px"
      /> -->
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
