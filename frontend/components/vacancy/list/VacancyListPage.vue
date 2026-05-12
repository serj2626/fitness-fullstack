<script setup lang="ts">
import { api } from "~/api";
import type { IVacancy } from "~/types";
const { $api } = useNuxtApp();

const { data: vacanciesData, pending } = await useAsyncData<IVacancy[]>(
  "vacancies-list-page",
  () => $api(api.contacts.vacancies),
);

const breadcrumbs = ref([
  {
    title: "Главная",
    url: "/",
  },
  {
    title: "Вакансии",
    url: "/vacancies",
  },
]);
</script>

<template>
  <div class="vacancies-page">
    <PagesTopSection title="Наши вакансии" />
    <div class="container">
      <BaseBreadCrumbs class="vacancies-page__breadcrumbs" :breadcrumbs />

      <div class="vacancies-page__content">
        <BaseLoader v-if="pending" />
        <BaseEmpty v-else-if="!vacanciesData" text="Вакансии не найдены" />
        <ul v-else class="vacancies-page__list">
          <li
            v-for="vacancy in vacanciesData"
            :key="vacancy.id"
            class="vacancies-page__list-item"
          >
            <VacancyCard :vacancy="vacancy" />
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.vacancies-page {
  background: $bg;
  color: $white;
  min-height: 100vh;

  .container {
    max-width: $desktop;
    margin: 0 auto;
    padding: 0 24px;

    @media (max-width: $tablet) {
      padding: 0 16px;
    }
  }

  &__content {
    margin-top: 48px;
    margin-bottom: 80px;
  }

  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 28px;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  &__list-item {
    transition:
      transform 0.25s ease,
      box-shadow 0.25s ease;

    &:hover {
      transform: translateY(-6px);

      .vacancy-card {
        border-color: $accent;
        box-shadow: 0 20px 35px -12px rgba(0, 0, 0, 0.5);
      }

      .vacancy-card__arrow {
        transform: translateX(4px);
      }
    }
  }
}

@keyframes pulse {
  0% {
    opacity: 0.6;
  }
  50% {
    opacity: 1;
  }
  100% {
    opacity: 0.6;
  }
}

@media (max-width: $laptop) {
  .vacancies-page {
    &__list {
      grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
      gap: 20px;
    }
  }
  .vacancy-card {
    padding: 20px;
  }
}

@media (max-width: $tablet) {
  .vacancies-page {
    &__list {
      grid-template-columns: 1fr;
    }
    &__content {
      margin-top: 32px;
    }
  }
}
</style>
