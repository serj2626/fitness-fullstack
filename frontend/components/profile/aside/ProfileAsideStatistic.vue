<script setup lang="ts"></script>
<template>
  <div class="user-sidebar__stats">
    <div class="user-sidebar__stat">
      <div class="user-sidebar__stat-value">{{ stats.visits }}</div>
      <div class="user-sidebar__stat-label">Посещений</div>
    </div>
    <div class="user-sidebar__stat">
      <div class="user-sidebar__stat-value">{{ stats.trainings }}</div>
      <div class="user-sidebar__stat-label">Тренировки</div>
    </div>
    <div class="user-sidebar__stat">
      <div class="user-sidebar__stat-value">{{ stats.daysLeft }}</div>
      <div class="user-sidebar__stat-label">Дней осталось</div>
    </div>
    <div class="user-sidebar__stat">
      <div class="user-sidebar__stat-value">{{ stats.freezeDays }}</div>
      <div class="user-sidebar__stat-label">Заморожено</div>
    </div>
  </div>
</template>
<style scoped lang="scss"></style>
