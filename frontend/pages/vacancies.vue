<script setup lang="ts">
import { api } from "~/api";
const { $api } = useNuxtApp();

export interface IVacanciesListPage {
  id: number;
  title: string;
  slug: string;
  content: string;
  time: string;
  created_at: Date;
  // Добавим опционально, если бек отдаёт
  salary?: string;
  location?: string;
}

const { data: vacanciesData } = await useAsyncData<IVacitiesListPage[]>(
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
        <!-- Скелетон загрузки (опционально) -->
        <div v-if="!vacanciesData" class="vacancies-page__skeleton">
          <div v-for="n in 3" :key="n" class="vacancies-page__skeleton-item"></div>
        </div>

        <!-- Список вакансий -->
        <ul v-else class="vacancies-page__list">
          <li
            v-for="vacancy in vacanciesData"
            :key="vacancy.id"
            class="vacancies-page__list-item"
          >
            <div class="vacancy-card">
              <h3 class="vacancy-card__title">{{ vacancy?.title }}</h3>
              
              <div class="vacancy-card__meta">
                <time class="vacancy-card__date" :datetime="vacancy.created_at.toString()">
                  {{ formatDate(vacancy?.created_at) }}
                </time>
                <span v-if="vacancy.location" class="vacancy-card__location">
                  {{ vacancy?.location }}
                </span>
              </div>
              
              <p class="vacancy-card__description">
                <BaseWysiwyg v-if="vacancy?.content" :html="vacancy?.content" />
              </p>
              
              <div class="vacancy-card__footer">
                <span v-if="vacancy.salary" class="vacancy-card__salary">
                  {{ vacancy?.salary }}
                </span>
                <NuxtLink :to="`/vacancies/${vacancy.slug}`" class="vacancy-card__link">
                  Подробнее
                  <span class="vacancy-card__arrow">→</span>
                </NuxtLink>
              </div>
            </div>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
// Импорт ваших переменных (они уже глобально доступны, но для ясности)
// $white, $grey, $text-secondary, $accent, $error, $success, $txt, $header_link, $bg, $bg_block, $info, $warning, $red
// $mobile, $tablet, $laptop, $desktop, $desctop_wide

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

  // Скелетон загрузки
  &__skeleton {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 28px;
  }

  &__skeleton-item {
    background: $bg_block;
    border-radius: 20px;
    height: 280px;
    animation: pulse 1.5s infinite;
  }

  // Сетка списка
  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(340px, 1fr));
    gap: 28px;
    list-style: none;
    margin: 0;
    padding: 0;
  }

  &__list-item {
    transition: transform 0.25s ease, box-shadow 0.25s ease;

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

// Карточка вакансии
.vacancy-card {
  background: $bg_block;
  backdrop-filter: blur(2px);
  border-radius: 24px;
  border: 1px solid rgba($white, 0.08);
  padding: 24px;
  height: 100%;
  display: flex;
  flex-direction: column;
  transition: all 0.25s ease;
  cursor: pointer;

  &__title {
    font-size: 1.5rem;
    font-weight: 700;
    line-height: 1.3;
    margin: 0 0 16px 0;
    color: $white;
    letter-spacing: -0.02em;
    
    @media (max-width: $tablet) {
      font-size: 1.3rem;
    }
  }

  &__meta {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    margin-bottom: 20px;
    font-size: 0.85rem;
    color: $text-secondary;
  }

  &__date {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    
    &::before {
      content: "📅";
      font-size: 0.9rem;
      opacity: 0.8;
    }
  }

  &__location {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    
    &::before {
      content: "📍";
      font-size: 0.9rem;
    }
  }

  &__description {
    color: rgba($white, 0.75);
    line-height: 1.55;
    margin: 0 0 28px 0;
    flex: 1;
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  &__footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-top: auto;
    border-top: 1px solid rgba($white, 0.08);
    padding-top: 20px;
  }

  &__salary {
    background: rgba($accent, 0.12);
    color: $accent;
    font-weight: 600;
    font-size: 0.9rem;
    padding: 6px 14px;
    border-radius: 40px;
    letter-spacing: 0.01em;
  }

  &__link {
    color: rgba($white, 0.8);
    text-decoration: none;
    font-weight: 500;
    font-size: 0.9rem;
    transition: color 0.2s ease;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    
    &:hover {
      color: $accent;
    }
  }

  &__arrow {
    transition: transform 0.2s ease;
    display: inline-block;
  }
}

// Анимация скелетона
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

// Адаптив под ваши брейкпоинты
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