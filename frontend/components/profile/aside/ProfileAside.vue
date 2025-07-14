<script setup lang="ts"></script>
<template>
  <aside class="user-sidebar">
    <AvatarComponent class="user-sidebar__avatar" />
    <h2 class="user-sidebar__name">{{ user.name }}</h2>
    <div class="user-sidebar__membership">
      {{ membershipStatus }}
    </div>

    <!-- Статистика -->
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

    <!-- Навигация -->
    <ul class="user-sidebar__nav">
      <li class="user-sidebar__nav-item">
        <a
          href="#"
          class="user-sidebar__nav-link"
          :class="{ active: activeTab === 'visits' }"
          @click.prevent="activeTab = 'visits'"
        >
          История посещений
        </a>
      </li>
      <li class="user-sidebar__nav-item">
        <a
          href="#"
          class="user-sidebar__nav-link"
          :class="{ active: activeTab === 'purchases' }"
          @click.prevent="activeTab = 'purchases'"
        >
          Мои покупки
        </a>
      </li>
      <li class="user-sidebar__nav-item">
        <a
          href="#"
          class="user-sidebar__nav-link"
          :class="{ active: activeTab === 'trainings' }"
          @click.prevent="activeTab = 'trainings'"
        >
          Персональные тренировки
        </a>
      </li>
      <li class="user-sidebar__nav-item">
        <a
          href="#"
          class="user-sidebar__nav-link"
          :class="{ active: activeTab === 'notifications' }"
          @click.prevent="activeTab = 'notifications'"
        >
          Уведомления
          <span v-if="unreadNotifications" class="notifications__unread"></span>
        </a>
      </li>
      <li class="user-sidebar__nav-item">
        <a
          href="#"
          class="user-sidebar__nav-link"
          :class="{ active: activeTab === 'freeze' }"
          @click.prevent="activeTab = 'freeze'"
        >
          Заморозка абонемента
        </a>
      </li>
    </ul>
  </aside>
</template>
<style scoped lang="scss"></style>
