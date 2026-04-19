<script setup lang="ts">
const postsStore = usePostsStore();
const { type } = storeToRefs(postsStore);
const { changeType } = postsStore;

const categories = [
  { label: "article", title: "Статьи" },
  { label: "news", title: "Новости" },
];
</script>
<template>
  <div class="post-list-filter">
    <BaseButton
      v-for="category in categories"
      :key="category.label"
      :label="category.title"
      :outline="type !== category.label"
      class="post-list-filter__btn"
      :class="{ active: type === category.label }"
      @click="changeType(category.label as 'article' | 'news')"
    />
  </div>
</template>
<style scoped lang="scss">
.post-list-filter {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
  justify-content: center;
  margin-top: 30px;
  &__btn {
    background: transparent;
    color: $white;
    border: none;
    border-radius: 0;
    width: max-content;
    transition: all 0.3s ease;
    &:hover {
      background-color: transparent;
      color: $white;
    }

    &.active {
      position: relative;
      color: $accent;
      transform: translateY(-2px);
      &::after {
        content: "";
        position: absolute;
        bottom: -6px;
        left: 50%;
        transform: translateX(-50%);
        width: 80%;
        height: 2px;
        background-color: $accent;
      }
    }
  }
}
</style>
