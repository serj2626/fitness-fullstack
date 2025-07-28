<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsFAQDetailPage } from "~/assets/data/breadcrumbs.data";
import type { IFAQResponse } from "~/types";
import { useIntersectionObserver } from "@vueuse/core";

const { $api } = useNuxtApp();
const currentPage = ref(1);
const faqItems = ref<IFAQResponse["results"]>([]);
const hasMore = ref(true);

// Первоначальная загрузка
const { data: initialData } = await useAsyncData<IFAQResponse>(
  "faq-page-info",
  () => $api(api.gym.faq, { params: { page: currentPage.value } })
);

if (initialData.value) {
  faqItems.value = initialData.value.results;
  hasMore.value = !!initialData.value.next;
}

const observerTarget = ref<HTMLElement | null>(null);

useIntersectionObserver(observerTarget, async ([entry]) => {
  if (entry.isIntersecting && hasMore.value) {
    currentPage.value += 1;
    
    const { data: newData } = await useAsyncData<IFAQResponse>(
      `faq-page-info-${currentPage.value}`,
      () => $api(api.gym.faq, { params: { page: currentPage.value } })
    );
    
    if (newData.value) {
      faqItems.value = [...faqItems.value, ...newData.value.results];
      hasMore.value = !!newData.value.next;
    }
  }
});
</script>

<template>
  <div class="faq-page">
    <PagesTopSection title="Вопросы и ответы" />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsFAQDetailPage" />
      <FaqContent :faq-info="faqItems" />
      <div
        ref="observerTarget"
        class="observer-trigger"
        style="height: 1px; margin-top: 40px"
      />
    </div>
  </div>
</template>