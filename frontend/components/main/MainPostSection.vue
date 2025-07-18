<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IPost } from "~/types";

defineProps<{ posts: IPost[] | null }>();
</script>
<template>
  <section
    class="main-post-section"
    data-aos="fade-up"
    data-aos-duration="2000"
  >
    <div class="container">
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
  &__button {
    margin-inline: auto;
  }
}
</style>
