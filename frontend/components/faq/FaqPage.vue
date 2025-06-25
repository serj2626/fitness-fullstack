<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsFAQDetailPage } from "~/assets/data/breadcrumbs.data";
import type { IFAQResponse } from "~/types";

const { $api } = useNuxtApp();
const isLoading = ref(false);
const currentPage = ref(1);
const faqItems = ref<IFAQResponse['results']>([]);
const hasMore = ref(true);

// Первоначальная загрузка
const { data: faqInfo } = await useAsyncData<IFAQResponse>(
  "faq-page-info",
  () => $api(api.gym.faq, { params: { page: currentPage.value } })
);

// Сохраняем первые результаты
if (faqInfo.value) {
  faqItems.value = faqInfo.value.results;
  hasMore.value = !!faqInfo.value.next; // Проверяем, есть ли еще страницы
}

// Функция для подгрузки новых данных
const loadMore = async () => {
  if (isLoading.value || !hasMore.value) return;

  isLoading.value = true;
  currentPage.value += 1;

  try {
    const response = await $api<IFAQResponse>(api.gym.faq, { 
      params: { page: currentPage.value } 
    });

    if (response) {
      faqItems.value = [...faqItems.value, ...response.results];
      hasMore.value = !!response.next; // Обновляем флаг наличия данных
    }
  } catch (error) {
    console.error('Ошибка при загрузке:', error);
  } finally {
    isLoading.value = false;
  }
};
</script>

<template>
  <div class="faq-page">
    <PagesTopSection
      title="Вопросы и ответы"
      description="Профессионалы, которые выжмут из тебя все соки"
    />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsFAQDetailPage" />
      <FaqContent v-if="faqItems.length" :faq-info="faqItems" />
      <LoadMoreObserver v-if="hasMore" @intersect="loadMore" />
    </div>
  </div>
</template>