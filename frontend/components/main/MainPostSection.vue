<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";

// Моковые данные
const posts = ref([
  {
    id: 1,
    title: "Как правильно выполнять становую тягу",
    slug: "deadlift-technique",
    category: "workout",
    content:
      "Становая тяга - одно из ключевых упражнений в силовом тренинге. В этой статье мы разберем правильную технику выполнения...",
    preview_image: "/services/gym.jpg",
    created_at: "2023-05-15T10:30:00Z",
    views: 1245,
  },
  {
    id: 2,
    title: "Питание для набора мышечной массы",
    slug: "muscle-gain-nutrition",
    category: "nutrition",
    content:
      "Чтобы эффективно набирать мышечную массу, важно не только тренироваться, но и правильно питаться...",
    preview_image: "/services/pool.png",
    created_at: "2023-05-10T14:15:00Z",
    views: 982,
  },
  {
    id: 3,
    title: "Новый тренажерный зал в нашем клубе",
    slug: "new-gym-equipment",
    category: "news",
    content:
      "Мы рады сообщить о расширении нашего тренажерного зала! Теперь у нас появилось новое оборудование...",
    preview_image: "/services/spa.jpg",
    created_at: "2023-05-05T09:00:00Z",
    views: 1567,
  },
]);

const getCategoryName = (category) => {
  const categories = {
    workout: "Тренировки",
    nutrition: "Питание",
    news: "Новости",
    promo: "Акции",
  };
  return categories[category] || category;
};

const formatDate = (dateString) => {
  const date = new Date(dateString);
  return date.toLocaleDateString("ru-RU", {
    day: "numeric",
    month: "long",
    year: "numeric",
  });
};
</script>
<template>
  <section class="main-post-section">
    <div class="container">
      <h2 class="main-post-section__title">Последние статьи</h2>
      <p class="main-post-section__subtitle">
        Полезные материалы от наших тренеров
      </p>

      <div class="main-post-section__list">
        <article
          v-for="post in posts"
          :key="post.id"
          class="main-post-section__list-card"
          :class="`main-post-section__list-card-category_${post.category}`"
        >
          <NuxtLink
            :to="`/blog/${post.slug}`"
            class="main-post-section__list-card-link"
          >
            <div class="main-post-section__list-card-image-wrapper">
              <img
                :src="post.preview_image"
                :alt="post.title"
                class="main-post-section__list-card-image"
              />
              <span class="main-post-section__list-card-category">{{
                getCategoryName(post.category)
              }}</span>
            </div>
            <div class="main-post-section__list-card-content">
              <h3 class="main-post-section__list-card-content-title">
                {{ post.title }}
              </h3>
              <p class="main-post-section__list-card-content-excerpt">
                {{ post.content.substring(0, 100) }}...
              </p>
              <div class="main-post-section__list-card-content-meta">
                <span class="main-post-section__list-card-content-date">{{
                  formatDate(post.created_at)
                }}</span>
              </div>
            </div>
          </NuxtLink>
        </article>
      </div>
      <BaseButtonWithIcon
        label="Смотреть все статьи"
        :icon="HeroIcons.ARROW_RIGHT"
        size="md"
        class="main-post-section__button"
      />
    </div>
  </section>
</template>
<style scoped lang="scss">
.main-post-section {
  padding: 80px 0;
  background-color: $bg;
  color: $white;

  &__title {
    font-size: 2.5rem;
    margin-bottom: 15px;
    color: $accent;
    text-align: center;
  }
  &__subtitle {
    font-size: 1.2rem;
    margin-bottom: 40px;
    text-align: center;
    color: $header_link;
  }

  &__list {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    margin-bottom: 40px;
    &-card {
      background: darken($bg, 3%);
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      }
      &-link {
        text-decoration: none;
        color: inherit;
      }

      &-image-wrapper {
        position: relative;
        height: 200px;
        overflow: hidden;
      }
      &-image {
        width: 100%;
        height: 100%;
        object-fit: cover;
        transition: transform 0.5s ease;
      }
      &-category {
        position: absolute;
        top: 15px;
        right: 15px;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;

        & * {
          background: rgba(#4caf50, 0.9);
          color: $white;
        }
      }
      &-content {
        padding: 20px;
        &-title {
          font-size: 1.3rem;
          margin-bottom: 10px;
          color: $white;
        }
        &-excerpt {
          color: $header_link;
          margin-bottom: 15px;
          line-height: 1.5;
        }
        &-meta {
          display: flex;
          justify-content: space-between;
          font-size: 0.9rem;
          color: $grey;
        }
        &-date {
          color: $white;
        }
      }
    }
  }
  &__button {
    margin-inline: auto;
  }
}
</style>
