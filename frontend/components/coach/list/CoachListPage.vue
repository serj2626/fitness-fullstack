<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import type { ICoachCategory } from "~/types";
import { useIntersectionObserver } from "@vueuse/core";

const coachesStore = useCoachesStore();
const { next, coaches, activeCategory, loading } = storeToRefs(coachesStore);

const { $api } = useNuxtApp();

const observerTarget = ref<HTMLElement | null>(null);

const { data: categories } = useAsyncData<ICoachCategory[]>(
  "coaches-list-page-categories",
  () => $api(api.categories.list),
);

await useAsyncData("coaches-list-page", async () => {
  await coachesStore.fetchAllCoaches();
  return coachesStore.coaches;
});

onMounted(() => {
  useIntersectionObserver(
    observerTarget,
    async ([entry]) => {
      if (entry.isIntersecting && next.value && !loading.value) {
        await coachesStore.fetchAllCoaches(next.value as number, 6);
      }
    },
    {
      threshold: 0.5, // при 50% видимости
      rootMargin: "300px", // дополнительный отступ
    },
  );
});
onUnmounted(() => {
  coachesStore.reset();
})
</script>
<template>
  <div class="trainers-page">
    <PagesTopSection
      title="Наши тренеры"
      description="Профессионалы, которые выжмут из тебя все соки"
    />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsCoachesPage" />
      <CoachListCategories
        v-if="categories"
        v-model="activeCategory"
        :categories="categories"
        style="margin-top: 15px"
      />
      <CoachListContent :coaches="coaches" />
      <div
        ref="observerTarget"
        class="observer-trigger"
        style="height: 1px; margin-top: 140px"
      />
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
