<script lang="ts" setup>
import { api } from "~/api";
import type { IPost, IAbonement } from "~/types";

const { $api } = useNuxtApp();

const { data: abonements } = await useAsyncData<IAbonement[]>(
  "main-page-abonements-info",
  () => $api(api.abonements.list),
);
const { data: lastPosts } = await useAsyncData<IPost[]>(
  "main-page-last-posts-info",
  () => $api(api.posts.last),
);
// const [
//   { data: servicesInfo },
//   { data: postsLast },
//   { data: advantagesInfo },
//   { data: equipmentList },
// ] = await Promise.all([
//   useAsyncData("main-page-services-list-info", () =>
//     $api<IServicesResponse[]>(api.gym.services)
//   ),
//   useAsyncData("main-page-posts-last-info", () =>
//     $api<IPost[]>(api.posts.last)
//   ),
//   useAsyncData("main-page-advantages-list-info", () =>
//     $api<IAdvantageResponse[]>(api.gym.advantages)
//   ),
//   useAsyncData("main-page-equipment-list",
//     () => $api(api.gym.equipment), {
//     transform: (data: IEequipmentResponse[]) =>
//       Object.fromEntries(data.map((item) => [item.title, item])),
//   }),
// ]);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection client:visible />
    <MainFirstSection client:visible />
    <MainAbonementsSection  :abonements="abonements" />
    <MainAdvantagesSection />

    <!--  

    <MainServicesSection v-if="servicesInfo" :services="servicesInfo" />

    <LazyMainPostSection v-if="postsLast" :posts="postsLast" />

    <LazyMainEquipmentSection
      v-if="equipmentList"
      :data="equipmentList"
      client:visible
    /> -->

    <LazyMainPoolSection client:visible />
    <BaseFormFeedback client:visible />
  </div>
</template>
