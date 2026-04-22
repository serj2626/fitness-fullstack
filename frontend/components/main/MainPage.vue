<script lang="ts" setup>
import { api } from "~/api";
import type { IPost, IAbonement, ICoach } from "~/types";

const { $api } = useNuxtApp();

const { data: abonements } = await useAsyncData<IAbonement[]>(
  "main-page-abonements-info",
  () => $api(api.abonements.list),
);
const { data: lastPosts } = await useLazyAsyncData<IPost[]>(
  "main-page-last-posts-info",
  () => $api(api.posts.last),
);
const { data: lastCoaches } = await useLazyAsyncData<ICoach[]>(
  "main-page-last-coaches-info",
  () => $api(api.coaches.last),
);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection client:visible />
    <MainFirstSection client:visible />
    <MainAbonementsSection v-if="abonements" :abonements="abonements" />
    <MainAdvantagesSection />
    <LazyMainPostSection v-if="lastPosts" :posts="lastPosts" />
    <LazyMainCoachesSection v-if="lastCoaches" :coaches="lastCoaches" />
    <LazyMainPoolSection client:visible />
    <LazyBaseFormFeedback client:visible />
  </div>
</template>
