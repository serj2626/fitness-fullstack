<script setup lang="ts">
import { NuxtImg } from "#components";
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IPost } from "~/types";

defineProps<{ post: IPost | null }>();
</script>
<template>
  <article class="post-card" @click="$router.push(`/posts/${post?.slug}`)">
    <button class="post-card__show">
      <Icon
        class="post-card-show__icon"
        :name="HeroIcons.ARROW_RIGHT"
        size="30"
      />
    </button>
    <div class="post-card__image-wrapper">
      <NuxtImg
        :src="post?.image"
        :alt="post?.title"
        lazy="loading"
        class="post-card__image"
      />
      <BaseButton
        v-if="post?.category"
        class="post-card__category"
        :label="post?.category"
        :disabled="true"
      />
    </div>
    <div class="post-card__content">
      <h3 class="post-card__content-title">
        {{ post?.title }}
      </h3>
      <div class="post-card__content-meta">
        <span class="post-card__content-date">
          {{ formatDate(post!.created_at) }}
        </span>
      </div>
    </div>
  </article>
</template>
<style scoped lang="scss">
.post-card {
  position: relative;
  background: darken($bg, 3%);
  border-radius: 8px;
  overflow: hidden;
  cursor: pointer;
  height: 100%;
  transition: transform 0.3s ease, box-shadow 0.3s ease,
    background 0.3s ease-in-out;

  &:hover {
    background: darken($bg, 22%);
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }

  &__show {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    border: none;
    background-color: $accent;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    color: $txt;
    cursor: pointer;
    transition: color 0.3s ease;
    &-icon {
      color: wheat;
    }
    &:hover {
      color: $white;
    }
  }
  &-link {
    text-decoration: none;
    color: inherit;
  }

  &__image-wrapper {
    position: relative;
    height: 300px;
    overflow: hidden;
  }
  &__image {
    width: 100%;
    height: 100%;
    object-fit: cover;
    transition: transform 0.5s ease;
  }
  &__category {
    position: absolute;
    background-color: $accent;
    color: $txt;
    top: 10px;
    right: 15px;
    padding: 5px 10px;
    border-radius: 4px;
    font-size: 0.8rem;
    font-weight: bold;
    text-transform: uppercase;
    rotate: -5deg;
  }
  &__content {
    padding: 20px;
    &-title {
      font-size: 1.3rem;
      margin-bottom: 10px;
      color: $white;
      overflow: hidden;
      text-overflow: ellipsis;
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
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
</style>
