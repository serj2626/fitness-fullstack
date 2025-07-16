<script setup lang="ts">
const postsStore = usePostsStore();
const { categories, activeCategory } = storeToRefs(postsStore);
const { selectCategory } = postsStore;
</script>
<template>
  <div class="post-list-filter">
    <BaseButton
      v-for="category in categories"
      :key="category.label"
      :label="category.label"
      :outline="activeCategory !== category.label"
      :class="{ active: activeCategory === category.label }"
      @click="selectCategory(category.label)"
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
  :deep(.base-button) {
    background: transparent;
    color: $white;
    border: none;
    border-radius: 0;
    width: max-content;
    transition: all 0.3s ease;

    &.active {
      position: relative;
      color: $accent;
      transform: translateY(-2px);
      &::after{
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
