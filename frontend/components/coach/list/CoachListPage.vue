<script setup lang="ts">
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import { useCoachesStore } from "~/stores/coaches";
import { useIntersectionObserver } from "@vueuse/core";

const coachesStore = useCoachesStore();
const { coaches, loading, next } = storeToRefs(coachesStore);

const { pending } = await useAsyncData("coaches", () => coachesStore.fetchAllCoaches());


const observerTarget = ref<HTMLElement | null>(null);

useIntersectionObserver(observerTarget, async ([entry]) => {
  if (entry.isIntersecting && next.value && !loading.value) {
    await coachesStore.fetchAllCoaches(next.value);
  }
});
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
      <CoachListContent v-if="coaches" :coaches="coaches" />
      <div
        ref="observerTarget"
        class="observer-trigger"
        style="height: 1px; margin-top: 40px"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
