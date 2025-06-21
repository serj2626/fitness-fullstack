<script setup lang="ts">
const { notifications, removeNotification } = useNotify();
</script>

<template>
  <div class="fixed top-4 right-4 z-50 space-y-2">
    <div
      v-for="notification in notifications"
      :key="notification.id"
      @click="removeNotification(notification.id)"
      class="p-4 rounded-lg shadow-lg cursor-pointer"
      :class="{
        'bg-green-500 text-white': notification.type === 'success',
        'bg-red-500 text-white': notification.type === 'error',
        'bg-yellow-500 text-black': notification.type === 'warning',
        'bg-blue-500 text-white': notification.type === 'info',
      }"
    >
      {{ notification.message }}
    </div>
  </div>
</template>
