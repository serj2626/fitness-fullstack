<script setup lang="ts">
import type { ICoachCategory } from "~/types";
const store = useCoachesStore();

defineProps<{
  categories: ICoachCategory[] | [];
}>();

const model = defineModel<string | null>();
</script>
<template>
  <div class="coach-list-categories">
    <select v-model="model" class="coach-category-select">
      <option :value="null">Выберите категорию</option>
      <option
        v-for="category in categories"
        :key="category.id"
        :value="category.slug"
      >
        {{ category.name }}
      </option>
    </select>
    <BaseButton
      v-if="store.activeCategory"
      size="xs"
      label="Сбросить фильтр"
      outline
      style="margin-left: 10px"
      color="#fff"
      @click="store.activeCategory = null"
    />
  </div>
</template>
<style scoped lang="scss">
.coach-list-categories {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-block: 20px;
}
.coach-category-select {
  padding: 10px 35px;
  border: 1px solid GRAY;
  width: fit-content;
  border-radius: 4px;
  background-color: $bg;
  color: $white;

  &:focus {
    border-color: $accent;
    outline: none;
  }

  // Убираем стандартную стрелку
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;

  // Своя стрелка (например, через фон)
  background-image: url("data:image/svg+xml;charset=utf-8,%3Csvg xmlns='http://www.w3.org/2000/svg' width='16' height='16' viewBox='0 0 24 24' fill='white' stroke='%23333' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 12px center;
  background-size: 18px;

  // Чтобы фон не перекрывал текст при длинном списке (опционально)
  cursor: pointer;
}
</style>
