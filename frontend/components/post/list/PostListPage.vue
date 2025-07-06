<script setup lang="ts">
import { breadcrumbsPostsPage } from "~/assets/data/breadcrumbs.data";

const postsStore = usePostsStore();
const { loading, filterPosts } = storeToRefs(postsStore);

await useAsyncData("posts", async () => {
  await postsStore.getAllPosts();
  return postsStore.posts;
});
</script>
<template>
  <section class="post-list-page">
    <PagesTopSection title="Новости и статьи" />
    <div class="container post-list-page__content">
      <BaseBreadCrumbs :breadcrumbs="breadcrumbsPostsPage" />
      <PostListFilter />
      <BaseLoader v-if="loading" />

      <div v-else-if="filterPosts.length > 0" class="post-list-page__articles">
        <PostCard
          v-for="post in filterPosts"
          :key="post.id"
          :post="post"
          class="apost-list-page__article-card"
        />
      </div>

      <div v-else class="post-list-page__empty-state">
        <Icon name="heroicons:book-open" size="60" />
        <p>Статьи не найдены</p>
      </div>
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
  &__content {
    min-height: calc(100vh - 550px);
  }
}
</style>
