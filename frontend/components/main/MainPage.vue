<script lang="ts" setup>
import { api } from "~/api";
import type {
  IPost,
  IServicesResponse,
  IAdvantageResponse,
  IEequipmentResponse,
} from "~/types";
const { $api } = useNuxtApp();

const { data: abonementsInfo } = useAbonements();

const [
  { data: servicesInfo },
  { data: postsLast },
  { data: advantagesInfo },
  { data: equipmentList },
] = await Promise.all([
  useAsyncData("main-page-services-list-info", () =>
    $api<IServicesResponse[]>(api.gym.services)
  ),
  useAsyncData("main-page-posts-last-info", () =>
    $api<IPost[]>(api.posts.last)
  ),
  useAsyncData("main-page-advantages-list-info", () =>
    $api<IAdvantageResponse[]>(api.gym.advantages)
  ),
  useAsyncData("main-page-equipment-list", () => $api(api.gym.equipment), {
    transform: (data: IEequipmentResponse[]) =>
      Object.fromEntries(data.map((item) => [item.title, item])),
  }),
]);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection />
    <MainFirstSection />

    <MainAdvantagesSection v-if="advantagesInfo" :advantages="advantagesInfo" />

    <MainAbonementsSection v-if="abonementsInfo" :abonements="abonementsInfo" />

    <MainServicesSection v-if="servicesInfo" :services="servicesInfo" />

    <LazyMainPostSection v-if="postsLast" :posts="postsLast" />

    <MainEquipmentSection
      v-if="equipmentList"
      :data="equipmentList"
      client:visible
    />

    <LazyMainPoolSection />
    <BaseFormFeedback client:visible />
  </div>
</template>
