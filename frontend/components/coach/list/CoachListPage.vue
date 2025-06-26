<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsCoachesPage } from "~/assets/data/breadcrumbs.data";
import type { ICoach, ICoachesListResponse } from "~/types";
import CoachListContent from "./CoachListContent.vue";

const { $api } = useNuxtApp();

const { data: coachesData } = await useAsyncData<ICoachesListResponse>(
  "coaches-list-page-info",
  () => $api(api.coaches.list)
);
</script>
<template>
  <div class="trainers-page">
    <PagesTopSection
      title="Наши тренеры"
      description="Профессионалы, которые выжмут из тебя все соки"
    />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsCoachesPage" />
      <CoachListContent :coaches="coachesData?.results as ICoach[]" />
    </div>
  </div>
</template>

<style scoped lang="scss">
.trainers-page {
  color: $txt;
}
</style>
