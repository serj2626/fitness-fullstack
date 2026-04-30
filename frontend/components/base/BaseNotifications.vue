<script setup lang="ts">
const { notifications, removeNotification } = useNotify();
</script>

<template>
  <div class="notifications-container">
    <TransitionGroup name="notification">
      <div
        v-for="notification in notifications"
        :key="notification.id"
        :class="['notification', `notification--${notification.type}`]"
        @click="removeNotification(notification.id)"
      >
        <div class="notification__content">
          {{ notification.message }}
        </div>
        <BaseButtonClose
          class="notification__close"
          color="#fff"
          top="5px"
          right="5px"
          :size="20"
          @click.stop="removeNotification(notification.id)"
        />
      </div>
    </TransitionGroup>
  </div>
</template>

<style scoped lang="scss">
.notifications-container {
  position: fixed;
  bottom: 20px;
  right: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 12px;
  max-width: 350px;
  width: 100%;
  pointer-events: none; // чтобы клик проходил сквозь контейнер, но не сквозь сами уведомления
}

.notification {
  position: relative;
  padding: 16px 20px;
  border-radius: 12px;
  color: white;
  cursor: pointer;
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.2);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 12px;
  pointer-events: auto; // уведомления кликабельны
  backdrop-filter: blur(4px);

  &--success {
    background: $success;
  }
  &--error {
    background: $red;
  }
  &--warning {
    background: $warning;
  }
  &--info {
    background: $info;
  }

  &__content {
    font-size: 0.9rem;
    font-weight: 500;
    word-break: break-word;
  }

  &__close {
    flex-shrink: 0;
  }
}

// Анимация появления/исчезновения
.notification-enter-active,
.notification-leave-active {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.notification-enter-from {
  opacity: 0;
  transform: translateX(100%);
}
.notification-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

.notification-leave-active {
  position: absolute; // важно для корректного удаления и сдвига остальных
  width: 100%;
}

// Перемещение оставшихся элементов
.notification-move {
  transition: transform 0.3s ease;
}
</style>