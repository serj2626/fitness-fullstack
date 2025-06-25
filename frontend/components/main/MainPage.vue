<script lang="ts" setup>
import { api } from "~/api";
import type { IMainAbonementAPIResponse, IServicesResponse } from "~/types";
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

const { data: servicesInfo } = await useAsyncData<IServicesResponse[]>(
  "main-page-services-list-info",
  () => $api(api.gym.services)
);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection />
    <MainAbonementsSection v-if="abonementsInfo" :abonements="abonementsInfo" />
    <MainServicesSection v-if="servicesInfo" :services="servicesInfo" />
    <MainPoolSection />
    <BaseFormFeedback />
  </div>
</template>
