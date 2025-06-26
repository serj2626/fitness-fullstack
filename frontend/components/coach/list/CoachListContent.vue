<script setup lang="ts">
import type { ICoach } from "~/types";

const categories = ref([
  { id: "all", name: "Все тренеры" },
  { id: "strength", name: "Силовые" },
  { id: "yoga", name: "Йога" },
  { id: "crossfit", name: "Кроссфит" },
  { id: "boxing", name: "Бокс" },
]);

const activeCategory = ref("all");

const setActiveCategory = (categoryId) => {
  activeCategory.value = categoryId;
};

defineProps<{
  coaches: ICoach[] | null;
}>();
</script>
<template>
  <main class="coach-list-content">
    <div class="coach-list-content__filters">
      <button
        v-for="category in categories"
        :key="category.id"
        @click="setActiveCategory(category.id)"
        :class="{ active: activeCategory === category.id }"
      >
        {{ category.name }}
      </button>
    </div>

    <div class="coach-list-content__trainers">
      <TrainerCard v-for="trainer in coaches" :key="trainer.id" :trainer />
    </div>
  </main>
</template>
<style scoped lang="scss">
.coach-list-content {
  padding: 60px 0;

  &__filters {
    display: flex;
    flex-wrap: wrap;
    gap: 10px;
    margin-bottom: 40px;
    justify-content: center;

    button {
      background: none;
      border: 1px solid $grey;
      padding: 8px 20px;
      border-radius: 20px;
      cursor: pointer;
      transition: all 0.3s;
      font-weight: 500;

      &.active,
      &:hover {
        background: $accent;
        border-color: $accent;
        color: $txt;
      }
    }
  }
  &__trainers {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 30px;

    @media (max-width: $tablet) {
      grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    }

    @media (max-width: $mobile) {
      grid-template-columns: 1fr;
    }
  }
}
</style>
