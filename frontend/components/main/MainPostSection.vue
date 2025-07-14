<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IPost } from "~/types";

defineProps<{ posts: IPost[] | null }>();
</script>
<template>
  <section class="main-post-section">
    <div class="container">
      <h2 class="main-post-section__title">Последние статьи</h2>
      <p class="main-post-section__subtitle">
        Полезные материалы от наших тренеров
      </p>

      <PostSwiper :posts="posts" />
      <BaseButtonWithIcon
        label="Смотреть все статьи"
        :icon="HeroIcons.ARROW_RIGHT"
        size="lg"
        class="main-post-section__button"
        @click="$router.push('/posts')"
      />
    </div>
  </section>
</template>
<style scoped lang="scss">
.main-post-section {
  background-color: $bg_block;
  padding: 80px 0;
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

  &__button {
    margin-inline: auto;
  }
}
</style>
