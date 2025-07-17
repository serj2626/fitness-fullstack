<script setup lang="ts">
const categories = ref([
  { id: "fitness", title: "Инструктор тренажерного зала" },
  { id: "pool", title: "Инструктор бассейна" },
  { id: "yoga", title: "Инструктор йоги" },
]);

const coachesStore = useCoachesStore();

const setActiveCategory = (cat: string) => {
  if (coachesStore.activeCategory === cat) {
    coachesStore.activeCategory = null;
  } else {
    coachesStore.activeCategory = cat;
  }
};
</script>
<template>
  <div class="coach-filters">
    <BaseButton
      v-for="category in categories"
      :key="category.id"
      :label="category.title"
      radius="15px"
      class="coach-filters__btn"
      :class="{ active: coachesStore.activeCategory === category.id }"
      @click="setActiveCategory(category.id)"
    />
  </div>
</template>
<style scoped lang="scss">
.coach-filters {
  display: flex;
  flex-wrap: wrap;
  gap: 30px;
  margin-bottom: 60px;
  justify-content: center;

  &__btn {
    position: relative;
    font-size: 14px;
    border-radius: 0;
    border: none;
    background-color: rgba(66, 62, 62, 0.847);
    border-radius: 10px;
    color: $white;
    transition: all 0.3s ease-in;
    &.active {
      position: relative;
      color: $accent;
    }
  }
}
</style>
