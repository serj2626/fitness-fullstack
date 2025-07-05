<script setup lang="ts">
import type { IPost } from "~/types";
import { api } from "~/api";

const { $api } = useNuxtApp();
const route = useRoute();

const { data: post } = await useAsyncData<IPost>(
  `post-${route.params.slug}`,
  () => $api(api.posts.detail(route.params.slug as string))
);
</script>
<template>
  <div class="post-detail" v-if="post">
    <div class="container">
      <!-- Заголовок -->
      <div class="post-header">
        <h1 class="post-title">{{ post.title }}</h1>
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
.post-detail {
  margin: 0 auto;
  padding: 20px;
  padding-block: 100px;
  color: $white;
}

.post-header {
  margin-bottom: 30px;
  text-align: center;
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

@media (max-width: $tablet) {
  .post-title {
    font-size: 1.8rem;
  }
}
</style>
