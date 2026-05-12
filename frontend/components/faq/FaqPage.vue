<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsFAQDetailPage } from "~/assets/data/breadcrumbs.data";
import type { IQuestion } from "~/types";

const { $api } = useNuxtApp();

const { data: faqData } = await useAsyncData<IQuestion[]>("faq-page-info", () =>
  $api(api.contacts.faq),
);
</script>

<template>
  <div class="faq-page">
    <PagesTopSection title="Вопросы и ответы" />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsFAQDetailPage" />
      <FaqContent :faq-info="faqData" />
    </div>
  </div>
</template>
