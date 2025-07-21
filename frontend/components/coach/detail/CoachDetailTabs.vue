<script setup lang="ts">
defineProps<{ activeTab: string }>();
const tabs: { id: string; label: string }[] = [
  { id: "contacts", label: "Контакты" },
  { id: "photos", label: "Фотографии" },
  { id: "reviews", label: "Отзывы" },
];

defineEmits(["update:activeTab"]);
</script>
<template>
  <div class="coach-detail-tabs">
    <button
      v-for="tab in tabs"
      :key="tab.id"
      :class="{ active: activeTab === tab.id }"
      @click="$emit('update:activeTab', tab.id)"
    >
      {{ tab.label }}
    </button>
  </div>
</template>
<style scoped lang="scss">
.coach-detail-tabs {
  display: flex;
  border-bottom: 1px solid rgba($white, 0.1);
  margin-bottom: 30px;

  button {
    padding: 12px 25px;
    color: rgba($white, 0.7);
    position: relative;
    font-weight: 500;

    &.active {
      color: $accent;

      &::after {
        content: "";
        position: absolute;
        bottom: -1px;
        left: 0;
        width: 100%;
        height: 2px;
        background: $accent;
      }
    }
  }
}
</style>
