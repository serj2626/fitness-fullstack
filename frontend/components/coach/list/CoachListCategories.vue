<script setup lang="ts">
import type { ICoachCategory } from "~/types";

defineProps<{
  categories: ICoachCategory[] | [];
}>();

const model = defineModel<string | null>();
</script>
<template>
  <select v-model="model" class="coach-category-select" placeholder="Выберите категорию" >
    <option value="">Все категории</option>
    <option
      v-for="category in categories"
      :key="category.id"
      :value="category.slug"
    >
      {{ category.name }}
    </option>
  </select>
</template>
<style scoped lang="scss">
.coach-category-select {
  padding: 10px 15px;
  border: 1px solid GRAY;
  border-radius: 4px;
  background-color: white;
  color: $txt;
}
</style>
