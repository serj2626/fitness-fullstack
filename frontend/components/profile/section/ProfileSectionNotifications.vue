<script setup lang="ts"></script>
<template>
  <section class="user-main__section" v-if="activeTab === 'notifications'">
    <div class="user-main__section-header">
      <h2 class="user-main__section-title">Уведомления</h2>
      <div class="user-main__section-actions">
        <button class="user-main__btn" @click="markAllAsRead">
          Прочитать все
        </button>
      </div>
    </div>

    <div class="notifications">
      <div
        class="notifications__item"
        v-for="notification in notifications"
        :key="notification.id"
        @click="markAsRead(notification.id)"
      >
        <div
          class="notifications__icon"
          :class="`notifications__icon--${notification.type}`"
        >
          <svg width="20" height="20" viewBox="0 0 24 24">
            <path
              fill="currentColor"
              :d="notificationIcon(notification.type)"
            />
          </svg>
        </div>
        <div class="notifications__content">
          <h3 class="notifications__title">{{ notification.title }}</h3>
          <p class="notifications__text">{{ notification.text }}</p>
          <div class="notifications__time">
            {{ formatTime(notification.time) }}
          </div>
        </div>
        <span v-if="!notification.read" class="notifications__unread"></span>
      </div>
    </div>
  </section>
</template>
<style scoped lang="scss"></style>
