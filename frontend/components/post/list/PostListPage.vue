<script setup lang="ts">
import { api } from "~/api";
import { breadcrumbsPostsPage } from "~/assets/data/breadcrumbs.data";
import type { IPost } from "~/types";
const { $api } = useNuxtApp();

const { data: posts } = await useAsyncData<IPost[]>("post-list-page-info", () =>
  $api(api.posts.list)
);

// const categories = computed(() => {
//   if (!posts.value) return [];
//   const allCategories = posts.value.map((post) => post.category);
//   return Array.from(new Set(allCategories));
// });

// const activeCategory = ref<string | null>(null);

// const filteredPosts = computed(() => {
//   if (!posts.value) return [];
//   if (!activeCategory.value) return posts.value;
//   return posts.value.filter((post) => post.category === activeCategory.value);
// });
</script>
<template>
  <section class="post-list-page">
    <PagesTopSection title="Новости и статьи" />
    <div class="container">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsPostsPage" />
      <PostListFilter />
      <div class="post-list-page__articles">
        <PostCard
          v-for="post in posts"
          :key="post.id"
          :post="post"
          class="apost-list-page__article-card"
        />
      </div>

      <!-- <div v-if="filteredPosts.length === 0" class="post-list-page__empty-state">
        <Icon name="heroicons:book-open" size="60" />
        <p>Статьи не найдены</p>
        <BaseButton label="Сбросить фильтры" @click="activeCategory = null" />
      </div> -->
    </div>
  </section>
</template>
<style scoped lang="scss">
.post-list-page {
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
  }
}
</style>
