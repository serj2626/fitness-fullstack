<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsPostsPage } from "~/assets/data/breadcrumbs.data";
import type { IPost } from "~/types";
const { $api } = useNuxtApp();

// Используем useAsyncData для SSR-совместимости
const { data: posts } = await useAsyncData<IPost[]>("posts-page-info", () =>
  $api(api.posts.list)
);

const categories = computed(() => {
  if (!posts.value) return [];
  const allCategories = posts.value.map((post) => post.category);
  return Array.from(new Set(allCategories));
});

const activeCategory = ref<string | null>(null);

const filteredPosts = computed(() => {
  if (!posts.value) return [];
  if (!activeCategory.value) return posts.value;
  return posts.value.filter((post) => post.category === activeCategory.value);
});
</script>
<template>
  <section class="posts-page">
    <PagesTopSection title="Фитнес-статьи" />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsPostsPage" />
      <div class="posts-page__filter">
        <BaseButton
          v-for="category in categories"
          :key="category"
          :label="category"
          :class="{ active: activeCategory === category }"
          @click="activeCategory = category"
        />
      </div>
      <div class="posts-page__articles">
        <PostCard
          v-for="post in filteredPosts"
          :key="post.id"
          :post="post"
          class="aposts-page__article-card"
        />
      </div>

      <div v-if="filteredPosts.length === 0" class="posts-page__empty-state">
        <Icon name="heroicons:book-open" size="60" />
        <p>Статьи не найдены</p>
        <BaseButton label="Сбросить фильтры" @click="activeCategory = null" />
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss">
.posts-page {
  &__filter {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    justify-content: center;
    margin-top: 30px;

    :deep(.base-button) {
      background: transparent;
      color: $header_link;
      border: 1px solid $grey;
      transition: all 0.3s ease;

      &:hover,
      &.active {
        background: $accent;
        color: $txt;
        border-color: $accent;
        transform: translateY(-2px);
      }
    }
  }

  &__articles {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;
    margin-block: 40px;
    &-card {
      transition: all 0.3s ease;

      &:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(0, 0, 0, 0.3);
      }
    }
  }
  &__empty-state {
    text-align: center;
    padding: 60px 0;
    color: $header_link;

    svg {
      margin-bottom: 20px;
      color: $grey;
    }

    p {
      font-size: 1.2rem;
      margin-bottom: 20px;
    }

    :deep(.base-button) {
      background: $accent;
      color: $txt;
      padding: 12px 24px;
    }
  }
}
</style>
