<script setup lang="ts">
import { HeroIcons } from "~/assets/icons/types/hero-icons";
import type { IPost } from "~/types";

defineProps<{ posts: IPost[] | null }>();

// Моковые данные
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
        >
          <button class="main-post-section__list-card-show">
            <Icon
              class="main-post-section__list-card-show-icon"
              :name="HeroIcons.ARROW_RIGHT"
              size="30"
            />
          </button>
          <NuxtLink
            :to="`/blog/${post.slug}`"
            class="main-post-section__list-card-link"
          >
            <div class="main-post-section__list-card-image-wrapper">
              <img
                :src="post.image"
                :alt="post.title"
                class="main-post-section__list-card-image"
              />
              <span class="main-post-section__list-card-category">
                {{ post.category }}</span
              >
            </div>
            <div class="main-post-section__list-card-content">
              <h3 class="main-post-section__list-card-content-title">
                {{ post.title }}
              </h3>
              <div class="main-post-section__list-card-content-meta">
                <span class="main-post-section__list-card-content-date">
                  {{ formatDate(post.created_at) }}
                </span>
              </div>
            </div>
          </NuxtLink>
        </article>
      </div>
      <BaseButtonWithIcon
        label="Смотреть все статьи"
        :icon="HeroIcons.ARROW_RIGHT"
        size="lg"
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
      position: relative;
      background: darken($bg, 3%);
      border-radius: 8px;
      overflow: hidden;
      transition: transform 0.3s ease, box-shadow 0.3s ease;

      &:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
      }
      &-show {
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

      &-image-wrapper {
        position: relative;
        height: 300px;
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
        background-color: $accent;
        color: $txt;
        top: 15px;
        right: 15px;
        padding: 5px 10px;
        border-radius: 4px;
        font-size: 0.8rem;
        font-weight: bold;
        text-transform: uppercase;
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
