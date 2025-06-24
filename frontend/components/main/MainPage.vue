<script lang="ts" setup>
import { api } from "~/api";
import type { IMainAbonementAPIResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: abonementsInfo } = await useAsyncData(
  "main-page-abonements-list-info",
  () => $api<IMainAbonementAPIResponse[]>(api.abonements.list),
  {
    transform: (data) => {
      return data.map((abonement) => {
        return {
          ...abonement,
          services: abonement.services.map((service) => service.title),
        };
      });
    },
  }
);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection />
    <MainAbonementsSection v-if="abonementsInfo" :abonements="abonementsInfo" />
    <MainServicesSection />
    <MainPoolSection />
    <!-- <MainCoachesSection />
    <MainReviewsSection /> -->
    <BaseFormFeedback />
  </div>
</template>
