<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsFAQDetailPage } from "~/assets/data/breadcrumbs.data";
import type { IFAQResponse } from "~/types";
const { $api } = useNuxtApp();

const { data: faqInfo } = await useAsyncData<IFAQResponse>(
  "faq-page-info",
  () => $api(api.gym.faq)
);
</script>
<template>
  <div class="faq-page">
    <PagesTopSection
      title="Вопросы и ответы"
      description="Профессионалы, которые выжмут из тебя все соки"
    />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsFAQDetailPage" />
      <FaqContent v-if="faqInfo" :faq-info="faqInfo.results" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.faq-page {
}
</style>
