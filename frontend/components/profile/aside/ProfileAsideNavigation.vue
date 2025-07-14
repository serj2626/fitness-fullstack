<script setup lang="ts"></script>
<template>
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
</template>
<style scoped lang="scss"></style>
