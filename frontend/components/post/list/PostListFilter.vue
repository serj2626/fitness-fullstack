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
  // :deep(.base-button) {
  //   background: transparent;
  //   color: $header_link;
  //   border: 1px solid $grey;
  //   transition: all 0.3s ease;

  //   &:hover,
  //   &.active {
  //     background: $accent;
  //     color: $txt;
  //     border-color: $accent;
  //     transform: translateY(-2px);
  //   }
}
</style>
