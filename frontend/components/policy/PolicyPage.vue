<script lang="ts" setup>
import { api } from "~/api";
import { policyHtml } from "~/assets/data/moke.data";
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
    <h1 class="policy-page__title">
      {{ policyInfo?.title || "Политика конфиденциальности" }}
    </h1>
    <div class="container">
      <BaseBreadCrumbs class="policy-page__breadcrumbs" :breadcrumbs />
      <BaseWysiwyg v-if="policyInfo?.content" :html="policyInfo?.content" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.policy-page {
  padding-block: 150px 50px;

  &__title {
    @include title_by_page;
  }

  &__breadcrumbs {
    margin-bottom: 50px;
  }
}
</style>
