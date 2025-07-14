<script lang="ts" setup>
import { api } from "~/api";
import type { IPost, IServicesResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: abonementsInfo } = useAbonements();

const { data: servicesInfo } = await useAsyncData<IServicesResponse[]>(
  "main-page-services-list-info",
  () => $api(api.gym.services)
);

const { data: postsLast } = await useAsyncData(
  "main-page-posts-last-info",
  () => $api(api.posts.last)
);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection />
    <MainAdvantagesSection />
    <MainAbonementsSection v-if="abonementsInfo" :abonements="abonementsInfo" />
    <MainServicesSection v-if="servicesInfo" :services="servicesInfo" />
    <MainPostSection :posts="postsLast as IPost[]" />
    <MainPoolSection />
    <BaseFormFeedback />
  </div>
</template>
