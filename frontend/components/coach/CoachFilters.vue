<script setup lang="ts">
const categories = ref([
  { id: 1, name: "Все тренеры" },
  { id: 2, name: "Силовые" },
  { id: 3, name: "Йога" },
  { id: 4, name: "Кроссфит" },
  { id: 5, name: "Бокс" },
]);

const activeCategory = ref(1);

const setActiveCategory = (categoryId: number) => {
  activeCategory.value = categoryId;
};
</script>
<template>
  <div class="coach-filters">
    <BaseButton
      v-for="category in categories"
      :key="category.id"
      :label="category.name"
      radius="15px"
      :outline="activeCategory !== category.id"
      @click="setActiveCategory(category.id)"
    />
  </div>
</template>
<style scoped lang="scss">
.coach-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  margin-bottom: 40px;
  justify-content: center;
}
</style>
