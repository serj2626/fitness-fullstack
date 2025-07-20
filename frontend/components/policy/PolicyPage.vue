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
    title: "Политика конфиденциальности",
    url: "/policy",
  },
]);

const { data: policyInfo } = await useAsyncData<ILegalResponse>(
  "policy-page-info",
  () => $api(api.legal.policy)
);
</script>
<template>
  <div class="policy-page">
    <PagesTopSection
      :title="policyInfo?.title || 'Политика конфиденциальности'"
    />
    <div class="container">
      <BaseBreadCrumbs class="policy-page__breadcrumbs" :breadcrumbs />
      <BaseWysiwyg v-if="policyInfo?.content" :html="policyInfo?.content" />
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
