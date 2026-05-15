<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import type { ICoachCategory } from "~/types";
import { useIntersectionObserver, useDebounceFn } from "@vueuse/core";

const coachesStore = useCoachesStore();
const { next, coaches, activeCategory, loading } = storeToRefs(coachesStore);

const { $api } = useNuxtApp();

const observerTarget = ref<HTMLElement | null>(null);

useAsyncData("coaches-list-page", async () => {
  await coachesStore.fetchAllCoaches();
  return coachesStore.coaches;
});

const { data: categories } = useAsyncData<ICoachCategory[]>(
  "coaches-list-page-categories",
  () => $api(api.categories.list),
  {
    server: true,
  },
);

watch(
  activeCategory,
  useDebounceFn(async () => {
    await coachesStore.fetchAllCoaches(1, 6);
  }, 300),
);

onMounted(() => {
  useIntersectionObserver(
    observerTarget,
    async ([entry]) => {
      if (entry.isIntersecting && next.value && !loading.value) {
        await coachesStore.fetchAllCoaches(next.value as number, 6);
      }
    },
    {
      threshold: 0.1, // при 10% видимости
      rootMargin: "300px", // дополнительный отступ
    },
  );
});
onUnmounted(() => {
  coachesStore.reset();
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
      <div style="color: wheat">
        {{ activeCategory }}
      </div>

      <template v-if="coaches && coaches.length > 0">
        <CoachListCategories
          v-model="activeCategory"
          :categories="categories || []"
        />

        <CoachListContent :coaches="coaches" />

        <div
          ref="observerTarget"
          class="observer-trigger"
          style="height: 1px; margin-top: 140px"
        />
      </template>
      <BaseEmpty v-else text="Тренеры не найдены" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
