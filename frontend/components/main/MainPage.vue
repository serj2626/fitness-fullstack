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

const { data: servicesInfo } = await useAsyncData<IServicesResponse[]>(
  "main-page-services-list-info",
  () => $api(api.gym.services)
);

const { data: postsLast } = await useAsyncData(
  "main-page-posts-last-info",
  () => $api(api.posts.last)
);

const { data: advantagesInfo } = await useAsyncData<IAdvantageResponse[]>(
  "main-page-advantages-list-info",
  () => $api(api.gym.advantages)
);

const { data: equipmentList } = useAsyncData(
  "main-page-equipment-list",
  () => $api<IEequipmentResponse[]>(api.gym.equipment),
  {
    transform: (data: IEequipmentResponse[]) => {
      const res: Record<string, IEequipmentResponse> = {};
      for (const item of data) {
        res[item.title] = item;
      }
      return res;
    },
  }
);
</script>
<template>
  <div>
    <MainVideoSection />
    <MainAboutSection />
    <MainFirstSection />
    

    <ClientOnly hydrate-on-visible>
      <MainAdvantagesSection
        v-if="advantagesInfo"
        :advantages="advantagesInfo"
      />
    </ClientOnly>

    <ClientOnly hydrate-on-visible>
      <MainAbonementsSection
        v-if="abonementsInfo"
        :abonements="abonementsInfo"
      />
    </ClientOnly>

    <ClientOnly hydrate-on-visible>
      <MainServicesSection v-if="servicesInfo" :services="servicesInfo" />
    </ClientOnly>
    <ClientOnly hydrate-on-visible>
      <MainPostSection v-if="postsLast" :posts="postsLast as IPost[]" />
    </ClientOnly>

    <ClientOnly hydrate-on-visible>
      <MainEquipmentSection v-if="equipmentList" :data="equipmentList" />
    </ClientOnly>

    <MainPoolSection />
    <BaseFormFeedback />
  </div>
</template>
