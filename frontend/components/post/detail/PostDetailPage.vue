<script setup lang="ts">
import type { IPost, ILinkBreadcrumb } from "~/types";
import { api } from "~/api";
import { breadcrumbsPostDetailPage } from "~/assets/data/breadcrumbs.data";

const { $api } = useNuxtApp();
const route = useRoute();

const { data: post } = await useAsyncData<IPost>(
  `post-${route.params.slug}`,
  () => $api(api.posts.detail(route.params.slug as string))
);

const currentPage: ILinkBreadcrumb = {
  title: post.value?.title ?? "Пост",
  url: `/posts/${post.value?.slug}`,
};
</script>
<template>
  <div v-if="post" class="post-detail-page">
    <PagesTopSection :title="post.title" />
    <div class="container">
      <BaseBreadCrumbs
        :breadcrumbs="breadcrumbsPostDetailPage"
        :current-page="currentPage"
      />
      <div class="post-header">
        <div class="post-meta">
          <span class="post-date">{{ formatDate(post.created_at) }}</span>
          <span class="post-category">{{ post.category }}</span>
        </div>
      </div>

      <!-- Изображение -->
      <NuxtImg :src="post.image" :alt="post.title" class="post-image" />
      <BaseWysiwyg v-if="post.content" :html="post.content" />
    </div>
  </div>
</template>
<style scoped lang="scss">
.post-detail-page {
  margin: 0 auto;
  color: $white;
}

.post-header {
  margin-bottom: 30px;
  text-align: center;
  padding-block: 50px;
}

.post-title {
  font-size: 2.2rem;
  margin-bottom: 10px;
  line-height: 1.3;
}

.post-meta {
  display: flex;
  justify-content: center;
  gap: 15px;
  color: rgba($white, 0.7);
  font-size: 0.9rem;
}

.post-image {
  width: 100%;
  border-radius: 8px;
  margin-bottom: 30px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.2);
}
</style>
