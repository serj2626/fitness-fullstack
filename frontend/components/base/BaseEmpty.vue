<script setup lang="ts">
defineProps<{
  text?: string;
  icon?: string;
}>();
</script>

<template>
  <div class="base-empty">
    <div class="empty-content">
      <Icon name="icon:anti-smile" class="empty-icon" />
      <h3 class="empty-title">{{ text || "Здесь пока ничего нет" }}</h3>
      <p class="empty-subtitle">Будьте первым, кто оставит отзыв</p>
    </div>
  </div>
</template>

<style scoped lang="scss">
.base-empty {
  display: flex;
  align-items: center;
  justify-content: center;
  min-height: 300px;
  padding: 2rem;
  text-align: center;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 12px;
  border: 1px dashed rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;

  .empty-content {
    max-width: 400px;
    margin: 0 auto;
  }

  .empty-icon {
    width: 80px;
    height: 80px;
    margin: 0 auto 1.5rem;
    color: var(--accent);
    opacity: 0.7;
  }

  .empty-title {
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 0.5rem;
    color: white;
  }

  .empty-subtitle {
    font-size: 1rem;
    color: rgba(255, 255, 255, 0.6);
    margin-bottom: 1.5rem;
    line-height: 1.5;
  }
}
</style>
