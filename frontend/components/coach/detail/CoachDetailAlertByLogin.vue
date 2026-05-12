<script setup lang="ts"></script>
<template>
  <div class="coach-detail-alert-by-login">
    <p>Для того, чтобы оставить отзыв, войдите в свой аккаунт.</p>
    <BaseButton label="Войти" size="md" outline />
  </div>
</template>
<style scoped lang="scss">
.coach-detail-alert-by-login {
  background: rgba($white, 0.05);
  border-radius: 12px;
  padding: 24px;
  color: $white;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: space-between;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
}
</style>
