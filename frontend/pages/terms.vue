<script lang="ts" setup>
import { api } from "~/api";
import type { ILegalResponse } from "~/types";

const { $api } = useNuxtApp();
const breadcrumbs = ref([
  {
    title: "Главная",
    url: "/",
  },
  {
    title: "Пользовательское соглашение",
    url: "/terms",
  },
]);

const { data: termsInfo } = await useAsyncData<ILegalResponse>(
  "policy-page-info",
  () => $api(api.contacts.terms)
);
</script>
<template>
  <div class="policy-page">
    <PagesTopSection
      :title="termsInfo?.title || 'Пользовательское соглашение'"
    />
    <div class="container">
      <BaseBreadCrumbs class="policy-page__breadcrumbs" :breadcrumbs />
      <BaseWysiwyg v-if="termsInfo?.content" :html="termsInfo?.content" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.policy-page {
  &__title {
    @include title_by_page;
  }

  &__breadcrumbs {
    margin-bottom: 50px;
  }
}
</style>
