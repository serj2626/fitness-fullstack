<script setup lang="ts">
const { notifications, removeNotification } = useNotify();
</script>

<template>
  <TransitionGroup
    name="notifications"
    tag="div"
    class="notifications-container"
  >
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
        :size="15"
        @click.stop="removeNotification(notification.id)"
      />
    </div>
  </TransitionGroup>
</template>

<style scoped lang="scss">
.notifications-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1000;
  display: flex;
  flex-direction: column;
  gap: 12px;
  width: 300px;
  max-width: 90vw;
}

.notification {
  position: relative;
  padding: 16px;
  border-radius: 8px;
  color: white;
  cursor: pointer;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: all 0.3s ease;
  display: flex;
  align-items: center;
  justify-content: space-between;

  &--success {
    background: #4caf50;
  }

  &--error {
    background: #f44336;
  }

  &--warning {
    background: #ff9800;
  }

  &--info {
    background: #2196f3;
  }
}

.notifications-enter-active,
.notifications-leave-active {
  transition: all 0.3s ease;
}

.notifications-enter-from,
.notifications-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

.notifications-leave-active {
  position: absolute;
}
</style>
