<script lang="ts" setup>
import { policyHtml } from "~/assets/data/moke.data";
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
</script>
<template>
  <div class="policy-page">
    <h1 class="policy-page__title">Политика конфиденциальности</h1>
    <div class="container">
      <BaseBreadCrumbs class="policy-page__breadcrumbs" :breadcrumbs />
      <BaseWysiwyg class="policy-page__wysiwyg" :html="policyHtml" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.policy-page {
  padding-block: 150px 50px;

  &__title {
    text-align: center;
    font-weight: 700;
    font-size: 36px;
    color: $accent;
    text-transform: uppercase;
    letter-spacing: 2px;
    margin-bottom: 30px;
  }

  &__breadcrumbs {
    margin-bottom: 50px;
  }

  &__wysiwyg {
  }
}
</style>
