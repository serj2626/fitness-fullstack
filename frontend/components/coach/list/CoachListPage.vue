<script setup lang="ts">
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";

import CoachListContent from "./CoachListContent.vue";

const coachesStore = useCoachesStore();
const { coaches, loading, error, activeCategory } = storeToRefs(coachesStore);

// Получаем filterCoaches напрямую из store, а не через storeToRefs
const filterCoaches = computed(() => coachesStore.filterCoaches);

const { pending } = await useAsyncData("coaches-list-init", async () => {
  await coachesStore.fetchAllCoaches();
  return true;
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
      <CoachListContent v-if="coaches" :coaches="filterCoaches" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
